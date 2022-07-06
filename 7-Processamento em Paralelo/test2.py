from random import random
from multiprocessing import Pool
import timeit
import sys

N = int(sys.argv[1])  # estes argumentos são passados da linha de comando
P = int(sys.argv[2])

def find_pi(n):
    """
    Função para estimar o valor de Pi
    """
    inside=0

    for i in range(0,n):
        x=random()
        y=random()
        if (x*x+y*y)**(0.5)<=1:  # se i cai dentro do círculo
            inside+=1

    pi=4*inside/n
    return pi

if __name__ == '__main__':
    
    with Pool(P) as p:
        print('tempo', timeit.timeit(lambda: print(f'{sum(p.map(find_pi, [N//P]*P))/P:0.5f}'), number=10))
    print(f'{N} total de iterações com {P} processos')
