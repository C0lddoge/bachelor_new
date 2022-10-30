import numpy as np
import os


def read_config(path = ''):
    filename = os.path.join(path,'config.ko')
    config = np.loadtxt(filename,dtype = str)
    if np.shape(config)[0] > 2:
        inter_type = config[:,0]
        pot_files = config[:,1]
    else:
        inter_type = [config[0]]
        pot_files = [config[1]]


    pots = []
    pot_error = []
    for potname in pot_files:
        pots.append(np.loadtxt(os.path.join(path,potname))[:,:2])
        pot_error.append(np.loadtxt(os.path.join(path,potname))[:,2])
    inter_pair = []
    for i in inter_type:
        inter_pair.append((int(i[0]),int(i[1])))



    

    return dict(zip(inter_pair,pots)), dict(zip(inter_pair,pot_error))














