# -*- coding: utf-8 -*-
import math

import numpy as np


class Integrator(object):

    """
    Klasa która implementuje całki metodą Newtona Cotesa z użyciem interpolacji
    N-tego stopnia :math:`n\in<2, 11>`.

    Dodatkowe wymaganie: Ilość operacji wykonanych w kodzie Pythona nie może zależeć 
    od num_evaluations. Mówiąc potocznie: nie ma "fora".

    UWAGA: Zachęcam do użycia współczynników NC z zajęć numer 2. Można
    je pobrać od innego zespołu!

    Podpowiedź: nasz algorytm działa tak że najpierw dzieli przedział na
    N podprzedziałów a każdy całkuje metodą NC. Wektoryzacja całkowania
    podprzedziału jest prosta:

    >>> coefficients = np.asanyarray(self.PARAMS[7]) # Wspolczynniki NC
    >>> x = ... # Tutaj wyznaczacie wsółrzędne
    >>> res = (x * coefficients) * norma

    A czy da się stworzyć tablicę X tak by dało się policzyć jednym wywołaniem
    całkę dla wszystkich podprzedziałów?

    Podpowiedź II: Może być to trudne do uzyskania jeśli będziecie używać macierzy
    jednowymiarowej. Należy użyć broadcastingu.

    Podpowiedź III: Proszę o kontakt to podpowiem więcej.

    """

    tab_coeff = {2:[1, 1],
                 3:[1,4,1],
                 4:[1,3,3,1],
                 5:[7,32,12,32,7],
                 6:[19,75,50,50,75,19],
                 7:[41,216,27,272,27,216,41],
                 8:[751,3577,1323,2989,2989,1323,3577,751],
                 9:[989,5888,-928,10496,-4540,10496,-928,5888,989],
                 10:[2857,15741,1080,19344,5778,5778,19344,1080,15741,2857],
                 11:[16067,106300,-48525,272400,-260550,427368,-260550,272400,-48525,106300,16067]}

    def __init__(self, level):
        """
        Funkcja ta inicjalizuje obiekt do działania dla danego stopnia metody NC
        Jeśli obiekt zostanie skonstruowany z parametrem 2 używa metody trapezów.
        :param level: Stopień metody NC
        """
        self.level = level

    @classmethod
    def get_level_parameters(cls, level):
        """
       
        :param int level: Liczba całkowita większa od jendości.
        :return: Zwraca listę współczynników dla poszczególnych puktów
                 w metodzie NC. Na przykład metoda NC stopnia 2 używa punktów
                 na początku i końcu przedziału i każdy ma współczynnik 1,
                 więc metoda ta zwraca [1, 1]. Dla NC 3 stopnia będzie to
                 [1, 3, 1] itp.
        :rtype: List of integers
        """
        if level < 2: raise ValueError
        
        return np.array(cls.tab_coeff.get(level)) 

    def integrate(self, func, func_range, num_evaluations):
        """

        :param callable func: Funkcja którą całkujemy
        :param tuple[int] func_range: Krotka zawierająca lewą i prawą granicę całkowania
        :param in tnum_evaluations:
        :return:
        """
        coeff = self.get_level_parameters(self.level)
        _range = math.ceil(num_evaluations/self.level)

        a, b = func_range
        step = (b-a) / ((self.level-1)*(_range))
        tab = np.arange(a, b, step)

        tmp = np.zeros((_range, self.level))
        tmp[:,:-1]  = tab.reshape((_range, self.level-1))
        tmp[:-1,-1] = tmp[1:,0]
        tmp[-1,-1]  = b
            
        h = (b-a)/_range
        tmp = func(tmp)*coeff
        return sum(sum(tmp))/sum(coeff)*h

if __name__ == "__main__":
≡jedi=0, ≡                   (*level*) ≡jedi≡
    ii = Integrator(level=7)
    print(ii.integrate(np.sin, (0, np.pi), 30))
