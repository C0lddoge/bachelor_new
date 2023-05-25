import numpy as np
from .radial_density import g_r_error
from .statistics import *


def van_hoft(data,lag,bin_number,bin_range,ty = 'all',error_len = 0):
    L = float(data[0]['L'])
    types = np.array(data[0]['types'])
    if ty != 'all':
        for i in range(len(data)):
            new = np.delete(data[i]['xyz'],np.argwhere(types != int(ty)),axis = 0)
            data[i]['xyz'] = new
    Npart = np.shape(data[0]['xyz'])[0]
    Nframe = len(data)
    samples = []
    for  sample in range(0,Nframe-lag):
        print(f'{sample}/{Nframe-lag} \r')
        helper = []
        for part in range(Npart):
            helper.append(np.linalg.norm(data[sample]['xyz'][part][:]-data[sample+lag]['xyz'][part][:]))
        hist,edges = np.histogram(helper,bins=bin_number,range = (bin_range[0],bin_range[1]),density = True)
        samples.append(hist)
    r = (edges[:-1]+edges[1:])/2
    van_hove = np.mean(samples,axis = 0)
    error = g_r_error(samples,error_len)

    return r,van_hove,error


    


