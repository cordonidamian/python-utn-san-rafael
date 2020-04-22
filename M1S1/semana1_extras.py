# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:25:50 2020

@author: Damián Cordoni
"""

"""
1. Determinar si el siguiente codigo tiene alg ́un tipo de error, ya sea de sintaxis o de l ́ogica.
Sugerir correcci ́on si as ́ı fuese.

a = input( ̈Ingrese un n ́umero:”)
b = input(’Ingrese otro n ́umero:”)
if (b - a = 0):
print(’a y b son distintos’)


// en las variables a y b se va a guardar un STRING, la lógica del programa necesita de NUMEROS


"""


"""
2. ¿Qu ́e imprimir ́a en pantalla el siguiente c ́odigo?
n = 5
m = 1
o = 8
if ((n != m) and (o > m)) or (m == 1):
if (n + m == o + 2):
print(”)
else:
print(”listo”)
print(”tal vez”)


// el primer if se cumple, el segundo no por lo tanto imprimirá:     listo    tal vez

"""



"""
3. Escribir un programita que pida el d ́ıa de nacimiento (no la fecha, solo el d ́ıa, controlando
que est ́e entre 1 y 31) y el mes de nacimiento (como texto, enero, febrero, etc) al usuario.
Determinar el signo astrol ́ogico del usuario
"""
print("Le pediremos ingresar su diá de nacimento y luego el mes... determinaremos si signo astrológico")
dia_nacim = int(input("Ingrese su día de nacimiento (en números): "))
mes_nacim = input("Ingrese el mes en el que nacio (en minúsclas): ")

if dia_nacim >= 1 and dia_nacim <=31:
    if (dia_nacim >=21 and dia_nacim <=31 and mes_nacim == "marzo") or (dia_nacim >=1 and dia_nacim <=20 and mes_nacim == "abril"):
        print("Tu signo es Aries!")
        
    elif (dia_nacim >=21 and dia_nacim <=31 and mes_nacim == "abril") or (dia_nacim >=1 and dia_nacim <=20 and mes_nacim == "mayo"):
        print("Tu signo es Tauro!")

    elif (dia_nacim >=21 and dia_nacim <=31 and mes_nacim == "mayo") or (dia_nacim >=1 and dia_nacim <=21 and mes_nacim == "junio"):
        print("Tu signo es Gemini!")
        
    elif (dia_nacim >=21 and dia_nacim <=31 and mes_nacim == "junio") or (dia_nacim >=1 and dia_nacim <=22 and mes_nacim == "julio"):
        print("Tu signo es Cáncer!")
        
    elif (dia_nacim >=21 and dia_nacim <=31 and mes_nacim == "julio") or (dia_nacim >=1 and dia_nacim <=22 and mes_nacim == "agosto"):
        print("Tu signo es Leo!")
        
    elif (dia_nacim >=21 and dia_nacim <=31 and mes_nacim == "agosto") or (dia_nacim >=1 and dia_nacim <=22 and mes_nacim == "septiembre"):
        print("Tu signo es Virgo!")
        
    elif (dia_nacim >=21 and dia_nacim <=31 and mes_nacim == "septiembre") or (dia_nacim >=1 and dia_nacim <=22 and mes_nacim == "octubre"):
        print("Tu signo es Libra!")
        
    elif (dia_nacim >=21 and dia_nacim <=31 and mes_nacim == "octubre") or (dia_nacim >=1 and dia_nacim <=22 and mes_nacim == "noviembre"):
        print("Tu signo es Escorpio!")
        
    elif (dia_nacim >=21 and dia_nacim <=31 and mes_nacim == "noviembre") or (dia_nacim >=1 and dia_nacim <=21 and mes_nacim == "diciembre"):
        print("Tu signo es Sagitario!")
        
    elif (dia_nacim >=21 and dia_nacim <=31 and mes_nacim == "diciembre") or (dia_nacim >=1 and dia_nacim <=20 and mes_nacim == "enero"):
        print("Tu signo es Capricornio!")
        
    elif (dia_nacim >=21 and dia_nacim <=31 and mes_nacim == "enero") or (dia_nacim >=1 and dia_nacim <=18 and mes_nacim == "febrero"):
        print("Tu signo es Acuario!")
        
    elif (dia_nacim >=21 and dia_nacim <=31 and mes_nacim == "febrero") or (dia_nacim >=1 and dia_nacim <=20 and mes_nacim == "marzo"):
        print("Tu signo es Piscis!")




"""
4. Realizar un programita que pida 4 n ́umeros y los muestre ordenados en pantalla en orden
decreciente.
"""


print("Le pediremos ingresar 4 números enteros para ordenarlos de menor a mayor")

num_1 = int(input("Ingrese el primer número: ")) 
num_2 = int(input("Ingrese el segundo número: ")) 
num_3 = int(input("Ingrese el tercer número: ")) 
num_4 = int(input("Ingrese el tercer número: "))

if num_1 < num_2:
    menor = num_1
    ind1 = num_1
    
else:
    menor = num_2
    ind1 = num_2
    
if menor < num_3:
    menor = menor
    ind1 = ind1
    
else:
    menor = num_3
    ind1 = num_3
    
if menor < num_4:
    menor = menor
    ind1 = ind1
    
else:
    menor = num_4
    ind1 = num_4
    
    
if num_1 > num_2:
    mayor = num_1
    ind4 = num_1
    
else:
    mayor = num_2
    ind4 = num_2
    
if mayor > num_3:
    mayor = mayor
    ind4 = ind1
    
else:
    mayor = num_3
    ind4 = num_3
    
if mayor > num_4:
    mayor = mayor
    ind4 = ind1
    
else:
    mayor = num_4
    ind4 = num_4
    




num_a = -1
num_b = -1

if num_1 != menor and num_1 != mayor:
    num_a = num_1

if num_2 != menor and num_2 != mayor:
    if num_a != -1:
        num_b = num_2
    else: 
        num_a = num_2


if num_3 != menor and num_3 != mayor:
    if num_a != -1:
        num_b = num_3
    else: 
        num_a = num_3
        
        
if num_4 != menor and num_4 != mayor:
    if num_a != -1:
        num_b = num_4
    else: 
        num_a = num_4        
        
        
if num_a < num_b:
    print(mayor, num_b, num_a, menor)  
else:
    print(mayor, num_a, num_b, menor)        
    



"""
5. Realizar un programita que permita determinar si un tri ́angulo es equil ́atero, is ́osceles
o escaleno. Al usuario le deber ́a pedir 3 n ́umeros. Nota: Equil ́atero es cuando sus tres
lados son iguales. Escaleno cuando sus tres lados son distintos entre si. Is ́osceles cuando
al menos dos de sus lados son iguales.
"""
print("Ingrese las 3 medidas de un triángulo, determinaremos qué tipo es: ")
num_1 = int(input("Ingrese el primer número: ")) 
num_2 = int(input("Ingrese el segundo número: ")) 
num_3 = int(input("Ingrese el tercer número: ")) 

if num_1 == num_2 == num_3:
    print("Es un triangulo equilátero")    
    
elif num_1 == num_2:
    print("Es un triangulo isósceles")
    
elif num_1 == num_3:
    print("Es un triangulo isósceles")
    
elif num_2 == num_1:
    print("Es un triangulo isósceles")
    
elif num_2 == num_3:
    print("Es un triangulo isósceles")

elif num_3 == num_1:
    print("Es un triangulo isósceles")
    
elif num_3 == num_2:
    print("Es un triangulo isósceles")

else:
    print("Es un triangulo escaleno")





"""
6. Escribir un programita que permita calcular la edad de un perro equivalente en a ̃nos
humanos. Tip: Los dos primeros a ̃nos de un perro equivalen a 10.5 a ̃nos de un humano.
Despu ́es cada a ̃no del perro equivalen a 4 a ̃nos de un humano.
"""


edad = int(input("Ingrese la edad de su mascota: "))

if edad <= 2:
    print("La edad de su mascota es de: ", edad * 5.25)
else:
    print("La edad de su mascota es de: ", (edad * 4) + 10.5 )



"""
7. Escribir un programita que permita ingresar una letra y determine si es una consonante
o una vocal.
"""

letra = input("Ingrese una letra, determinaremos si es consonante o vocal: ")

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Es vocal")
else:
    print("Es consonante")