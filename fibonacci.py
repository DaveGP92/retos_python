"""Escriba un programa que imprima los primeros 50 números de la sucesión de Fibonacci, comenzando desde el 0.

-La sucesión de Fibonacci se compone de una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores."""

def fibonacci():

    num_anterior = 0
    num_siguiente = 1

    for n in range(0,50):
        resultado = num_anterior + num_siguiente
        num_anterior = num_siguiente
        num_siguiente = resultado
        print(resultado)
        

fibonacci()
