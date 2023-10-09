import codemodule as cm
import numpy as np
import matplotlib.pyplot as plt

r_c = 4.5
part_ind = 350
max_lifetime = 100
frames_mr = cm.read_lammpstrj('./coms/MIXTURE_N1-256_N2-256_MPR1-50_MPR2-50_Bend1-00.0_Bend2-30.0_L-044.03-com.lammpstrj',0.2)
adj_mat_mr,part_ind = cm.dyn_graph(frames_mr,part_ind,r_c)
lags = np.arange(1,100)
refs = [10,110,200,270,300,450]
counter = 0
cutoffs = [0]
part_inds = [100,300]
for part_ind in part_inds:
    buf = []
    adj_mat_mr,part_ind = cm.dyn_graph(frames_mr,part_ind,r_c)
    for ref in range(260,510):
        res = cm.dyn_onerow(adj_mat_mr,ref,lags)
        if np.mean(res[:,1])>cutoffs[0]:
            buf.append(res[:,1])
#hist1,bins1 = cm.clust_time(adj_mat_cg,1,part_ind,max_lifetime)
#hist2,bins2 = cm.clust_time(adj_mat_mr,1,part_ind,max_lifetime)
    avg = np.mean(np.array(buf),axis = 0)
    plt.plot(lags,avg,label=part_ind)

plt.legend()
plt.show()


