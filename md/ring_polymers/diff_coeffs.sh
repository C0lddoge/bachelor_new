#!/bin/bash
path=results_1.5/MSDs_new/
Ls='108.6 80.0 63.5 55.47 50.4 46.78 44.03'
types=( '1' '2')
Rgs=('3.55' '6.5')
for L in $Ls; do
  for i in "${!types[@]}"; do
    echo ${i}
    python3 diff_script.py --file ${path}RP_N256,256_L${L}_MSDs_${types[i]}_err.dat --L ${L} --save_path results_1.5/diff_coeff_ty${types[i]}_rg.dat --R_g ${Rgs[i]}
  done
done



