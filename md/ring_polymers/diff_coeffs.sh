#!/bin/bash
path=./rdf_diff_res/MSDs_newdamp/
Ls='108.6 80.0 63.5 55.47 50.4 46.78 44.03'
types=( '1' '2')
#Rgs=('3.55' '6.5')
for L in $Ls; do
  for i in "${!types[@]}"; do
    echo ${i}
    python3 diff_script.py --file ${path}RP_N256,256_L${L}_NVT_MSDs_${types[i]}_err.dat --L ${L} --save_path ./rdf_diff_res/diff_data/diff_coeff_ty${types[i]}_nvt.dat --t1 100 --t2 50000
  done
done



