#!/usr/bin/env python3

import sys; print(sys.version)
import os
import glob
import subprocess
import multiprocessing

import numpy as np; print('numpy', np.__version__)

import pandas as pd; print('pandas',pd.__version__)
import allel; print('allel', allel.__version__)
import zarr; print('zarr', zarr.__version__)

INFN = sys.argv[1]
if not INFN:
    print('Must provide input .vcf.gz as first argument')
    sys.exit(2)

OUTFN = INFN+'.zarr'

# Below will probably not need to be changed
FIELDS = [
    'samples',
    'variants/CHROM',
    'variants/POS',
    'variants/REF',
    'variants/ALT',
    'variants/QUAL',
    'variants/TYPE',
    'variants/NUMALT',
    'variants/AF',
    'variants/DP',
#     'variants/ANN',
    'calldata/DP',
    'calldata/GT',
         ]
EXCLUDE_FIELDS = None

# # ALTERNATIVE:
# # All the fields from the VCF (overkill leads to very big archive)
# FIELDS = '*'
# EXCLUDE_FIELDS = ['variants/NUMALT'] # allel will calculate a numalt (lower case) on the fly

TABIX_EXEC = 'tabix'

print("Using tabix executable '{}' {} '{}'\n{}".format(TABIX_EXEC, u"\u2192",
        subprocess.check_output(['which', 'tabix']).decode('utf-8').rstrip(),
        subprocess.check_output([TABIX_EXEC, '--version']).decode('utf-8')))

chroms = subprocess.check_output([TABIX_EXEC,'-l',INFN],
                                 universal_newlines=True).strip().split('\n')
#print(chroms)

num_procs = multiprocessing.cpu_count()-1

transformers = None
if 'ANN' in FIELDS:
    transformers=allel.ANNTransformer()

def vcf_to_zarr_func(ch):
    allel.vcf_to_zarr(INFN, OUTFN,
                      region=ch,
                      group=ch,
                      log=sys.stderr,
                      fields=FIELDS,
                      exclude_fields=EXCLUDE_FIELDS,
                      tabix=TABIX_EXEC,
                      transformers=transformers)

with multiprocessing.Pool(num_procs) as pool:
    pool.map(vcf_to_zarr_func, chroms, chunksize=1)
