#!/bin/bash
damps='500 700 1000'
rhos='0.02 0.05 0.1'
for rho in $rhos; do
  for damp in $damps; do
  cp infile.lmp LJ_N500_rho${rho}_damp${damp}dt
done
done



