"""
    Dada una lista de números enteros, escribir una función que:
        a) Devuelva una lista con todos los que sean primos.
        b) Devuelva la sumatoria y el promedio de los valores.
        c) Devuelva una lista con el factorial de cada uno de esos números.
"""



def es_primo(num):

    condicion = True
    i = 2

    while i<num and condicion:
        if num%i == 0:
            condicion = False
        i+=1
    
    return condicion
    
def lista_num_primos(lista):

    num_primos = []

    for num in lista:
        condicion = es_primo(num)

        if condicion:
            num_primos.append(num)

    return num_primos


# print(lista_num_primos([1,3,5,10,12,2,4,6,7]))


def sumatoria_y_promedio(lista):

    sumador = 0

    for num in lista:
        sumador = sumador + num

    promedio = sumador / len(lista)

    return sumador, promedio


# print(sumatoria_y_promedio([1,5,10,12,20]))


def factorial_num(num):
    
    factorial = 1

    for i in range(2,num+1):
        factorial = factorial * i

    return factorial

def lista_num_factoriales(lista):

    num_factoriales = []

    for num in lista:
        factorial = factorial_num(num)
        num_factoriales.append(factorial)

    return num_factoriales



# print(lista_num_factoriales([1,2,3,4,0,8]))