# -*- coding: utf-8 -*-

import numpy as np

from itertools import chain, permutations, product


def calculate_neighbours(board):

    """

    Funkcja zwraca tablicę która w polu N[R, C] zwraca ilość sąsiadów którą 
    ma komórka Board[R, C]. Za sąsiada uznajemy obszazoną komórkę po bokach lub
    na ukos od danej komórki, komórka nie jest swoim sąsiatem, zatem maksymalna
    ilość sąsiadów danej komórki wynosi 8.

    Funkcja ta powinna być zwektoryzowana, tj ilość operacji w bytekodzie
    Pythona nie powinna zależeć od rozmiaru macierzy.

    :param np.ndarray board: Dwuwymiarowa tablica zmiennych logicznych która
    obrazuje aktualny stan game of life. Jeśli w danym polu jest True (lub 1)
    oznacza to że dana komórka jest obsadzona


    Podpowiedź: Czy jest możliwe obliczenie ilości np. lewych sąsiadów
    których ma każda z komórek w macierzy, następnie liczymy ilość sąsiadów
    prawych itp.

    Podpowiedź II: Proszę uważać na komórki na bokach i rogach planszy.
    """
    N, M = board.shape

    tmp = np.zeros((N, M))
    tmp[:, :-1] += board[:, 1:]
    tmp[:, 1:] += board[:, :-1]
    tmp[:-1, :] += board[1:, :]
    tmp[1:, :] += board[:-1, :]

    tmp[:-1, :-1] += board[1:, 1:]
    tmp[1:, 1:] += board[:-1, :-1]
    tmp[1:, :-1] += board[:-1, 1:]
    tmp[:-1, 1:] += board[1:, :-1]

    return tmp


def iterate(board):

    """

    Funkcja pobiera planszę game of life i zwraca jej następną iterację.

    Zasady Game of life są takie:

    1. Komórka może być albo żywa albo martwa.
    2. Jeśli komórka jest martwa i ma trzech sąsiadóœ to ożywa.
    3. Jeśli komórka jest żywa i ma mniej niż dwóch sąsiadów to umiera,
       jeśli ma więcej niż trzech sąsiadóœ również umiera. W przeciwnym wypadku
       (dwóch lub trzech sąsiadów) to żyje dalej.

    :param np.ndarray board: Dwuwymiarowa tablica zmiennych logicznych która
    obrazuje aktualny stan game of life. Jeśli w danym polu jest True (lub 1)
    oznacza to że dana komórka jest obsadzona

    """
    tmp = np.array(board.shape)

    b = np.array(board, dtype=int)
    b = calculate_neighbours(b)

    tmp = np.logical_and(board == False, b==3)
    tmp = np.logical_or(tmp, np.logical_and(board  == True, np.logical_and(b>=2, b<=3)))

    return tmp