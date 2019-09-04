# utility / helper functions to work with scikit-allel, pandas, and matplotlib
# python3

import sys
import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import zarr
import allel

__version__ = '0.2.0'

#########################################
# General utility
#########################################

def str2int(s):
    """return the int value of string, handles strings like 1e6 too"""
    rv = None
    try:
        rv = int(s)
    except ValueError:
        rv = int(float(s))
    return rv

#########################################
# General sequence related utility
#########################################

def str2range(s):
    """parse a samtools/tabix type region specification 'chr:start-stop'"""
    chrom = None
    start = 1
    stop = None
    tmp = s.split(':')
    chrom = tmp[0]
    if len(tmp)>1:
        if '-' in tmp[1]:
            tmp = tmp[1].split('-')
        else:
            tmp = tmp[1].split('..')
        start = str2int(tmp[0])
        if len(tmp)>1:
            stop = str2int(tmp[1])
    return (chrom, start, stop)

#########################################
# Matplotlib related
#########################################

def twinx_below(ax, *args, **kwargs):
    ax2 = ax.twinx(*args, **kwargs)
    ax2.set_zorder(ax.get_zorder()-1)
    ax2.patch.set_visible(True)
    ax.patch.set_visible(False)
    return ax2

#########################################
# scikit-allel related
#########################################

def LoadRegion(callset,
               meta, # minimally a dataframe with sample names as index
               region,
               min_FMTDP=0,
               filter_snp=False,
               filter_biallelic=False,
               max_missing_proportion=None,
               group_col=None, # column name in meta used to identify groups for group_max_missing_proportion
               group_max_missing_proportion=None):
    # NOTE: returned meta should be in the same order and same length as the returned genotype array
    
    # determine the index in the full callset for all the samples in meta
    callset_all_sample_ids = list(list(callset.values())[0]['samples'])
    meta['callset_idx'] = [callset_all_sample_ids.index(x) for x in meta.index]
    meta['idx'] = np.arange(meta.shape[0]) # index in the genotype array

    ch, start, stop = str2range(region)
    print("Region:", region, '->', (ch,start,stop))

    pos = allel.SortedIndex(callset[ch]['variants/POS'])
    if pos.shape[0] == 0: # return empty if nothing for chrom
        return [],[],meta
    # create the slice
    try:
        sl = pos.locate_range(start,stop)
        pos = pos[sl]
    except KeyError:
        pos = []
    if len(pos) == 0: # no loci in slice
        return [],[],meta

    # load combined set of both groups
    sample_idxs = meta['callset_idx'].values
    g = allel.GenotypeDaskArray(callset[ch]['calldata/GT'])[sl].take(sample_idxs, axis=1)
    g = g.compute() # need to convert GenotypeDaskArray to GenotypeArray

    ## Filtering
    num_loci_in = g.shape[0]
    flt = np.ones(num_loci_in, dtype=bool)
    ac = None
    print('total number of loci =',flt.shape[0])

    # filter genotypes on FMT:DP
    if min_FMTDP > 0:
        genoflt_FMTDP = callset[ch]['calldata/DP'][sl].take(sample_idxs, axis=1) < min_FMTDP
        g[genoflt_FMTDP] = [-1,-1]
        tmp_num_calls = g.shape[0]*g.shape[1]
        tmp = np.count_nonzero(genoflt_FMTDP)
        print('{} genotype calls of {} ({:02.2f}%) fail FMT:DP filter'.format(
                tmp, tmp_num_calls, 100*tmp/float(tmp_num_calls)))

    if filter_snp:
        flt_snp = np.all(np.logical_or(callset[ch]['variants/TYPE'][sl] == 'snp',
                                           callset[ch]['variants/TYPE'][sl] == ''), axis=1)
        flt = flt & flt_snp
        print('=',np.count_nonzero(flt), 'passing previous filters & SNP')

    if filter_biallelic:
        if ac is None:
            ac = g.count_alleles()
        flt_biallelic = ac.allelism() == 2
        flt = flt & flt_biallelic
        print('=',np.count_nonzero(flt), 'passing previous filters & biallelic')

    # filter max_missing (genotype calls)
    if max_missing_proportion is not None:
        max_missing = int(np.floor(g.shape[1]*max_missing_proportion))
        flt_max_missing = g.is_missing().sum(axis=1) <= max_missing
        tmp = np.count_nonzero(flt_max_missing)
        print("max missing proportion {} of {} is {}".format(max_missing_proportion, g.shape[1], max_missing))
        print("max missing passing loci = {} ({:2.2f}%)".format(tmp, 100*tmp/flt_max_missing.shape[0]))
        flt = flt & flt_max_missing
        print('=',np.count_nonzero(flt), 'passing previous filters & max_missing')

    if group_max_missing_proportion is not None and group_col is not None:
        gmmflt = np.ones(g.shape[0], dtype=bool)
        for grp in meta[group_col].unique():
            grp_meta = meta[meta[group_col]==grp]
            max_missing = int(np.floor(grp_meta.shape[0]*group_max_missing_proportion))
            print("### Group max missing filter:", grp)
            print(grp_meta['idx'])
            print("N =", grp_meta.shape[0])
            print("max missing =", max_missing)
            print("loci in =",flt.shape[0])
            f = g[:,grp_meta['idx']].is_missing().sum(axis=1) <= max_missing
            tmp = np.count_nonzero(f)
            print("passing loci = {} ({:2.2f}%)".format(tmp, 100*tmp/f.shape[0]))
            gmmflt = gmmflt & f
        tmp = np.count_nonzero(mmflt)
        print("passing all max missing filters {:d} of {:d} ({:.2f}%)".format(
                tmp, gmmflt.shape[0], 100*tmp/gmmflt.shape[0]))
        flt = flt & gmmflt
        print('=',np.count_nonzero(flt), 'passing previous filters & max_missing')

    # apply combined filter
    tmp = np.count_nonzero(flt)
    print("Passing all all filters {:d} of {:d} ({:.2f}%)".format(tmp, flt.shape[0], 100*tmp/flt.shape[0]))
    return g.compress(flt, axis=0), pos.compress(flt, axis=0), meta


