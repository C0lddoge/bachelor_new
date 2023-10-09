import numpy as np
import matplotlib.pyplot as plt
import codemodule as cm

frames = cm.read_lammpstrj('./coms/MIXTURE_N1-256_N2-256_MPR1-50_MPR2-50_Bend1-00.0_Bend2-30.0_L-044.03-com.lammpstrj',0.2)
adj_mat = cm.dyn_graph_ser(frames,4.5)
#times = np.arange(1,100)
res_flex = []
res_semi = []
times = [3,50]
for t in times:
    ring,score = cm.centrality(adj_mat,t,50)
    score = list(score)
    res_flex.append(np.mean(score[:256]))
    res_semi.append(np.mean(score[256:]))
    plt.plot(ring,score,label=f'{t} compound time')
    #plt.plot(ring,score,label = t)
#plt.plot(times,res_flex,linestyle = 'dashed',label = 'flexible' )
#plt.plot(times,res_semi,label = 'semiflexible')
plt.xlabel('ring index')
plt.ylabel('mean centrality score')
#plt.savefig('./dyn_graph_res/cen_distL44.03.pdf')
plt.legend()
plt.show()
