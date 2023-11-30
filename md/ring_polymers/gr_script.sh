#Ls='80.0 63.5 55.47 50.4 46.78 44.03'

Ls=(58.48 41.98 41.61)
N1s=(500 666 864)
N2s=(500 666 864)

for idx in "${!Ls[@]}"; do
  L=${Ls[$idx]}
  N1=${N1s[$idx]}
  N2=${N2s[$idx]}
  python3 gr_script.py --file ./data/RP_N${N1},${N2}_L${L}_M100,25_k0,30/dump.lammpstrj --cutoff 0.3 --save_dir ./rdf_diff_res/rdf_M100,25_k0,30/ --bin_len 20
done
