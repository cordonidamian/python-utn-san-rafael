# -*- coding: utf-8 -*-
"""
Editor de Spyder
"""

# Importo la librería math para calcular la raíz cuadrada y para truncar el resultado en el ejercicio 1
#sqrt() - trunc()
from math import sqrt 
# Importo la librería trunc para truncar un float
from math import trunc
# Importo la librería fraction para utilizar fracciones
from fractions import Fraction
#Fraction()






#EJERCICIO 1
"""
Calcule la raiz cuadrada del n ́umero 458. Muestre el resultado completo con decimales, y
luego mu ́estrelo truncado.
"""

num = 458

print("Resultado con decimales (en caso de que corresponda):", sqrt(num))

print("Resultado sin decimales casteando con int:", int(sqrt(num)))

# https://kite.com/python/answers/how-to-truncate-a-float-in-python
trunca_num = f"{sqrt(num):.0f}"

print("Resultado sin decimales con format:", trunca_num)

print("Resultado sin decimales con trunc", trunc(sqrt(num)))





#EJERCICIO 2
"""
Realizar el programita que calcule cada una de las siguientes expresiones: (*La sumatoria
y la productoria de los puntos e, f desarrollelas primero en papel para calcular dicha
expresion numerica)

"""

print("Ejercicio a: ",(3+8) * (2-26))
print("Ejercicio b: ",34**3)
print("Ejercicio c: ",2*(10-2) / -1*(8-12))
print("Ejercicio d: ",sqrt(9))
print("Ejercicio e: ",1+1+2+3+4+5+6+7+8+9+10)
print("Ejercicio f: ",(2+1)*(3+1)*(4+1)*(5+1)*(6+1)*(7+1)*(8+1))
print("Ejercicio g: ",Fraction(1,2) + Fraction(2,3) + Fraction(3,) + Fraction(4,5))
print("Ejercicio h: ",-8 + sqrt((8**2-(4*3*2))) / (2*3))




#EJERCICIO 3
"""
Realizar un programa que calcule para una temperatura ingresada por el usuario en
Fahrenheit, su temperatura equivalente, en grados Celsius. 
"""


grados = int(input("Por favor ingrese la temperatura en grados Fahrenheit para ser calculada en grados Celsius: "))

calculo = float((grados - 32) * Fraction(5,9))

print("La temperatura es de", calculo, "grados Celsius")





#EJERCICIO 4
"""
Escribir un programita que permita convertir una medida en pulgadas, a una medida en
metros. *Una pulgada es 0.0254 mtrs
"""

medida = int(input("Por favor ingrese la medida en pulgadas la cual será convertida en metros: "))

a_metros = medida * 0.0254

print("El valor ingresado convertido a metros es de:", a_metros, "metros")




#EJERCICIO 5
"""
Realizar un programita que pida un nombre al usuario e imprima en pantalla un saludo
de bienvenida junto al nombre ingresado. (”Hola Pepe!”por ejemplo, si el usuario ingres ́o
Pepe)
"""

nombre = input("Por favor ingrese su nombre: ")

print("Bienvenido", nombre, "al curso de Introducción a Python!")





#EJERCICIO 6
"""
Realizar un programita que pida un n ́umero y determine si es par o impar.
"""

nume = int(input("Ingrese un número y determinaremos si es par o impar: "))

if nume % 2 == 0:
    print(nume, " es un número par!")
else:
    print(nume, " es un número impar!")
    



#EJERCICIO 7
"""
Realizar un programita que pida un n ́umero, controlando que haya ingresado un n ́umero
entre 1 y 10, determinar si es menor a 5 o mayor o igual a 5.
"""

numeingre = int(input("Ingrese un número entre 1 y 10, determinaremos si es menor, mayor o igual a 5: "))

if numeingre >= 1 and numeingre <= 10:
    if numeingre < 5:
        print("El número ingresado es menor a 5")
        
    elif numeingre > 5:
        print("El número ingresado es mayor a 5")

    else: print("El número ingresado es 5")
    
else: print("El número ingresado no cumple con los requisitos")




#EJERCICIO 8
"""
Realizar un programita que pida un numero y devuelva +1 si  ́este es positivo y -1 si  ́este
es negativo.
"""

posinega = int(input("Ingrese un número distinto de cero (positivo ó negativo), devolveremos +1 si es positivo o -1 si es negativo: "))

if posinega != 0:
    if posinega < 0:
        print("-1")
        
    else:
        print("+1")

else: print("El número ingresado no cumple con los requisitos")
               
             





#EJERCICIO 9
"""
Realizar un programita que pida un n ́umero y devuelva +1 si  ́este es positivo y 0 si  ́este
es negativo.
"""

posinega = int(input("Ingrese un número distinto de cero (positivo ó negativo), devolveremos +1 si es positivo o 0 si es negativo: "))

if posinega != 0:
    if posinega < 0:
        print("0")
        
    else:
        print("+1")

else: print("El número ingresado no cumple con los requisitos")



#EJERCICIO 10
"""
Realizar un programita que pida dos n ́umeros enteros y devuelva 1 si ambos n ́umeros son
iguales, y 0 sino.
"""

