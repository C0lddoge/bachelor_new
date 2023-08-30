import numpy as np
from.graph_dynamics import dyn_graph_ser,part_clustser
from .read_traj import read_lammpstrj
from .radial_density import g_r_error


def same_ratio_part(adj_mat,lag,part_ind,low_s,high_s,binsies):
    times,res,comps = part_clustser(adj_mat,part_ind)
    N = len(comps)
    res = []
    to_hist = []
    norm = 0
    for i in range(lag,len(comps)):
        clust0 = np.array(comps[i-lag])
        clust1 = np.array(comps[i])

        if len(clust0)>=low_s and len(clust1)<=high_s:
            to_hist.append((len(np.intersect1d(clust0,clust1)))/(len(clust0)))
    hist,bins_ = np.histogram(to_hist,bins=binsies)
    return hist

def same_ratio(filename,r_c,cutoff,lag,low_s,high_s,type_flag,bin_width = 0.05,error_len = 0):
    frames = read_lammpstrj(filename,cutoff)
    Npart = np.shape(frames[0]['xyz'])[0]
    adj_mat = dyn_graph_ser(frames,r_c)
    if type_flag == 'all':
        part_inds = list(np.arange(Npart))
    else:
        types = np.array(frames[0]['types'])
        type_flag = int(type_flag)
        part_inds = list(np.asarray(types==type_flag).nonzero()[0])
    binsies = np.arange(0,1.1,bin_width)
    res = []
    for part_ind in part_inds:
        print(part_ind)
        res.append(same_ratio_part(adj_mat,lag,part_ind,low_s,high_s,binsies))
    error = g_r_error(res,error_len)
    res = np.mean(res,axis = 0)
    return binsies[:-1],res,error


