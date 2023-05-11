import numba as nb

nb.jit(nopython = True)
def summation(n):
    res = 0
    for i in range(n):
        print(i)
        res +=1

    return res


def main():
    summation(10**6)

if __name__ =="__main__":
    main()
