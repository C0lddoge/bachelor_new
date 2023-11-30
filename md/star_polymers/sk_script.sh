#Ls='80.0 63.5 55.47 50.4 46.78 44.03'

Ls=(12.38 11.35)
N1s=(400 400)
N2s=(112 112)

for idx in "${!Ls[@]}"; do
  L=${Ls[$idx]}
  N1=${N1s[$idx]}
  N2=${N2s[$idx]}
  python3 sk_script.py --file ./data/SP_N${N1},${N2}_L${L}_f166,200/dump_equilibrated.lammpstrj --qmax 10 --type 1 --cutoff 0.2 --save_file ./Sqs/data/SP_N${N1},${N2}_L${L}_f166,200_Sqs_1.dat --bin_len 20
done