print("Le pediremos que ingrese 2 números enteros y comprobaremos si estos son iguales (1) o diferentes (0).")
num_uno = int(input("Ingrese el primer número:  "))
num_dos = int(input("Ingrese el primer número:  "))

if num_uno == num_dos:
    print("1 (Los números ingresados son iguales)")
else: 
    print("0 (Los números ingresados son diferentes)")




#EJERCICIO 11
"""
Realizar un programita que pida dos n ́umeros enteros y devuelva true si ambos n ́umeros
son iguales, y false sino.
"""


print("Le pediremos que ingrese 2 números enteros y comprobaremos si estos son iguales (true) o no (false).")
num_uno = int(input("Ingrese el primer número:  "))
num_dos = int(input("Ingrese el primer número:  "))


print(num_uno == num_dos)






#EJERCICIO 12
"""
Realizar un programita que pida dos palabras al usuario y determine si son iguales o no,
devolviendo true (verdadero) si lo son.
"""

print("Le pediremos ingresar 2 palabras y comprobaremos si son iguales (true) o no (false) ")

texto_1 = input("Ingrese la primer palabra: ")

texto_2 = input("Ingrese la segunda palabra: ")

print(texto_1 == texto_2)






#EJERCICIO 13
"""
Realizar un programita que pida dos palabras al usuario y muestre la palabra que resulta
de concatenar (sumar) ambas.
"""



print("Le pediremos ingresar dos palabras, y mostraremos por pantalla la contatenación de ambas")

palab_1 = input("Ingrese la primer palabra: ")

palab_2 = input("Ingrese la segunda palabra: ")

print(palab_1, palab_2)




#EJERCICIO 14
"""
Realizar un programita que pida una contrase ̃na al usuario y determine si es la contrase ̃na
correcta, dando un mensaje de error cuando no lo sea.
"""


clave_usuario = input("Ingrese su clave de acceso al sistema (miclave): ")

if clave_usuario != "miclave":
    print("Clave incorrecta!")
    
    
    
    
    
#EJERCICIO 15
"""
Realizar un programita que pida 3 n ́umeros enteros al usuario, y determine el orden
creciente de los mismos, es decir, los muestre en pantalla de menor a mayor.
"""

print("Le pediremos ingresar 3 números enteros para ordenarlos de menos a mayor")

num_1 = int(input("Ingrese el primer número: ")) 
num_2 = int(input("Ingrese el segundo número: ")) 
num_3 = int(input("Ingrese el tercer número: ")) 

if num_1 > num_2 and num_2 > num_3:
    print("El orden es: ", num_3,num_2,num_1)
    
if num_2 > num_1 and num_1 > num_3:
    print("El orden es: ", num_3,num_1,num_2)
    
if num_2 > num_1 and num_3 > num_1:
    print("El orden es: ", num_1,num_3,num_2)
    
if num_1 > num_1 and num_3 > num_2:
    print("El orden es: ", num_2,num_3,num_1)
    
if num_3 > num_1 and num_1 > num_2:
    print("El orden es: ", num_2,num_1,num_3)
    
if num_3 > num_1 and num_2 > num_1:
    print("El orden es: ", num_1,num_2,num_3)





#EJERCICIO 16
"""
Realizar un programita que pida 2 datos: el valor del d ́olar actual, y la cantidad de pesos
que posee el usuario, y determine cu ́antos d ́olares tendr ́ıa el usuario entonces.
"""

print("Pprograma para mostrar cuántos dolares tiene.")
dolar = int(input("Ingrese la cotización actual del dolar: "))
pesos = int(input("Ingrese la cantidad de pesos: "))

print("La cantidad de dolares que posee es de: ", pesos / dolar)




#EJERCICIO 17
"""
Realizar un programita Convertir a Pesos: que pida 2 datos, el valor del d ́olar actual, y el
precio en d ́olares de un producto. Calcular y mostrar en pantalla cu ́anto cuesta en pesos
ese producto.
"""
print("Programa para mostrar cuánto cuesta un producto en pesos cotizado en dolares ")
dolar = int(input("Ingrese la cotización del dolar actual: "))
precio_dolar = int(input("Ingrese el valor del producto en dolares: "))
print("El precio del producto en pesos es de: ", dolar * precio_dolar)



#EJERCICIO 18
"""
Realizar un programita que pida una nota de un alumno, y devuelva Aprobado si la
nota est ́a entre 6 y 8. Desaprobado, si la nota es menor que 6, y Promocionado si
la nota es mayor o igual a 9. (*adem ́as se deber ́a controlar que la nota ingresada es una
nota v ́alida entre 1 y 10 previo a clasificarla)
"""


nota_alu = int(input("Ingrese la nota del alumno y determinaremos su condición: "))

if nota_alu >=1 and nota_alu <=10:
    if nota_alu >=6 and nota_alu <=8:
        print("Aprobado")
    elif nota_alu >=9:
        print("Promocionado")
    else:
        print("Desaprobado")
else:
    print("Ingrese una nota válida!")

   
    