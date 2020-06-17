from itertools import permutations
from sys import maxsize
import numpy as np
from mpi4py import MPI

MASTER = 0

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

import os





def wczytaj(file):
    data = []
    plik = open(file)
    for line in plik:
        number_strings = line.split()
        numbers = [int(n) for n in number_strings]
        data.append(numbers)
    return data


def oblicz_dlugosc(vertex, graph,s):
    sciezka_min=maxsize




def TSP(graph, s):
    vertex = []
    liczba = 2
    wynik={}

    for i in range(l_miast):
        if i != s:
            vertex.append(i)

    print("vertex: {}".format(vertex))
    perm = list(permutations(vertex))
    print("Długość perm: {}".format(len(perm)))
    
    
    podzielona = np.array_split(perm, liczba)
    print("Podzielona: {} \n \n \n".format(podzielona))

    for i in range(liczba):
        print("                                                                   inna maszyna pc ")
        wynik[i]=(oblicz_dlugosc(podzielona[i], graph,s))
        print("Koszt: {}  Sciezka: {}".format(wynik[i][0], wynik[i][1]))
        
        
    for i in range(liczba):
        if rank == i:
            wynik[i] = (oblicz_dlugosc(podzielona[i], graph, s))
            print("Process {} Koszt: {}  Sciezka: {}".format(rank, wynik[i][0], wynik[i][1]))
            
            
if __name__ == "__main__":
    s = 0
    l_miast = len(open("1miasta.txt").readlines())
    print(l_miast)
    data = wczytaj("1miasta.txt")
    # print(data)

    TSP(data, s)

    wiad = "koszt {0} \n sciezka: {1}."
    # print(wiad.format(wynik[0], wynik[1]))
