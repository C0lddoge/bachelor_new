import matplotlib.pyplot as plt
import numpy as np
import codemodule as cm

r_c = 4.5
part_inds=[150,350]
frames = cm.read_lammpstrj('./coms/MIXTURE_N1-256_N2-256_MPR1-50_MPR2-50_Bend1-00.0_Bend2-30.0_L-046.78-com.lammpstrj',0.2)
adj_mat = cm.dyn_graph_ser(frames,r_c)

binsies = np.arange(0,5,0.1)
lags = np.arange(1,50)

for k in part_inds:
    times,res,comps = cm.part_clustser(adj_mat,k)

    res = []
    for lag in lags:
        to_hist = []
        for i in range(lag,len(comps)-lag,lag):
            clust0 = np.array(comps[i-lag])
            clust1 = np.array(comps[i])
            if len(clust0)>1 and len(clust1)>1:
                to_hist.append(len(clust1)/len(clust0))
    #hist,bins_ = np.histogram(to_hist,bins=binsies,density=True)
    #plt.plot(binsies[:-1],hist, label = f'lag = {lag}')
        res.append(np.mean(to_hist))

    plt.plot(lags,res,label = f'partind = {k}')

#plt.xlabel('clust size ratio')
#plt.ylabel('occurences')
#plt.xlim(0,2)
#plt.xticks(binsies)
plt.title('ring_ind = 450 (semiflexible)')
plt.legend() 
plt.show()

