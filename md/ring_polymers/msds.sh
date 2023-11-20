#!/bin/bash
path=dynana_test/msds/
Ls='80.0'
for L in $Ls; do
  python3 msd_lammpstrj.py --cutoff 0.2 --file ./data/RP_N256,256_L${L}_newpot/dump.lammpstrj --Nlag 20 --bin_len 40 --save_dir ./rdf_diff_res/MSDs_newpot/ --type 2
done



