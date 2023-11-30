#Ls='80.0 63.5 55.47 50.4 46.78 44.03'

Ls=(13.02 12.77 12.57 12.21)
N1s=(243 243 243 243)
N2s=(243 243 243 243)
N3s=(243 243 243 243)
for idx in "${!Ls[@]}"; do
  L=${Ls[$idx]}
  N1=${N1s[$idx]}
  N2=${N2s[$idx]}
  N3=${N3s[$idx]}
  python3 gr_script.py --file ./data/SP_N${N1},${N2},${N3}_L${L}_sig1.0,1.2,0.8/dump.lammpstrj --cutoff 0.2 --save_dir ./rdfs/data/ --bin_len 20
done
