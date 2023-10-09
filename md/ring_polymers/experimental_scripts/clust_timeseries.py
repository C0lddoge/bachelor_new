import matplotlib.pyplot as plt
import numpy as np
import codemodule as cm

r_c = 4.5
part_ind=120
frames = cm.read_lammpstrj('../coms/MIXTURE_N1-256_N2-256_MPR1-50_MPR2-50_Bend1-00.0_Bend2-30.0_L-046.78-com.lammpstrj',0.2)
adj_mat = cm.dyn_graph_ser(frames,r_c)
times,res,comps = cm.part_clustser(adj_mat,part_ind)
diffs = np.diff(res)
plt.plot(times,res,linewidth = 1.0)
plt.xlabel('frames')
plt.ylabel('cluster size')
#axs[1].plot(times[:-1],diffs)
plt.show()

