from itertools import permutations
from sys import maxsize
import numpy as np
from mpi4py import MPI
from salesman.mpi.dawajtarule import oblicz_dlugosc

# odpalanie: mpirun -np 3 python dawajta.py



comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
dest = 0  #na tp wysylamy oblioczone dane
druk =1 # czy chcemy drukowac piedoly


def wczytaj(file):
    data = []
    plik = open(file)
    for line in plik:
        number_strings = line.split()
        numbers = [int(n) for n in number_strings]
        data.append(numbers)
    return data


s = 0  #wierzchoek starowy
vertex = []
liczba = size - 1
wynikk = {}
l_miast = len(open("1miasta.txt").readlines())
if druk: print(l_miast)
data = wczytaj("1miasta.txt")
if druk: print(data)

for i in range(l_miast):
    if i != s:
        vertex.append(i)

if druk: print("vertex: {}".format(vertex))
perm = list(permutations(vertex))
if druk: print("Dlugosc perm: {}".format(len(perm)))

podzielona = np.array_split(perm, liczba)
if druk: print("Podzielona: {} \n \n \n".format(podzielona))

                                                              
wynik=(oblicz_dlugosc(podzielona[rank-1], data,s))
#if druk: print("Koszt: {}  Sciezka: {}".format(wynik[0], wynik[1]))

if druk: print(" BYL {} node idzie kolejny NOOOOOOOOOOOOOOOOOOOOOOOOOODE".format(rank))

if rank == 0:

    for source in range(1,size):
        wynikk[source]= comm.recv(source=source)
        print("PE <- {} Koszt: {}  Sciezka: {}".format(rank, wynikk[source][0], wynikk[source][1]))
        #wynik[1][2]   1-z ktorego noda przyszlo rozwiazanie    2[0-koszt najktorszej sciezki 1- ta sciezka]

else:
    
    comm.send(wynik,dest)
    print("PE >> {} Koszt: {}  Sciezka: {}".format(rank, wynik[0], wynik[1]))



if (rank==0):
    print("elo")
    #tutaj zrobic wybranie z tablicy wynikk[] najmniejszej sciezki i jakos to zwrocic

MPI.Finalize()


