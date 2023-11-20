#!/bin/bash
path=./cluster_vh_res/cluster_data_M100,25_k0,30/
#Ls='108.6 97.21 80.0 63.5 55.47 50.4 46.78 44.03'
rcs='4.5'
Ls=(58.48 99.99)
N1s=(500 500)
N2s=(500 500)
for idx in "${!Ls[@]}"; do
  L=${Ls[$idx]}
  N1=${N1s[$idx]}
  N2=${N2s[$idx]}
  for rc in $rcs; do
    python3 cluster_script.py --file data/RP_N${N1},${N2}_L${L}_M100,25_k0,30/dump.lammpstrj --r_c ${rc} --cutoff 0.2 --save_path ${path}RP_N${N1},${N2}_L${L}_M100,25_k0,30_clust_rc${rc}_CG.dat --error_len 30
  done
done

  
