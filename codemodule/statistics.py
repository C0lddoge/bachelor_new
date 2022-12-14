import numpy as np
import matplotlib.pyplot as plt

def read_txt(txt,delimiter):
    #reads txt file with assumptions that first column is steps and 2nd column is the data
    return np.loadtxt(txt, delimiter = delimiter)

def equilibrate(data,cutoff):
    #takes an input file equilibrates it and returns it as array and writes a new txt file. Assumes that the first column of the data are the steps and the second column is the data
    cutoff_index = int(cutoff*len(data[:,0]))
    print(len(data[cutoff_index:]))
    
    return data[cutoff_index:]
    
def equil_check(data,parts):
    splits = np.array_split(data[:,1],parts)
    check = []
    for i in splits:
        check.append(np.mean(i))
    
    return check
    #takes equil data assumes it s a 2d array and plots fragmented averages to make sure it s equilibrated correctly
    pass




def A(data):
    O = data[:,1]
    k = np.array(sorted(list(set(np.logspace(0,np.log(1000),num = 150, dtype = int, base = np.e)))))
    O_i = np.mean(O)
    O_i_2 = np.mean(O**2)
    
    O_k = np.zeros(len(k))
    for i in range(len(k)):
        Ns = int(len(O)-k[i])
        O_m = np.zeros(Ns)
        for j in range(Ns):
            O_m[j] = O[j]*O[j+k[i]]
        O_k[i] = np.mean(O_m)
    #for i in range(len(k)):
     #   O_k[i] = np.mean(O*np.roll(O,k[i]))
    A = (O_k-O_i*O_i)/(O_i_2-O_i*O_i)

    print(k)
    print(A)
    return k,A

def A_time(A):
    tau = 1/2 + np.cumsum(A)
    tau_final = -1
    for i in range(len(tau)):
        if i >= 6*tau[i]:
            tau_final = tau[i]
            break

    return tau,tau_final 

def bin_ana_input(data):
    # does bin ana to plot different boxlengths to let you select one
    N = len(data)
    Nb = np.arange(2,500)
    plot = []
    for i in Nb:
        plot.append(bin_ana(data,i))
    plt.plot(Nb,np.array(plot), '.', markersize = 3)
    plt.xlabel('Nb')
    plt.ylabel('sig2')
    plt.show()
    input_nb = int(input())
    return input_nb


def bin_ana(data,Nb):
    if len(np.shape(data)) == 2:  #careful this will fuck you if you put your data has 3 columns or something!!! make sure you want the 2nd column to be used
        O = data[:,1]
    else:
        O = data[:]
    N = len(O)
    k = int(N/Nb) #maybe need to properly do this
    print(f' k = {k}')
    print(f' NB = {Nb}')
    O_bn = []
    for i in range(1,Nb+1):
        O_temp = 0
        for j in range(k):
            O_temp += O[(i-1)*k+j]
            
        O_bn.append(1/k * O_temp)
    
    O_b = np.mean(O)
    O_bn = np.array(O_bn)
    x = (O_bn-O_b)**2
    sig2 = 1/(Nb-1) * np.sum(x)



    return sig2
#def bin_ana2(data,ks):
#    sig2_arr = []
#    Ns = len
#    for k in ks:
#        A = 0
#        Ns = 


def main():
    txt = '../data_lj/energy3.txt'
    delimiter = ';'
    data = read_txt(txt,delimiter)
    data = equilibrate(data,0.4)
    plt.plot(data[:,0],data[:,1])
    plt.show()
    k = [0,1,2,5,10,20,50,100,200,500]
    #k = np.arange(500)

    A_done = A(data,k)
    tau = A_time(A_done)
    plt.scatter(k,A_done)
    plt.plot(k,A_done)
    plt.plot(k,tau)
    plt.show()

if __name__ == '__main__':
    main()



