import matplotlib.pyplot as plt
import numpy as np
import codemodule as cm

r_c = 4.0
part_ind=150
frames = cm.read_lammpstrj('./coms/MIXTURE_N1-256_N2-256_MPR1-50_MPR2-50_Bend1-00.0_Bend2-30.0_L-044.03-com.lammpstrj',0.2)
adj_mat = cm.dyn_graph_ser(frames,r_c)
times,res = cm.part_nodedeg(adj_mat,part_ind)
#plt.xscale('log')
plt.plot(times,res)
plt.show()

