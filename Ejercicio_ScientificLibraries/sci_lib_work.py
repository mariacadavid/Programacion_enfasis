#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:51:08 2020

@author: mariacadavid
"""

#database of paleobiological data

#Use pandas and matplotlib to get the following requested information.

#-Percentage distribution (histogram, pie), or just a table, for the following variables:
 #     phylum, class, stratscale, environment, tectonic_setting, preservation_quality

#-Make plot tables or scattered plots to relate 
 #  life_habit vs reproduction
  # diet with vs life_habit
   #reproduction vs life_habitat

#see demo for plot tables at
#https://matplotlib.org/gallery/misc/table_demo.html#sphx-glr-gallery-misc-table-demo-py

#see scattered plot at
#https://matplotlib.org/gallery/shapes_and_collections/scatter.html#sphx-glr-gallery-shapes-and-collections-scatter-py


import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


##Funciones para contabilizar casos y muertes por paises 
def covid_19_cases_by_country(file):
    cases = 0
    stats_cases = { }
    
    #Cual posicion del record en el archivo corresponde a cual variable:
    ISO_CODE = 0 
    LOCATION = 2
    CASES = 5
    
    assert os.path.isfile(file) , "archivo no existe"
    data = open(file,"r")                    
    data.readline()                          #descartar fila de encabezados
                  
    for rec in data:                       
        campos = rec.split(",")            #extraer campos
        pais = campos[LOCATION]            #extraer pais
        cases = campos[CASES]              #extraer casos 
          
        if campos[ISO_CODE] in [ 'OWID_WRL' , '']:  #evitar ciertos códigos
            continue                          
        if campos[LOCATION] == '':                  #evitar pais vacío
            continue
        if not pais in stats_cases:                  #si pais no está en colección 
            stats_cases[pais] = 0                    #adicionarlo con valor 0
        try:
            stats_cases[pais] += float(cases)        #sumar las casos por pais
        except ValueError:                    
            continue 
    data.close() 
    return stats_cases



def covid_19_deaths_by_country(file):
    deaths = 0
    stats_deaths = { }
    
    #Cual posicion del record en el archivo corresponde a cual variable:
    ISO_CODE = 0 
    LOCATION = 2
    DEATHS = 8
    
    assert os.path.isfile(file) , "archivo no existe"
    data = open(file,"r")                    
    data.readline()                          #descartar fila de encabezados
                  
    for rec in data:                       
        campos = rec.split(",")            #extraer campos
        pais = campos[LOCATION]            #extraer pais
        deaths = campos[DEATHS]              #extraer muertes 
        
        if campos[ISO_CODE] in [ 'OWID_WRL' , '']:  #evitar ciertos códigos
            continue                          
        if campos[LOCATION] == '':                  #evitar pais vacío
            continue
        if not pais in stats_deaths:                  #si pais no está en colección 
            stats_deaths[pais] = 0                    #adicionarlo con valor 0
        try:
            stats_deaths[pais] += float(deaths)        #sumar las muertes por pais
        except ValueError:                     
            continue
    
    data.close() 
    return stats_deaths


##Creation of pandas dataframe
cases_by_country= (covid_19_cases_by_country('/Users/mariacadavid/Google Drive/Universidad /BIOLOGÍA/Enfasis_computacional/Programación_Enfasis/Pandas_ejercicio/covid-data.csv'))
deaths_by_country= (covid_19_deaths_by_country('/Users/mariacadavid/Google Drive/Universidad /BIOLOGÍA/Enfasis_computacional/Programación_Enfasis/Pandas_ejercicio/covid-data.csv'))

df_cases =(pd.DataFrame.from_dict(cases_by_country, orient='index', columns= ['Cases']))
df_deaths=(pd.DataFrame.from_dict(deaths_by_country, orient='index', columns= ['Deaths'])) 
df_cases_deaths= (df_cases.set_index(df_cases.index).join(df_deaths.set_index(df_deaths.index)))


##scattered plot
N= 210 #cuantos paises
plt.title("Coronavirus total cases vs. total deaths per Country")
plt.ylabel("Total Cases")
y = df_cases_deaths.Cases
plt.xlabel("Total Deaths")
x = df_cases_deaths.Deaths  
colors = np.random.rand(N)
plt.scatter(x, y, c=colors, alpha=0.5)

plt.show()

##pie chart total cases by country
plt.pie(df_cases.Cases, labels= df_cases.index)
plt.title("Coronavirus total cases by Country")
plt.show() 

##pie chart total deaths by country
plt.pie(df_cases_deaths.Deaths, labels= df_cases.index)
plt.title("Coronavirus total deaths by Country")
plt.show() 


