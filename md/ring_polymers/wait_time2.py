import matplotlib.pyplot as plt
import numpy as np
import codemodule as cm

r_c = 4.5


frames = cm.read_lammpstrj('./coms/MIXTURE_N1-256_N2-256_MPR1-50_MPR2-50_Bend1-00.0_Bend2-30.0_L-046.78-com.lammpstrj',0.2)
adj_mat = cm.dyn_graph_ser(frames,r_c)
inds = [np.arange(256),np.arange(256,512)]
#inds = [np.arange(1,101),np.arange(350,450)]
binsies = np.arange(0,1,0.01)
lags = np.arange(1,50)
labels = ['flexible','semiflexible']
for i in range(2):
    res = np.zeros((len(inds[i]),len(lags)))
    print(res)
    for j in range(len(inds[i])):
        print(inds[i][j])
        part_ind=inds[i][j]
        times,dat,comps = cm.part_clustser(adj_mat,part_ind)
        for lag in lags:
            to_hist = []
            for k in range(lag,len(comps)-lag,lag):
                clust0 = np.array(comps[k-lag])
                clust1 = np.array(comps[k])
                if len(clust0)>1 and len(clust1)>1:
                    to_hist.append((len(np.intersect1d(clust0,clust1))-1)/len(clust0))
            hist,bins_ = np.histogram(to_hist,bins=binsies,density=True)
    #plt.plot(binsies[:-1],hist, label = f'lag = {lag}')
            res[j,lag-1] = hist[binsies[:-1]==0.5]*0.01


    plt.plot(lags,np.mean(res,axis = 0),label = labels[i])
plt.xlabel('lag')
plt.ylabel('P_50(lag)')
plt.legend()
#plt.xticks(binsies)
#plt.legend()
plt.savefig('p50.pdf')
plt.show()

