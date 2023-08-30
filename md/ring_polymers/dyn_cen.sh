#!/bin/bash
path=dynana_test/msds/
Ls='044.03 046.78 050.40 055.47 063.50 080.00 108.60'
types='1 2'
for ty in $types; do
  for L in $Ls; do
    python3 dyn_cen.py --cutoff 0.2 --types ${ty} --error_len 10 --tau_N 20  --r_c 4.5 --file ./coms/MIXTURE_N1-256_N2-256_MPR1-50_MPR2-50_Bend1-00.0_Bend2-30.0_L-${L}-com.lammpstrj  --save_path ./dyn_graph_res/cen_data/cen_N256,256_L${L}_type${ty}_MR.dat --save_path_cenarr ./dyn_graph_res/cen_data/cen_N256,256_L${L}_type${ty}_cenarr_MR.dat 
  done
done




