import networkx as nx
import numpy as np
from .numeric_pot_mc import d_matrix
from .radial_density import g_r_error


def make_graph(d_arr,r_c):
    #returns a graph from a given d_arr
    inc_arr = d_arr<r_c
    inc_arr = inc_arr.astype(int)
    #adm = (np.dot(inc_arr,inc_arr.T) > 0).astype(int)
    np.fill_diagonal(inc_arr,0)

    return nx.from_numpy_matrix(inc_arr)

def make_graph_2(d_arr,r_c):
    inc_arr = d_arr<r_c
    rows,cols = np.where(inc_arr == 1)
    edges = zip(rows.tolist(),cols.tolist())
    gr = nx.Graph()
    for n in range(np.shape(inc_arr)[0]):
        gr.add_node(n)
    gr.add_edges_from(edges)
    return gr


def struct_ana_frame(frame,types,L,r_c,flag = "all"):
    frame = frame.T
    d_arr = d_matrix(frame,L)
    d_arr = d_arr_splitter(d_arr,types,flag)
    G = make_graph_2(d_arr,r_c)
    to_hist = [len(c) for c in nx.connected_components(G)]
    bins = np.arange(1,5)
    hist, bin_edges = np.histogram(to_hist,bins)
    for i in range(len(hist)):
        hist[i] = (i+1)*hist[i]
    total = np.sum(hist*np.diff(bin_edges))
    return hist/total, bin_edges


def struct_ana(frames,types,rho,r_c,flag = "all"):
    N_total = np.shape(frames[0])[0]
    L = (N_total/rho)**(1/3)
    print(L)
    cluster_list = []
    for i in range(len(frames)):
        print(i)
        cluster,bins = struct_ana_frame(frames[i],types,L,r_c,flag)
        cluster_list.append(cluster)
    error = g_r_error(cluster_list)
    cluster_res = np.mean(cluster_list,axis = 0)
    
    return bins[:-1],cluster_res,error

        



def d_arr_splitter(d_arr,types,flag = "all"):
    unique_types = np.unique(types)
    if flag == "all":
        return d_arr
    else:
        idx = np.where(types == int(flag[0]))

        return d_arr[idx[0][0]:idx[0][-1],idx[0][0]:idx[0][-1]] 
















