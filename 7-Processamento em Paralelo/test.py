from random import random
from multiprocessing import Pool
import timeit

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
    N = 10**5  # total de iteracoes 
    
    P = 1      # numero de processos
    p = Pool(P)
    print('tempo1', timeit.timeit(lambda: print(f'{sum(p.map(find_pi, [N//P]*P))/P:0.7f}'), number=10))
    p.close()
    p.join()
    print(f'{N} total de iteracoes com {P} processos')
    
    P = 5      # número de processos
    p = Pool(P)
    print('tempo2', timeit.timeit(lambda: print(f'{sum(p.map(find_pi, [N//P]*P))/P:0.7f}'), number=10))
    p.close()
    p.join()
    print(f'{N} total de iteracoes com {P} processos')
