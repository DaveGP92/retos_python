#Escribe un programa que mueste por consola los números del 1 al 100 (ambos incluídos y con un salto de línea entre cada impresión), sustituyendo los siguientes:

#Múltiplos de 3 por la palabra "fizz"
#Múltiplos de 5 por la palabra "fuzz"
#Múltiplos de 3 y 5 a la vez por la palabra "fizzbuzz"

#Primera forma:

def fizz_fuzz():
    for n in range(1, 101):
        if n % 3 == 0 and n % 5:
            print(f"FizzBuzz")
        
        elif n % 3 == 0:
            print("Fizz")
        
        elif n % 5 == 0:
            print("Buzz")
        
        else:
            print(n)
            

fizz_fuzz()

#Segunda forma:

fizz_fuzz = ["FizzBuzz" if num % 3 == 0 and num % 5 == 0 else "Fizz" if num % 3 == 0 else "Buzz" if num % 5 == 0 else num for num in range (1, 101)]

for elemento in fizz_fuzz:
    print(elemento)