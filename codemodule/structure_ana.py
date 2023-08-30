import networkx as nx
import numpy as np
from .numeric_pot_mc import d_matrix
from .radial_density import g_r_error
from .statistics import bin_ana_input,bin_ana


def make_graph(d_arr,r_c):
    #returns a graph from a given d_arr
    inc_arr = d_arr<r_c
    inc_arr = inc_arr.astype(int)
    #adm = (np.dot(inc_arr,inc_arr.T) > 0).astype(int)
    np.fill_diagonal(inc_arr,0)

    return nx.from_numpy_matrix(inc_arr)

def make_graph_2(d_arr,r_c):
    inc_arr = d_arr<r_c
    inc_arr = inc_arr.astype(int)
    np.fill_diagonal(inc_arr,0)
    print(inc_arr)
    rows,cols = np.where(inc_arr == 1)
    edges = zip(rows.tolist(),cols.tolist())
    gr = nx.Graph()
    for n in range(np.shape(inc_arr)[0]):
        gr.add_node(n)
    gr.add_edges_from(edges)
    return gr



def mu_ana_frame(G,mu_dict,types,N_total,type_count):
    cluster_makeup = np.zeros((2,N_total))
    for c in nx.connected_components(G):
        makeup = []
        for ind in c:
            makeup.append(types[ind])
        total = len(makeup)
        if makeup.count(type_count)< 1:
            cluster_makeup[0,len(c)-1] += 0.0
            cluster_makeup[1,len(c)-1]+= 1
        else:
            makeup = np.array(makeup)
            unique,counts = np.unique(makeup,return_counts=True)
            dic = dict(zip(unique,counts))
            cluster_makeup[0,len(c)-1] += (dic[type_count]/total)
            cluster_makeup[1,len(c)-1]+= 1

    for n in range(N_total):
        if cluster_makeup[1,n] > 0:
            ratio = cluster_makeup[0,n]/cluster_makeup[1,n]
            mu_dict[n+1].append(ratio)
    return mu_dict

def mu_ana(frames,types,L,r_c,type_count = 2,flag = "all",error_len = 0):

    N_total = np.shape(frames[0])[0]
    mu_dict = {}
    for n in range(N_total):
        mu_dict[n+1] = []

    for i in range(len(frames)):
        print(f'{i} \r')
        frame = frames[i]
        frame = frame.T
        d_arr = d_matrix(frame,L)
        d_arr = d_arr_splitter(d_arr,types,flag)
        G = make_graph_2(d_arr,r_c**2)
        mu_dict = mu_ana_frame(G,mu_dict,types,N_total,type_count)

    Nb = error_len
    mu_arr = np.zeros(N_total)
    error_arr = np.zeros(N_total)
    clust_sizes = np.arange(1,513)
    for n in range(N_total):
        if len(mu_dict[n+1])>0:
            mu_arr[n] = np.mean(mu_dict[n+1])
            error_arr[n] = np.sqrt(bin_ana(mu_dict[n+1],Nb))

    return clust_sizes,mu_arr,error_arr    
    
def struct_ana_frame(G,N_total):
    to_hist = [len(c) for c in nx.connected_components(G)]        
    bins = np.arange(1,N_total+2)
    hist, bin_edges = np.histogram(to_hist,bins)
    hist = hist*bin_edges[:-1]
    return hist/np.sum(hist), bin_edges


def struct_ana(frames,types,L,r_c,flag = "all",error_len = 0):
    N_total = np.shape(frames[0])[0]
    cluster_list = []
    for i in range(len(frames)):
        print(i)
        frame = frames[i]
        frame = frame.T
        d_arr = d_matrix(frame,L)
        d_arr = d_arr_splitter(d_arr,types,flag)
        G = make_graph_2(d_arr,r_c**2)
        cluster,bins = struct_ana_frame(G,N_total)
        cluster_list.append(cluster)
    error = g_r_error(cluster_list,error_len)
    cluster_res = np.mean(cluster_list,axis = 0)
    return bins[:-1],cluster_res,error

        



def d_arr_splitter(d_arr,types,flag = "all"):
    unique_types = np.unique(types)
    if flag == "all":
        return d_arr
    else:
        idx = np.where(types == int(flag[0]))

        return d_arr[idx[0][0]:idx[0][-1],idx[0][0]:idx[0][-1]] 
















