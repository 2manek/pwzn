# -*- coding: utf-8 -*-
import csv


def merge(path1, path2, out_file):
    """
    Funkcja pobiera nazwy dwóch plików z n-gramami (takie jak w poprzedmim
    zadaniu) i łączy zawartość tych plików i zapisuje do pliku w ścieżce ``out``.

    Pliki z n-gramami są posortowane względem zawartości n-grama.

    :param str path1: Ścieżka do pierwszego pliku
    :param str path2: Ścieżka do drugiego pliku
    :param str out_file:  Ścieżka wynikowa

    Testowanie tej funkcji na pełnych danych może być mało wygodne, możecie
    stworzyć inną funkcję która działa na dwóch listach/generatorach i testować
    ją.

    Naiwna implementacja polegałaby na stworzeniu dwóch słowników które
    zawierają mapowanie ngram -> ilość wystąpień i połączeniu ich.

    Lepsza implementacja ładuje jeden z plików do pamięci RAM (jako słownik
    bądź listę) a po drugim iteruje.

    Najlepsza implementacja nie wymaga ma złożoność pamięciową ``O(1)``.
    Podpowiedź: merge sort. Nie jest to trywialne zadanie, ale jest do zrobienia.
    """
    from collections import defaultdict
    import operator

    counter = defaultdict(lambda : 0)

    # data = list()

    with open(path1, 'r', encoding='utf-8') as file, open(path2, 'r', encoding='utf-8') as file2:
        r = csv.reader(file, dialect=csv.unix_dialect)
        for line in r:
            # data.append( (line[0], int(line[1]) ) )
            counter[line[0]]+=int(line[1])

        r = csv.reader(file2, dialect=csv.unix_dialect)
        for line in r:
            counter[line[0]]+=int(line[1])
            # data.append( (line[0], int(line[1]) ))
    out = []
    for key, value in counter.items():
        out.append( (key, value) )
    out = sorted(out, key=operator.itemgetter(0) )
    # print(out[0])
    # print(out[-1])

    with open(out_file, 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='\'')
        for o in out:
            spamwriter.writerow(o)

    # with open(out_file, 'w', encoding='utf-8') as file:
    #     for ngram, frq in data:
    #         file.write("'"+ngram+"','"+frq+"'\n")

if __name__ == '__main__':

    merge(
        '/home/kinkuro/Studia/Doktorat/Python/zaj3/enwiki-20140903-pages-articles_part_2.xmlascii1000.csv',
        '/home/kinkuro/Studia/Doktorat/Python/zaj3/enwiki-20140903-pages-articles_part_2.xmlascii1000.csv',
        '/tmp/mergeout.csv')