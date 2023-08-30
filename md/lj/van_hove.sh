#!/bin/bash
path=./dynana_test/vanhove_data/
rhos='0.02 0.05 0.1'
damps='500 700 1000'
lags='1 5 10 20 50 100 200'
types='1'

for rho in $rhos; do
  for damp in $damps; do
  for lag in $lags; do
    for ty in $types; do
      python3 van_hove.py --file data/LJ_N500_rho${rho}_damp${damp}dt/dump10mio.lammpstrj --lag ${lag} --save_path ${path}LJ_N500_rho${rho}_vh_lag${lag}_type${ty}_damp${damp}dt.dat --error_len 50 --bin_low 0 --bin_high 150 --bin_number 5000 --cutoff 0.2 --types ${ty}
    done
  done
  done
done

  
