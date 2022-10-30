import numpy as np
import math
import numba as nb




#@nb.jit(nopython = True)
def closest_point(potential_arr, r_input):
    r = potential_arr[:,0]
    idx = np.searchsorted(r, r_input, side="left")
    if idx > 0 and (idx == len(r) or math.fabs(r_input - r[idx-1]) < math.fabs(r_input - r[idx])):
        return potential_arr[idx-1,1]
    else:
        return potential_arr[idx,1]    
    



#@nb.jit(nopython = True)
def pairwise_interpolate(potential_arr, r_input):
    r = potential_arr[:,0]
    idx = np.searchsorted(r, r_input, side="left")
    if idx > 0 and (idx == len(r) or math.fabs(r_input - r[idx-1]) < math.fabs(r_input - r[idx])):    
        closest_idx = idx-1       
    else:                                
        closest_idx = idx

    # find the right pair of points to interpolate between
    r_back = r[closest_idx-1]
    r_forward = r[closest_idx+1]
    r_closest = r[closest_idx]
    if np.abs(r_closest-r_forward) <= np.abs(r_closest-r_back):
        r_inter = [r_closest,r_forward]
        p_inter = potential_arr[closest_idx:closest_idx+2,1]
    else:
        r_inter = [r_back,r_closest]
        p_inter = potential_arr[closest_idx-1:closest_idx+1,1]

    return np.interp(r_input,r_inter,p_inter)
    

#@nb.jit(nopython = True)
def bin_potential(potential_arr, r_input):
    r = potential_arr[:,0]
    Veff = potential_arr[:,1]
    dr = np.mean(r[2:]-r[1:-1])
    bin_idx = int(r_input/dr)
    if bin_idx > len(Veff):
        return 0
    elif bin_idx == len(Veff):
        return Veff[-1]
    else:
        return Veff[bin_idx]

    
#@nb.jit(nopython = True)
def lj(r,eps,sig):
    x = (sig/r)**6
    return 4*eps*(x**2-x)






















