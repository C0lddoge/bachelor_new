import codemodule as cm
import numpy as np
import matplotlib.pyplot as plt

r_c = 8.5
part_ind = 150
max_lifetime = 1000
frames_mr = cm.read_lammpstrj('./coms/MIXTURE_N1-256_N2-256_MPR1-50_MPR2-50_Bend1-00.0_Bend2-30.0_L-044.03-com.lammpstrj',0.2)
adj_mat_mr,part_ind = cm.dyn_graph(frames_mr,part_ind,r_c)
plt.imshow(adj_mat_mr,cmap='binary')
plt.show()

