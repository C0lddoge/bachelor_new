#!/bin/bash
path=dynana_test/msds/
rhos='0.02 0.05 0.1'
damps='500 700 1000'
for rho in $rhos; do
  for damp in $damps; do
    python3 msd_lammpstrj.py --cutoff 0.3 --file data/LJ_N500_rho${rho}_damp${damp}dt/dump10mio.lammpstrj --integration_step 0.005 --Nlag 20 --bin_len 40 --save_dir dynana_test/msds/
  done
done



