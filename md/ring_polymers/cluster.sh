#!/bin/bash
path=./cluster_vh_res/cluster_data/
Ls='108.6 97.21 80.0 63.5 55.47 50.4 46.78 44.03'
rcs='4.0 4.5 5.0 5.5 6.0 6.5 7.0'
for L in $Ls; do
  for rc in $rcs; do
    python3 cluster_script.py --file data/RP_N256,256_L${L}/dump.lammpstrj --r_c ${rc} --cutoff 0.2 --save_path ${path}RP_N256,256_L${L}_clust_rc${rc}_CG.dat --error_len 60
  done
done

  
