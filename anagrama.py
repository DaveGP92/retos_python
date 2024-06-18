"""¿Es un anagrama?
Escribe un función que reciba dos argumentos "strings" y retorne True o False según sean o no anagramas.

-Un anagrama consiste en formar una palabra reordenando todas las letras de la palabra inicial.

-No hace falta comprobar que ambas palabras existan.

-Dos palabras exactamente iguales no son anagramas."""

palabra_1 = input("Escriba la primer palabra:\n").lower()

palabra_2= input("Escriba la segunda palabra:\n").lower()


#Forma 1

def es_anagrama(palabra_1, palabra_2):

    if palabra_1 == palabra_2:
        return False
    
    elif sorted(palabra_1) == sorted(palabra_2):
        return True

    else:
        return False

respuesta = es_anagrama(palabra_1, palabra_2)

print(f"¿Las palabras {palabra_1} y {palabra_2} son anagramas? = {respuesta}")



#Forma 2 List Comprehension

palabra_anagram = [False if palabra_1 == palabra_2 else True if sorted(palabra_1) == sorted(palabra_2) else False]

print(f"¿Las palabras {palabra_1} y {palabra_2} son anagramas? = {palabra_anagram}")