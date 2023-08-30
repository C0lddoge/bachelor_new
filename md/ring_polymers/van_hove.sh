#!/bin/bash
path=./cluster_vh_res/vanhove_data/
Ls='108.60 080.00 063.50 055.47 050.40 046.78 044.03'
lags='1 5 10 20 50 100'
types='1 2'

for L in $Ls; do
  for lag in $lags; do
    for ty in $types; do
      python3 van_hove.py --file coms/MIXTURE_N1-256_N2-256_MPR1-50_MPR2-50_Bend1-00.0_Bend2-30.0_L-${L}-com.lammpstrj --lag ${lag} --save_path ${path}RP_N256,256_L${L}_mr_vh_lag${lag}_type${ty}.dat --error_len 50 --bin_low 0 --bin_high 250 --bin_number 5000 --cutoff 0.2 --types ${ty}
    done
  done
done

  
