import numpy as np
from .radial_density import g_r_error
from .statistics import *


def self_F(data,q,N_lag,max_lag,ty,error_len = 0):
    types = np.array(data[0]['types'])
    if ty != all:
        for i in range(len(data)):
            new = np.delete(data[i]['xyz'],np.argwhere(types != int(ty)),axis = 0)
            data[i]['xyz'] = new
    Npart = np.shape(data[0]['xyz'])[0]
    L = float(data[0]['L'])

    twopi_L = 2*np.pi/L
    q2 = q*q
    Nframe = len(data)
    lags = sorted(list(set(np.logspace(0,np.log10(max_lag-1), num = N_lag,dtype = int))))

    N_lag = len(lags)
    res = []
    for qi in range(-q,q+1):
        for qj in range(-q,q+1):
            for qk in range(-q,q+1):
                Q = np.array([qi,qj,qk])
                n = np.dot(Q,Q)
                if n>0 and n==q2:
                    print(n)
                    F_t = np.zeros((N_lag,3))
                    for lagind,lag in enumerate(lags):
                        helper = []
                        for sample in range(0,Nframe-lag):
                            csum = 0
                            for part in range(Npart):
                                dr = -data[sample]['xyz'][part][:]+data[sample+lag]['xyz'][part][:]
                                qr = twopi_L*np.dot(Q,dr)
                                csum += np.cos(qr)
                            helper.append(csum/Npart)
                            
                        F_t[lagind,0] = lag
                        F_t[lagind,1] = np.mean(helper)
                        error = np.sqrt(bin_ana(helper,40))
                        F_t[lagind,2] = error
                    res.append(F_t)
    F_qt = np.vstack(np.mean(res,axis=0))
            
    return F_qt

                        





    pass
