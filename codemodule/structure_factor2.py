#!/usr/bin/env python3
import numpy as np
import codemodule as cm


def structure_factor(frames,types,qmax,stride = 1,error_len = 0):
##### the actual program
    NFR=len(frames)
    TYPE=types
    BOX_L=frames[0]['L']
    QMAX=qmax
    QMAX2=qmax*qmax
    TWO_PI_iL=2*np.pi/BOX_L
    NA=frames[0]['types'].count(TYPE)
    NPART=len(frames[0]['types'])
    print('\n {:} frames selected for S(q) wit qmax {:} for:'.format(NFR,QMAX))
    print(' type {:} with {:} particles'.format(TYPE,NA))

    # loop over the frames
    Sqs=np.zeros((NFR,QMAX2))
    for f,frame in enumerate(frames):
        qvec_counts=np.zeros(QMAX2,dtype=int)
        print(' running frame: {:d}/{:d}'.format(f+1,NFR),end='\r')
        #Sqs=np.zeros((NA,QMAX2))
        for qi in range(0,QMAX+1):
            for qj in range(-QMAX,QMAX+1):
                for qk in range(-QMAX,QMAX+1):
                    n=qi*qi+qj*qj+qk*qk
                    if (n>0) and (n<=QMAX2):
                        Csum,Ssum=0.0,0.0
                        for p in range(NA):
                            if frames[0]['types'][p]==TYPE:
                                qr=TWO_PI_iL*(qi*frame['xyz'][p,0]+qj*frame['xyz'][p,1]+qk*frame['xyz'][p,2])
                                Csum+=np.cos(qr)
                                Ssum+=np.sin(qr)
                        Sqs[f,n-1]+=Csum*Csum+Ssum*Ssum
                        qvec_counts[n-1]+=1

  # normalization


    
    QLEN=np.count_nonzero(qvec_counts)
    print(Sqs)
    print(qvec_counts)
    Sq_dump=np.zeros((QLEN,3))
    counter=0
    for q in range(QMAX2):
        if qvec_counts[q]!=0:
            Sq_dump[counter,0]=TWO_PI_iL*np.sqrt(q+1)
            Sq_dump[counter,1]=np.mean(Sqs[:,q]/(NA*qvec_counts[q]))
            Sq_dump[counter,2] = np.sqrt(cm.bin_ana(Sqs[:,q]/(NA*qvec_counts[q]),error_len))
            counter+=1
    return Sq_dump
