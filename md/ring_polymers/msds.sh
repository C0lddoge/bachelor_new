#!/bin/bash
path=dynana_test/msds/
Ls='044.03 046.78 050.40 055.47 063.50 080.00 108.60'
for L in $Ls; do
  python3 msd_lammpstrj.py --cutoff 0.2 --file coms/MIXTURE_N1-256_N2-256_MPR1-50_MPR2-50_Bend1-00.0_Bend2-30.0_L-${L}-com.lammpstrj --Nlag 20 --bin_len 40 --save_dir ./rdf_diff_res/MSDs_mr/ --type 2
done



