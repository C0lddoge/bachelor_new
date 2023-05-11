import numpy as np
import codemodule as cm


frames,types = cm.read_last('frames.xyz')
frames,types = cm.read_xyz('frames.xyz',0,3027)
frame = frames[3000].T
print(np.shape(frames))
rho = 0.0025
#frames = frames.T
N = 512
L = (N/rho)**(1/3)
r_c = 2.0
d_arr = cm.d_matrix(frame,L)
part_inds = []
for i in range(np.shape(d_arr)[0]):
    for j in range(i+1,np.shape(d_arr)[0]):
        if d_arr[i,j]<=r_c:
            part_inds.append(i)
            part_inds.append(j)

print(part_inds)






