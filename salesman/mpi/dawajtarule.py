from itertools import permutations
from sys import maxsize
import numpy as np


def oblicz_dlugosc(vertex, graph,s):
    sciezka_min=maxsize
    druk = 0

    for i in vertex:
        koszt_sciezki = 0
        k = s
        if druk: print(i)
        if druk: print("  i im vertex   ")
        for j in i:
            if druk: print(graph[k][j])
            koszt_sciezki += graph[k][j]
            k=j
        if druk: print(graph[k][s])
        koszt_sciezki+=graph[k][s]

        if druk: print("koszt: {}".format(koszt_sciezki))
        if druk: print("   ")

        if (koszt_sciezki < sciezka_min):
            sciezka_min = koszt_sciezki
            droga = i
    return sciezka_min, droga