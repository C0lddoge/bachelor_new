#!/bin/bash
damps='500 700 1000'
rhos='0.02 0.05 0.1'
for rho in $rhos; do
  for damp in $damps; do
  cd LJ_N500_rho${rho}_damp${damp}dt
  ~/mylammps/src/lmp_serial -i infile.lmp -var damp ${damp} -var dt 0.01
  cd ../
done
done



