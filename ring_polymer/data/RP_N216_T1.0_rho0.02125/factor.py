import numpy as np
import codemodule as cm
boxL = 63.50
typeA = 0
q_max = 6

q_max2 = q_max * q_max
two_pi_invboxL = 2 * np.pi / boxL

frame,types = cm.read_xyz('frames.xyz',1000,1001)
frame = frame[0]
N = len(types)
NA = np.unique(types, return_counts = True)[1][0]
print(NA)

Sqs, counts = np.zeros(q_max2), np.zeros((q_max2), dtype = int)
for qi in range(0, q_max + 1):
  for qj in range(-q_max, q_max + 1):
    for qk in range(-q_max, q_max + 1):
      n = qi * qi + qj * qj + qk * qk
      if (n > 0) and (n <= q_max2):
        print(n)
        Csum, Ssum = 0.0, 0.0
        for p in range(N):
          if types[p] == typeA:
            qr = two_pi_invboxL * (qi * frame[p,0] + qj * frame[p,1] + qk * frame[p,2])
            Csum += np.cos(qr)
            Ssum += np.sin(qr)
        Sqs[n - 1] += Csum * Csum + Ssum * Ssum
        counts[n - 1] += 1
Sqs /= (counts * NA)
qs = two_pi_invboxL * np.sqrt(np.arange(0, q_max2, dtype = float) + 1)
Sqs= Sqs[~np.isnan(Sqs)]
qs = qs[:len(Sqs)]
print(len(Sqs))
print(len(qs))
