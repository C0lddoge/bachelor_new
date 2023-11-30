#!/bin/bash
path=dynana_test/msds/
Ls='12.57'
for L in $Ls; do
  python3 msd_lammpstrj.py --cutoff 0.2 --file ./data/SP_N243,243,243_L${L}_sig1.0,1.2,0.8/dump_quickrestart.lammpstrj --Nlag 20 --bin_len 40 --save_dir ./MSDs --type 1
done



