#!/bin/bash
path=dynana_test/msds/
#Ls='044.03 046.78 050.40 055.47 063.50 080.00 108.60'
partind=350
r_cs='4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0'
for r_c in $r_cs; do
  python3 dyn_lifetime.py --cutoff 0.2 --r_c ${r_c} --file coms/MIXTURE_N1-256_N2-256_MPR1-50_MPR2-50_Bend1-00.0_Bend2-30.0_L-044.03-com.lammpstrj  --save_path ./dyn_graph_res/lifetime_data/lifetime_N256,256_L044.03_partind${partind}_rc${r_c}_MR.dat --part_ind ${partind} 
done



