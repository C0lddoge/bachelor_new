import numpy as np
import numba as nb
from .numeric_pot_mc import d_matrix
from .radial_density import g_r_error



def structure_fac(frames,types,pair0,pair1,rho):
    pair = (pair0,pair1)
    N_types = np.unique(types, return_counts = True)[1]
    N_total = len(types)
    L = (N_total/rho)**(1/3)

    q_base = 2*np.pi/L
    qs = [q_base]
    prefac = [1,np.sqrt(2),np.sqrt(3)]
    i = 1
    while qs[-1] <= 8*q_base:
        q_i = (i//3 + 1)*prefac[i%3] * q_base
        qs.append(q_i)
        i = i+1
    qs = np.sort(qs)
    
    d_arr_idx = []
    for i in range(N_total):
        for j in range(N_total):
            if (types[i],types[j]) == pair and i!=j:
                d_arr_idx.append((i,j))

    S_frames = []
    for i in range(len(frames)):
        print(f'{i}/{len(frames)}')
        d_arr = d_matrix(frames[i].T,L)
        rs = []
        for j in d_arr_idx:
                rs.append(d_arr[j])
        

        S = []
        for q in qs:
            summation = 0
            for r in rs:
                summation = summation + np.sin(q*r)/(q*r)
            S.append(summation)

        S = np.array(S)
        S = 1/(np.sqrt(np.prod(N_types)))  * S
        S_frames.append(S)
    error = g_r_error(S_frames)
    S = np.mean(S_frames, axis = 0)

    return qs, S 


@nb.jit(nopython = True)            
def term(q,r):
    return np.sin(q*r)/(q*r)


def fac_avg(frames,types,rho,q_max,typeA):
    N_total = len(types)
    N_A = np.unique(types,return_counts = True)[1][typeA]
    L = (N_total/rho)**(1/3)
    invL = 2*np.pi/L
    q_max2 = q_max * q_max
    qs = invL * np.sqrt(np.arange(0,q_max2,dtype = float)+1)


    Sqs_avg = []
    counter = 0
    for frame in frames:
        counter += 1
        print(counter)
        Sqs = fac(frame,types,invL,q_max,q_max2,N_total,N_A,typeA)
        Sqs_avg.append(Sqs)
    Sq = np.mean(Sqs_avg,axis = 0)
    #error = g_r_error(Sqs_avg)
    error = 0
    qs = qs[qs>0]
    qs = qs[:len(Sq)]
    return Sq,qs,error


def fac(frame,types,invL,q_max,q_max2,N_total,N_A,typeA): 
    Sqs = np.zeros(q_max2)
    counts = np.zeros((q_max2),dtype = int)
    for qi in range(0,q_max + 1):
        for qj in range(-q_max,q_max+1):
            for qk in range(-q_max,q_max+1):
                n = qi**2 + qj**2 + qk**2
                if (n>0) and (n<=q_max2):
                    Csum,Ssum = 0.0,0.0
                    for p in range(N_total):
                        if types[p] == typeA:
                            qr = invL * (qi*frame[p,0] + qj * frame[p,1] + qk*frame[p,2])
                            Csum += np.cos(qr)
                            Ssum += np.sin(qr)
                    Sqs[n-1] += Csum**2 + Ssum**2
                    counts[n-1] += 1
    Sqs /= (counts*N_A)
    Sqs = Sqs[~np.isnan(Sqs)]
    return Sqs

        








