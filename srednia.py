def srednia(lista):
    lenght = len(lista)
    suma = 0
    for i in lista:
        suma = suma + i

    srednia = suma / lenght
    return srednia

print(srednia([2, 3, 4]))