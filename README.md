# gambiae-dispersal
An. gambiae transcontinental dispersal analysis custom scripts (2019)

For the 2019 paper:
## A new model of West African origin and transcontinental dispersal via serial founder events of Anopheles gambiae

Hanno Schmidt, Yoosook Lee, Travis C. Collier, Mark J. Hanemaaijer, Oscar D. Kirstein, Ahmed Ouledi,
Mbanga Muleba, Douglas E. Norris, Montgomery Slatkin, Anthony J. Cornel, Gregory C. Lanzaro

## F<sub>ST</sub> and Sequence Diversity (&pi);
- `sample_meta.csv` (data) : Sample metadata file.  Generally useful
- `Whole_genome_Fst_and_pi.ipynb` : Jupyter notebook computing F<sub>ST</sub> and &pi;
- `allel_helpers.py`: small module used by `Whole_genome_Fst_and_pi.ipynb` to simplify loading data
- `vcf2zarr.py` : standalone script which converts a vcf file to a zarr archive
- `hfst_by_group.csv` (results) : Hudson's F<sub>ST</sub> estimator for each pair of sample groups
- `hfst_se_by_group.csv` (results) : Standard error estimates of `hfst_by_group.csv`
- `pi_by_group.csv` (results) : Sequence diversity (&pi;) within each sample group

## MSMC2 analysis
Link to MSMC2 code : https://github.com/stschiff/msmc2
msmc2_notes.txt : Working notes on how msmc2 was run
msmc2_sequential.sh : script runing sequential 4 specimen analyses
msmc2_CC.sh : script for cross-coalescence pairs
msmc2_CC_CO_vs_EA.sh : script for cross-coalescence Comoros vs East Africa only
msmc2_Ne_data.hdf (data) 
msmc2_RCC_data.hdf (data) 
MSMC_plot-v2.ipynb : 


