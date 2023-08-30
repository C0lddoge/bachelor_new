import numpy as np
from .structure_ana import make_graph_2,d_arr_splitter
import codemodule as cm
import matplotlib.pyplot as plt
from networkx import betweenness_centrality as bc
import networkx as nx

def dyn_graph(frames,part_ind,r_c):
    N_time = len(frames)
    L = frames[0]['L']
    ty = frames[0]['types'][part_ind]
    N_tot = len(frames[0]['types'])
    print(f'the type of your particle is {ty}')
    adj_mat = np.zeros((N_tot,N_time))
    for i in range(N_time):
        frame = frames[i]['xyz']
        frame = frame.T
        d_arr = cm.d_matrix(frame,L)
        inc_arr = d_arr<r_c**2
        inc_arr = inc_arr.astype(int)
        np.fill_diagonal(inc_arr,0)
        inc_arr = inc_arr[part_ind,:]
        adj_mat[:,i] = inc_arr
    return adj_mat,part_ind


def node_degree_dist(adj_mat_series,types,type_flag,max_degree = 100):
    types = np.array(types)
    typ_mask = np.where(types==type_flag)
    N_f = np.shape(adj_mat_series)[2]
    adj_mat_series_split = np.zeros((len(types[typ_mask]),len(types[typ_mask]),N_f))
    for i in range(N_f):
        adj_mat_series_split[:,:,i] = adj_mat_series[typ_mask[0][0]:typ_mask[0][-1]+1,typ_mask[0][0]:typ_mask[0][-1]+1,i]
    adj_mat_series = adj_mat_series_split


    to_hist = []
    bins = np.arange(max_degree)
    for i in range(N_f):
        print(np.sum(adj_mat_series[:,:,i],axis = 1))
        to_hist.append(np.sum(adj_mat_series[:,:,i],axis = 1))
    to_hist = [item for sublist in to_hist for item in sublist]
    hist,bin_edges = np.histogram(to_hist,bins,density = True)
    return bin_edges[:-1],hist


def dyn_graph_ser(frames,r_c):
    N_time = len(frames)
    L = frames[0]['L']
    N_tot = len(frames[0]['types'])
      #N_part_ty = len(frames[0]['types'][frames[0]['types']==ty])
      #N_part2 = N_tot - N_part1
    adj_mat = np.zeros((N_tot,N_tot,N_time))
    for i in range(N_time):
        frame = frames[i]['xyz']
        frame = frame.T
        d_arr = cm.d_matrix(frame,L)                                               
        inc_arr = d_arr<r_c**2                                                     
        inc_arr = inc_arr.astype(int)                                              
        np.fill_diagonal(inc_arr,0)                                                                                              
        adj_mat[:,:,i] = inc_arr
    return adj_mat


def part_clustser(adj_mat,part_ind):
    N_time = np.shape(adj_mat)[2]
    times = np.arange(N_time)
    res = []
    con_inds = []
    for i in range(N_time):
        G = nx.from_numpy_matrix(adj_mat[:,:,i])
        comps = list(nx.node_connected_component(G,part_ind))
        con_inds.append(comps)
        res.append(len(comps))
    return times,res,con_inds

def part_nodedeg(adj_mat,part_ind):
    N_time = np.shape(adj_mat)[2]
    times = np.arange(N_time)
    res = []
    for i in range(N_time):
        G = nx.from_numpy_matrix(adj_mat[:,:,i])
        res.append(G.degree(part_ind))
    return times,res








def abs_diff(adj1,adj2):
    N = len(adj1)
    return 1/N * np.sum((np.sqrt((adj2-adj1)**2)))
def mul_diff(adj1,adj2):
    N = len(adj1)
    return 1/N * np.sum(adj2*adj1)

def dyn_corr(adj_mat,lags,weight_func):
    Nf = np.shape(adj_mat)[1]
    res = np.zeros((len(lags),2))
    for l,lag in enumerate(lags):
        samples = []
        for sample in range(0,Nf-lag):
            weight = weight_func(adj_mat[:,sample],adj_mat[:,sample+lag])
            samples.append(weight)
        res[l,0] = lag
        res[l,1] = np.mean(samples)


    return res
def dyn_onerow(adj_mat,ref_ind,lags):
    row = adj_mat[ref_ind,:]
    Nf = len(row)
    res = np.zeros((len(lags),2))
    for l,lag in enumerate(lags):
        samples = []
        for sample in range(0,Nf-lag):
            samples.append(row[sample]*row[sample+lag])
        res[l,0] = lag
        res[l,1] = np.mean(samples)
    return res

def clust_time(adj_mat,state,part_ind,max_lifetime):
    N = np.shape(adj_mat)[0]
    bins = np.arange(1,max_lifetime)
    samples = []
    for i in range(N):
        if i != part_ind:
            clust_series = adj_mat[i,:]
            samples.append(np.diff(np.where(np.concatenate(([clust_series[0]],clust_series[:-1] != clust_series[1:],[state])))[0])[::2])
    samples = [item for sublist in samples for item in sublist]
    hist,bin_edges = np.histogram(np.array(samples),bins,density = True)

    return hist,bin_edges[:-1]

def centrality(adj_mat_series,tau,start_frame):
    inc_arr = np.sum(adj_mat_series[:,:,start_frame:(start_frame+tau+1)],axis = 2)
    inc_arr[inc_arr>1] = 1
    rows,cols = np.where(inc_arr == 1)
    edges = zip(rows.tolist(),cols.tolist())
    gr = nx.Graph()
    for n in range(np.shape(inc_arr)[0]):
        gr.add_node(n)
    gr.add_edges_from(edges)
    res_dict = bc(gr)
    return res_dict.keys(),res_dict.values()

def mean_centrality(adj_mat_series,types,tau_N,type_flag,tau_max = 100, error_len = 0):
    types = np.array(types)
    typ_mask = np.where(types==type_flag)
    N_f = np.shape(adj_mat_series)[2]
    taus = sorted(list(set(np.logspace(0, np.log10(tau_max), num = tau_N, dtype = int))))
    adj_mat_series_split = np.zeros((len(types[typ_mask]),len(types[typ_mask]),N_f))
    for i in range(N_f):
        adj_mat_series_split[:,:,i] = adj_mat_series[typ_mask[0][0]:typ_mask[0][-1]+1,typ_mask[0][0]:typ_mask[0][-1]+1,i]
    adj_mat_series = adj_mat_series_split
    N = np.shape(adj_mat_series)[0]
    cen_scores = np.zeros((np.shape(adj_mat_series)[0],len(taus)))
    cen_scores[0,:] = taus
    for tau_ind,tau in enumerate(taus):
        print(tau)
        accumu = np.zeros((N,len(list(range(1,N_f-tau+1,50)))))
        for ind,start in enumerate(list(range(1,N_f-tau+1,50))):
            keys,scores = centrality(adj_mat_series,tau,start)
            scores = np.array(list(scores))
            accumu[:,ind] = scores
        cen_scores[:,tau_ind] = np.mean(accumu,axis = 1)
    avg_cen = np.mean(cen_scores[1:,:],axis = 0)
    if error_len == 0:
        Nb = cm.bin_ana_input(cen_scores[:,0])
    else:
        Nb = error_len
    err = []
    for i in range(len(taus)):
        err.append(np.sqrt(cm.bin_ana(cen_scores[:,i],Nb)))
    
    return cen_scores,taus,avg_cen,err

    


