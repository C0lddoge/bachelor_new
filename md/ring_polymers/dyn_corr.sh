#!/bin/bash
path=dynana_test/msds/
Ls='44.03 46.78 50.4 55.47 63.5 80.0 108.6'
partind=350
for L in $Ls; do
  python3 dyn_corr.py --cutoff 0.2 --r_c 4.5 --file data/RP_N256,256_L${L}_newdamp/dump.lammpstrj  --save_path ./dyn_graph_res/diffcorr_data/diffcorr_N256,256_L${L}_partind${partind}_CG.dat --part_ind ${partind} 
done



