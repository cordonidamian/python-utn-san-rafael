# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:15:39 2020

@author: dcordoni
"""

import random




# 1. Pedir una frase al usuario y mostrarla en may ́usculas y en min ́usculas.

frase = input("Ingrese un texto cualquiera y lo mostraremos en minúsculas y en mayúsculas: ")

print(frase.lower())
print(frase.upper())





# 2. Pedir una frase al usuario y si se encuentra en may ́usculas devolverla en min ́usculas, y
#    vice versa.

frase = input ("Ingrese un texto todo en mayúsculas o en minúsculas: ")

if frase.isupper():
    print(frase.lower())
else:
    print(frase.upper())   
    
    
    
    
    
# 3. Pedir una frase y una palabra al usuario. Determinar si la palabra se encuentra en la
#    frase. *Utilizar in
    
print("Le pediremos una frase y luego una palabra, determinaremos si la palabra se encuentra en la frase ingresada")

frase = input("Ingrese una frase: ")
text = input("Ingrese un texto: ")

if text in frase:
    print("El texto ingresado(", text,")pertenece a la frase!")
else:
    print("El texto ingresado(",text,")no pertenece a la frase!")





# 4. Pedir una palabra al usuario y determinar si ingreso todos numeros o una palabra cual-
#    quiera.
    
palabra = input("Ingrese un texto culquiera: ")

if palabra.isdigit():
    print("Usted a ingresado solo números!")
elif palabra.isalpha():
    print("Usted a ingresado solo texto!")
elif palabra.isalnum():
    print("Usted a ingresado texto y números!")
    
    
    
    
    
# 5. Pedir una frase al usuario y una palabra. Determinar si esa frase empieza o termina con
#    dicha palabra.    

frase = input("Ingrese una frase: ") 
palabra = input("ingrese una palabra: ")  

if frase.startswith(palabra):
    print("La palabra es igual al comienzo de la frase")
elif frase.endswith(palabra):
    print("La palabra ingresada es la última de la frase")
else:
    print("La palabra ingresada no es ni la primera ni la última")
   
    
    
    
    
# 6. Realizar un programa que pida una frase y una letra. Y determine la cantidad de ocu-
#    rrencias de esa letra en dicha frase.
    
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
contador = 0


for text in frase:
    if letra == text:
        contador = contador + 1
print("La cantidad de veces que encontramos la letra ingresada es de:", contador)





    
# 7. Realizar un programita que tome una frase y devuelva la misma frase con guiones inter-
#    calados. (hola → h-o-l-a) Tip: utilizar los m ́etodos split y join: Googlear sobre ellos    

frase = input("Ingrese una frase: ")

lista = frase.split()

print("-".join(lista))






# 8. Realizar un programita que dada la frase ”23, 6, 82, 5, 123, 65”devuelva la lista [23, 6,
#    82, 5, 123, 65]. Tip: utilizar el m ́etodo split

frase = "23, 6, 82, 5, 123, 65"
print(frase.split())






# 9. ¿C ́omo puedo acceder al  ́ultimo elemento de una lista, siempre, sin saber a priori cuantos
#    elementos tiene ni utlizando len() a tal fin?


lista = [1,2,4,3,6,8,5,4,3]
print("El último número de la lista es:", lista[-1])






# 10. Dada una lista de 10 frutas cualesquiera, realizar las siguientes operaciones: (Utilizar los
#     m ́etodos de las listas en este punto)
#   a) Determinar si la fruta cereza se encuentra en dicha lista.
#   b) Pedirle una fruta al usuario, y agregarla a la lista.
#   c) Si se encuentra la fruta durazno, eliminarla de la lista.
#   d) Mostrar las primeras 5 frutas de la lista.
#   e) Mostrar la cantidad total de frutas de la lista.
#   f ) Pedir al usuario 5 verduras y guardarlas en una lista nueva. Unir ambas listas y
#       mostrar el resultado final.
#   g) Ordenar la lista.



lista_frutal = ["manzana", "pera", "naranja", "banana", "cereza", "ciruela", "durazno", "fresa", "granada", "piña"]

if "cereza" in lista_frutal:
    print("(a) Cereza se encuentra en el listado")
    
fruta = input("(b)Ingrese una fruta al listado: ")
lista_frutal.append(fruta)
print("La lista actualizada es:",lista_frutal)

if "durazno" in lista_frutal:
    lista_frutal.remove("durazno")
    print("(c) Hemos eliminado durazo de la lista", lista_frutal)
    
print("(d) Las 5 primeras frutas son: ", lista_frutal[0:5])

print("(e) La cantidad total de frutas es de:", len(lista_frutal))

lista_verduras = []
cont = 0
print("(f) Ingrese 5 verduras: ")
for i in range(5):  
    cont = cont + 1
    ver = input("Ingrese una nueva verdura:")
    lista_verduras.append(ver) 
print("La lista de verduras es: ", lista_verduras)

lista_final = lista_frutal + lista_verduras

lista_final.sort()
print("La lista ordenada alfabéticamente de verduras y frutas es: ", lista_final)





# BUCLES FOR

#   11. Realizar los siguientes programitas:

#   a) Pedir al usuario una palabra e imprimirla en vertical, una letra por l ́ınea.
#   b) Pedir al usuario una palabra e imprimirla en vertical, pero en orden inverso, es decir,
#    la primer letra a imprimir, ser ́a la  ́ultima de la palabra.

palabra = input("Ingrese una palabra cualquiera: ")
lista = list()

for i in range(len(palabra)):
    print(palabra[i])

for i in range(len(palabra)):
    print(lista.append(palabra[i]))
    


#   c)
total = 0
for p in range(51):
    total = p**2 + 3*p
print(total)    
    
    
    
#   d) 
 

nro_1 = int(input("Ingrese el primer número: "))
nro_2 = int(input("Ingrese el segundo número: "))

for j in range(46):
    total = j + (nro_2 - nro_1) / (nro_1 ** 2) + (nro_2 **2) + (j **2)

print(total)






#   12. Pedir al usuario 10 n ́umeros enteros y guardarlos en una lista. Ordenar la lista, y mostrarla
#       en pantalla. Mostrar adem ́as, el valor m ́aximo y m ́ınimo de la misma. Utilizar los m ́etodos
#       de la lista, adem ́as de las funciones max() y min()

input("Le pediremos ingresar 10 números")
nros = list()
for i in range(10):
    temp = int(input("Ingrese números: "))
    nros.append(temp)
print("Lista:",nros)
print("Lista ordenada:",sorted(nros))
print("Número máximo:",max(nros))
print("Número mínimo:",min(nros))


#   13. Realizar un programa que permita al usuario ingresar una longitud e imprima en pantalla
#   un rect ́angulo de numerales, hueco por dentro. Por ejemplo, si se ingres ́o 4, se ver ́a en
#   pantalla: Tip: Puede ser  ́util pensarlo por l ́ınea horizontal



cant = int(input("Ingrese un número: "))
rango = cant -2

print(cant * "#")

for i in range(rango):
    print("#" + (rango * " ") + "#")

print(cant * "#")





# N ́umeros aleatorios
#   14. Utilizando la libreria random y sus m ́etodos, realice los siguientes programitas:

#   a) Dada una frase ingresada por el usuario, devolver en pantalla una letra de la misma,
#       al azar.



frase = list()
frase = input("Ingrese una frase cualquiera: ")
print(random.choice(frase))

#   b) Pedir un n ́umero al usuario, y determinar si  ́este es mayor o menor que un n ́umero
#       aleatorio entre 1 y 100.

nro = int(input("Ingrese un número entre 1 y 100: "))

nro_aleatorio = random.randrange(1, 100)

if nro > nro_aleatorio:
    print("El número ingresado es mayor el número aleatorio:", nro_aleatorio)
elif nro == nro_aleatorio:
    print("El número ingresado es igual al aleatorio:", nro_aleatorio)
else:
    print("El número ingresado es menor al número aleatorio:", nro_aleatorio)




#   15. Dada una lista de colores inventada, devolver un color al azar y mostrarlo en pantalla.    
    
colores = ["blanco", "verde", "azul", "amarillo", "naranja"]

print(random.choice(colores))






#   16. Llenar una lista con 50 n ́umeros enteros aleatorios entre 1 y 10.

contenedor_nro = list()

for i in range(51):
     temp = random.randrange(1, 10)
     contenedor_nro.append(temp)
print(contenedor_nro)






#   17. Llenar una lista con 10 n ́umeros con decimales aleatorios entre 0 y 1.


nro_decimales = list()

for i in range(10):
    temp = random.random()
    nro_decimales.append(temp)
    
print(nro_decimales)







#   18. Determine qu ́e hace el siguiente c ́odigo, en palabras simples, para qu ́e sirve este progra-
#   mita:

#frase = input("Ingrese una frase:")
#frase = frase.strip ()
#c = 0
#for i in range(len(frase )):
#if (frase[i] == ’ ’):
#c = c + 1

#print(c+1)






#   19. Realizar un programa que permita al usuario ingresar una frase y determine la cantidad
#       de vocales que hay en la misma.


frase = input("Ingrese una frase, determinaremos la cantidad de vocales que contiene: ")

cont = 0
for rep in frase:
    if rep == "a" or rep == "e" or rep == "i" or rep == "o" or rep == "u":
        cont = cont + 1
print("La cantidad de vocales es de:", cont)






#   20. Pedirle una frase al usuario y una letra, determinar cuantas veces est ́a esa letra en la
#       frase.    


frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
cont = 0

for rep in frase:
    if letra == rep:
        cont = cont + 1
print("La letra ingresada se repite:", cont ," veces")







#   21. Realizar un programa que permita al usuario ingresar una frase y determine la cantidad
    #   de palabras que hay en la misma.


frase = input("Ingrese una frase: ")
cont = 1

for rep in frase:
    if rep == " ":
        cont = cont + 1
print("La frase contiene:", cont ," palabras")






#   22. Realizar un programa que permita al usuario ingresar una palabra e imprima en pantalla
#       la palabra resultante de haberle quitado todas las vocales.



palabra = input("Ingrese una palabra: ")
new_pala = list()
sin_voca = ""

for rep in palabra:
    if rep != "a" and rep != "e" and rep != "i" and rep != "o" and rep != "u":
        new_pala.append(rep)

       
for i in new_pala:
    sin_voca = sin_voca + i
    
print(sin_voca)






#   23. Pedirle al usuario dos palabras. Determinar si una es la inversa de la otra.

#   Opcion A
pala_1 = input("Ingrese la primer palabra: ")
pala_2 = input("Ingrese la segunda palabra: ")
new_pala = ""

for i in range(len(pala_2)):
    new_pala = new_pala + pala_2[-(i +1)]

if pala_1 == new_pala:
    print("La segunda palabra es la inversa de la primera!")




#   Opción B
pala_1 = input("Ingrese la primer palabra: ")
pala_2 = input("Ingrese la segunda palabra: ")

compara = pala_2[::-1]
print(compara)

if pala_1 == compara:
    print("La segunda palabra es la inversa de la primera!")
else:
    print("La segunda palabra no es la inversa de la primera!")






#   24. Pedirle una palabra al usuario y determinar si es pal ́ındrome o no. (si se lee igual del
#       derecho que del rev ́es)
 

#   Opcion A
pala_1 = input("Ingrese la primer palabra: ")
new_pala = ""

for i in range(len(pala_1)):
    new_pala = new_pala + pala_1[-(i +1)]

if pala_1 == new_pala:
    print("La palabra ingresada es palíndrome!")
else:
    print("La palabra ingresada no es palíndrome!")
    
    


#   Opción B    
pala_1 = input("Ingrese una palabra: ")

if pala_1 == pala_1[::-1]:
    print("La palabra ingresada es palíndrome!")
else:
    print("La palabra ingresada no es palíndrome!")