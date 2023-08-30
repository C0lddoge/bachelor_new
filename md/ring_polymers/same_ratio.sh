#!/bin/bash
path=./
Ls='044.03'
lags='1'
types='1 2'

for L in $Ls; do
  for lag in $lags; do
    for ty in $types; do
      python3 same_ratio.py --file coms/MIXTURE_N1-256_N2-256_MPR1-50_MPR2-50_Bend1-00.0_Bend2-30.0_L-${L}-com.lammpstrj --lag ${lag} --save_path ${path}RP_N256,256_L${L}_mr_SR_lag${lag}_type${ty}.dat --r_c 4.5 --error_len 10 --low_s 2 --high_s 5 --bin_width 0.05 --cutoff 0.2 --type_flag ${ty}
    done
  done
done

  
