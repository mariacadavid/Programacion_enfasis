#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 19:16:59 2020

@author: mariacadavid
"""

#Cree una función  que reciba el código de un continente, y devuelva el total de infectados por país del continente indicado.
#La función devolverá un diccionario, donde cada entrada es un código de país, y cuyo valor es el número de muertes.
#La función también devolverá, junto con la colección, el pais que más muertes presenta a la fecha.

#Usar archivo descargado de la web 
#Es un archi tipo CSV 
#El primer registro es informativo, y corresponde a los nombres de los campos

#condiciones
#Los campos de interés para el problema son continent y total_deaths.
#Registros que no tengan dato en el campo iso_code no deben ser procesados.
#Registros cuyo iso_code es OWID_WRL no deben ser procesados.
 
import os 

def covid_19_cases_by_country(file,continent):
    cases = 0
    stats = { }
    #Cual posicion del record en el archivo corresponde a cual variable:
    ISO_CODE = 0 
    LOCATION = 2
    CASES = 5
    CONTINENT = 1
    
    assert os.path.isfile(file) , "archivo no existe"
    data = open(file,"r")                    #abrir archivo modo lectura
    data.readline()                          #descartar fila de encabezados
    
                  
    for rec in data:                       #recorrer registros
        campos = rec.split(",")            #extraer campos
        pais = campos[LOCATION]            #extraer pais
        cases = campos[CASES]              #extraer casos 
        
        if campos[CONTINENT] != continent:          #evitar registros de continentes no pedidios
            continue
        if campos[ISO_CODE] in [ 'OWID_WRL' , '']:  #evitar ciertos códigos
            continue                          
        if campos[LOCATION] == '':                  #evitar pais vacío
            continue
        if not pais in stats:                  #si pais no está en colección 
            stats[pais] = 0                    #adicionarlo con valor 0
        try:
            stats[pais] += float(cases)        #sumar las casos por pais
        except ValueError:                     #controlando conversión 
            continue
    maxcountry =(max(stats, key=lambda key: stats[key]))
    data.close() 
    return stats, maxcountry

if __name__ == "__main__":
    print(covid_19_cases_by_country("covid_data.csv","South America"))



