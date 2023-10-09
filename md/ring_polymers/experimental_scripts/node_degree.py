import codemodule as cm
import numpy as np
import matplotlib.pyplot as plt


r_c = 4.0
partind = 350
frames = cm.read_lammpstrj('./coms/MIXTURE_N1-256_N2-256_MPR1-50_MPR2-50_Bend1-00.0_Bend2-30.0_L-046.78-com.lammpstrj',0.8)
types = frames[0]['types']
adj_mat = cm.dyn_graph_ser(frames,r_c)
bins,node_dist = cm.node_degree_dist(adj_mat,types,2,10)
bins,node_dist_flex = cm.node_degree_dist(adj_mat,types,1,10)
plt.plot(bins,node_dist,label = 'semiflexible')
plt.plot(bins,node_dist_flex,label = 'flexible')
plt.legend()
plt.show()

