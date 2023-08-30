#!/bin/bash
path=dynana_test/msds/
rhos='0.02 0.05 0.1'
damps='500 700 1000'
for rho in $rhos; do
  for damp in $damps; do
    python3 diff_script.py --file ${path}LJ_N500_rho${rho}_damp${damp}dt_MSDs_1_err.dat --rho ${rho} --save_path dynana_test/diff_coeff_damp${damp}dt.dat --t1 100 --t2 10000 
done
done



