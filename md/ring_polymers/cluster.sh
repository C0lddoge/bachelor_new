#!/bin/bash
path=results_21.5/cluster_data/
Ls='108.60 097.21 080.00 063.50 055.47 050.40 046.78 044.03'
rcs='4.0 4.5 5.0 5.5 6.0 6.5 7.0'

for L in $Ls; do
  for rc in $rcs; do
    python3 cluster_script.py --file coms/MIXTURE_N1-256_N2-256_MPR1-50_MPR2-50_Bend1-00.0_Bend2-30.0_L-${L}-com.lammpstrj --r_c ${rc} --cutoff 0.2 --save_path ${path}RP_N256,256_L${L}_clust_rc${rc}_MR.dat --error_len 60
  done
done

  
