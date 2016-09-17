from random import randint
from itertools import accumulate

def min_loc(A):
    low=0
    hi=len(A)
    while low<=hi:
        mid=(low+hi)//2
        if mid-1<=low or mid+1>=hi:
            return mid #print (A[mid])
        elif A[mid-1]>=A[mid] and A[mid]<=A[mid+1]:
            return mid #print(A[mid])
        elif A[mid-1]>=A[mid] and A[mid]>A[mid+1]:
            low=mid+1
        else:
            hi=mid-1

    
#gracias al compañero que lo  hizo
def randomwalk(N):
    W = [ randint(-1, 1) for _ in range(N)]
    A = list(accumulate(W))
    return A
def arr_ascendente(arreglo, tamano) :
    for i in range(0, tamano):
        arreglo.append(i)

def arr_descendiente(arreglo, tamano) :
    for i in range(0, tamano):
        arreglo.append(tamano - i)


if __name__=='__main__':
    from timeit import Timer
    from sys import stdin
    A=[]
    #arr_descendiente(A,100000)
    arr_ascendente(A,8000000)
    samples=1
    t=Timer("min_loc(A)", "from __main__ import min_loc, A")
    took = t.timeit(samples)/samples
    print("min_loc for {} integers took {:.7f} secs".format(len(A), took))
    
    
