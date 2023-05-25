#!/bin/bash
path=./results_21.5/vanhove_data/
Ls='108.6 80.0 63.5 55.47 50.4 46.78 44.03 97.21'
lags='1 5 10 20 50 100 200'
types='1 2 all'

for L in $Ls; do
  for lag in $lags; do
    for ty in $types; do
      python3 van_hove.py --file data/RP_N256,256_L${L}/dump.lammpstrj --lag ${lag} --save_path ${path}RP_N256,256_L${L}_vh_lag${lag}_type${ty}.dat --error_len 50 --bin_low 0 --bin_high 250 --bin_number 5000 --cutoff 0.2 --types ${ty}
    done
  done
done

  
