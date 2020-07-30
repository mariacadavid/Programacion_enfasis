#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:17:13 2020

@author: mariacadavid
"""

#Ejercicio repaso condicinales Python 

#Construya una función python que resuelva la siguiente necesidad. corresponde al problema 450 del libro de lógica algorítmica artesanal.
#Granos de Cosecha. Los granos de distintas cosechas muy especiales se recogen en contenedores.
#Los contenedores están codificados con números enteros de 5 dígitos, de tal modo que:

#-Los granos que pesan en promedio 15 gramos se almacenan en contenedores cuyo código  comienza en 10, 30 Y 87.   
#-Los granos que pesan en promedio 18 gramos se almacenan en contenedores cuyo código comienza con 35, 95, y 45.  
#-Los granos que pesan en promedio 20 gramos se almacenan en contenedores cuyo código comienza con 12, 31, y 71.  
#-Todos los demás códigos corresponden a contenedores destinados a almacenar tierra abonada. 
#El código del contenedor también especifica la especie del grano, de tal modo que:
#-Los códigos terminados en 18,28 y 38 corresponden a la especie Alphus. 
#-Los códigos terminados en 32,56 y 78 corresponden a la especie Betus.  
#El tercer dígito de los códigos corresponde al semestre de recolección 1 o 2. 

#Se desea que el algoritmo ayude a la valoración del grano en contenedores que pasan por una banda que lee una string que representa el tipo de grano, y el peso del contenedor en kilogramos. Con esta información, se procede a calcular el valor de los contenedores, así:  
#-granos en promedio 15 gramos tienen un valor base de 10 centavos.  
#-granos en promedio 18 gramos tienen un valor base de 20 centavos.  
#-granos en promedio 20 gramos tienen un valor base de 30 centavos.  
#-granos del primer semestre tienen un recargo del 20% del valor base. 
#-granos del segundo semestre tienen un recargo del 23% del valor base. 
#-granos de la especie Alphus tienen un recargo del 3% del valor base. 
#-granos de la especie Betus tienen un recargo del 7%. 
#Elabore una función que reciba una cadena que representa el código de contenedor, y un valor numérico que representa el peso de contenedor en kilogramos, y calcule el valor total del contenedor.

#Funcion
def leecodigo(cod,kg):
    preciobase= 0
    precio=0
    if cod[0:2] == "10" or cod[0:2] == "30" or cod[0:2] == "87":
        #gramos=15
        preciobase= (kg*1000/15)*10
    elif cod [0:2] == "35" or cod[0:2] == "95" or cod[0:2] == "45":
        #gramos=18
        preciobase=  (kg*1000/18)*20
    elif cod [0:2] == "12" or cod[0:2] == "31" or cod[0:2] == "71":
        #gramos=20
        preciobase= (kg*1000/20)*30
    else:
        #es tierra
        preciobase = 0 
        
    if cod[3:5] == "18" or cod[3:5] == "28" or cod[3:5]== "38":
        #sp="Alphus"
        precio= preciobase + preciobase*0.03
    elif cod [3:5] == "32" or cod[3:5]== "56" or cod[3:5] == "78":
        #sp= "Betus"
        precio= preciobase + preciobase*0.07
    else:
        #sp= "otra"
        precio= preciobase
        
    if cod [2] == "1":
        #semestre=1
        precio= precio + preciobase*0.2
    elif cod [2] == "2":
        #semestre=2
        precio= precio + preciobase*0.23
    else:
        #seria un error porque solo puede ser recogido en el 1 o 2 semestre del año 
        precio= "no fue recogido"
    
    return precio
    
#intentos:
print (leecodigo("95278",1))
print (leecodigo("10156",2))
print (leecodigo("10156",400))
print (leecodigo("20156",400))
print (leecodigo("31255",400))
print (leecodigo("31055",400))
