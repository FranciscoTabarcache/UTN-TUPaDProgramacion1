#1)  Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)

#2 Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene. 

n = input("Ingrese un número entero: ")
print(f"El número tiene {len(n.strip('-'))} dígitos.")

#3)Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores. 

a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))

if a > b:
    a, b = b, a  

suma = 0
for i in range(a + 1, b):
    suma += i

print(f"La suma de los enteros entre {a} y {b} es: {suma}")

#4)Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0.

suma = 0
while True:
    n = int(input("Ingrese un número (0 para terminar): "))
    if n == 0:
        break
    suma += n

print(f"Total acumulado: {suma}")

#5)Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random

objetivo = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el número (0-9): "))
    intentos += 1
    if intento == objetivo:
        print(f"¡Correcto! Lo lograste en {intentos} intentos.")
        break


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2):
    print(i)

#7)Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario.

n = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(n + 1):
    suma += i

print(f"La suma de los enteros de 0 a {n} es: {suma}")


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos

COUNT = 100  # cambia este valor para probar con menos entradas

pares = impares = positivos = negativos = 0

for i in range(1, COUNT + 1):
    n = int(input(f"{i}/{COUNT} Ingrese un entero: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores

COUNT = 100  # cambia este valor para probar
suma = 0

for i in range(1, COUNT + 1):
    n = int(input(f"{i}/{COUNT} Ingrese un entero: "))
    suma += n

media = suma / COUNT
print(f"Media: {media}")

# 10) ) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario

n = input("Ingrese un número entero: ").strip()

# Manejo de signo
signo = "-" if n.startswith("-") else ""
solo_digitos = n[1:] if signo else n

invertido = solo_digitos[::-1].lstrip("0") or "0"  # conserva "0" si corresponde
print(signo + invertido)

# Ejercicio 10
n = input("Ingrese un número entero: ").strip()

# Manejo de signo
signo = "-" if n.startswith("-") else ""
solo_digitos = n[1:] if signo else n

invertido = solo_digitos[::-1].lstrip("0") or "0"
print("Número invertido:", signo + invertido)
