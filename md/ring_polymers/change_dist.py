import matplotlib.pyplot as plt
import numpy as np
import codemodule as cm
from scipy.integrate import trapz 
r_c = 4.5
part_inds=[150,450]
binsies = np.arange(-20,20)
lags = [5]
frames = cm.read_lammpstrj('./coms/MIXTURE_N1-256_N2-256_MPR1-50_MPR2-50_Bend1-00.0_Bend2-30.0_L-046.78-com.lammpstrj',0.2)
adj_mat = cm.dyn_graph_ser(frames,r_c)
iterations = 4000
for k in part_inds:
    times,res,comps = cm.part_clustser(adj_mat,k)
    N = len(comps)
    respl = []
    res0 = []
    resmin = []
    for lag in lags:
        print(lag)
        to_hist = []
        #sampled_inds = []
        norm = 0
        for i in range(0,N-lag,lag):
            #ind = np.random.randint(0,N-lag)
            #if not np.any(np.array(sampled_inds) == ind):
            clust0 = comps[i]
            clust1 = comps[i+lag]
            #if len(clust0)>1:
            if len(clust0)>1 and len(clust1)>1:
                to_hist.append(len(clust1)-len(clust0))
            else:
                norm+=1
            #sampled_inds.append(ind)
        hist,bins_ = np.histogram(to_hist,bins=binsies)
        hist = hist/(N/lag-1-norm)
        print(trapz(hist,dx=1.0))
        #respl.append(trapz(hist[binsies[:-1]>0],dx = 1.0))
        #resmin.append(trapz(hist[binsies[:-1]<0],dx = 1.0))
        #res0.append(hist[binsies[:-1] == 0])
        plt.plot(binsies[:-1],hist, label = f'lag = {lag}')
        #res.append(np.mean(to_hist))
    #plt.plot(lags,respl,label = f'{k} grow')
    #plt.plot(lags,res0,label = f'{k} same')
    #plt.plot(lags,resmin,label=f'{k} shrink')
#plt.ylabel('occurences')
#plt.xticks(binsies)
#plt.plot(lags,0.57*,color = 'black')
plt.title('ring_ind = 450 (semiflexible)')
plt.legend() 
plt.show()

