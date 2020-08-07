#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 18:00:00 2020

@author: mariacadavid
"""
#Taller pyton: Methanosphaera stadtmania

#Instrucciones:
#Methanosphaera stadtmaniae is a methanogen archaeon. 
#It is a non-motile, Gram-positive, spherical-shaped organism that obtains energy by using hydrogen to reduce methanol to methane. 
#It does not possess cytochromes and is part of the large intestine's biota. 

#Request:
#La secuencia de la archaea se encuentra disponible en NCBI bajo la referencia  MGYG-HGUT-02164.
#Construya código Python que abra el archivo y lo analice para contestar las siguientes preguntas: 

#1. Lista de códigos de proteína identificadas como dependiente de nickel
#2. De las proteínas dependientes de nickel encontradas, identifique cuál o cuáles (header de registro completo), 
#tienen la mayor presencia relativa de histidina. La presencia relativa es el conteo de histidinas dividido el número de aminoácidos dentro de la proteina.
#3. Entre todo el archivo, identifique la(s) proteína(s) de mayor peso molecular (si hay iguales entregan todas las iguales). 
#El peso molecular en gramos por mol se halla sumando los pesos moleculares individuales de los aminoácidos de la proteína. 
#Use termofisher para los pesos moleculares en gramos por mol de los aminoacidos.

#Consideraciones:
#-La descarga del archivo de secuencias se podrá hacer manual.
#-Las funciones del código deberán estar anotadas y con nombres apropiados.
#-Los tipos que devuelve la función deberán ser el mismo.
#-Se deberá validar la existencia del archivo en disco (assert of path file with os)
#-Todo error por validación será or medio de asserts.


import os 
import io
#tipo para un archivo "io.TextIOWrapper"

#Funcion para identificar proteinas dependientes de nickel
def nickel_dependent_proteins(file: io.TextIOWrapper )->list:
    nickel_proteins = []
    
    #Validaciones 
    assert os.path.isfile(file) , "archivo no existe"
    
    #Abrir archivo 
    data = open(file,"r") 
    
    #logica
    for line in data:
        if line[0] == '>' and "nickel" in line:   #Buscar en los encabezados del fasta
            code= line[1:15] 
            nickel_proteins.append(code)
    data.close()
    return nickel_proteins                    
    


#Funcion para saber cuales proteinas nickel tienen la mayor presencia relativa de histidina
def nickel_proteins_largest_histidine_content(file: io.TextIOWrapper) -> list:
    count_histidines= 0
    relativeab_histidine= 0
    histidine_content= {}
    longseq= 0 
     
    #Validaciones 
    assert os.path.isfile(file) , "archivo no existe"
    
    #Abrir archivo 
    data = open(file,"r") 
    
    #logica
    for line in data:
        if "nickel" in line:
            code= line[1:15]
            for seq in data:
                if seq.startswith(">"):
                    break
                else:
                    longseq += len(seq)  
                    count_histidines += seq.count("H")
            relativeab_histidine= count_histidines/len(seq) 
            histidine_content.update ({code : relativeab_histidine}) 
            #devolver solo el codigo de la proteina
    data.close()
    maxcontent =(max(histidine_content, key=lambda key: histidine_content[key]))
    return maxcontent
         

#Funcion para determinar proteinas de mayor peso molecular 
def mayor_peso_molecular(file: io.TextIOWrapper) -> list: 
    molecularw= {"A": 89.1,"R":	174.2, "N":	132.1, "D":	133.1, "C":	121.2, "E":	147.1, "Q":	146.2, "G":	75.1, "H":	155.2, "I":	131.2, "L":	131.2, "K":	146.2, "M":	149.2, "F":	165.2, "P":	115.1, "S":	105.1, "T":	119.1, "W":	204.2, "Y":	181.2, "V":	117.1}
    protw={}
    
    
    #Validaciones 
    assert os.path.isfile(file) , "archivo no existe"
    
    #Abrir archivo 
    data = open(file,"r") 
    
    #logica
    linea = data.readline()                 
    while linea != '':
        if linea[0] == ">":
            code= linea[1:15]
            linea= data.readline()
            weight=0.0
            while linea != '':
                if linea[0] != ">":
                    for aa in linea:
                        if aa in molecularw:
                            weight += molecularw[aa]
                    linea= data.readline()
                else:
                    break
            protw.update ({code : weight})
        else:
            linea= data.readline()
            
    data.close()
    maxweight =(max(protw, key=lambda key: protw[key]))
    return maxweight



def main(file):
    print(nickel_dependent_proteins(file))
    print(nickel_proteins_largest_histidine_content(file))
    print(mayor_peso_molecular(file))

#Llamadas de prueba  
if __name__ == "__main__" :
    main("protein_file.fasta")
    
    

#Notas:
# puedo hacer funciones para definiciones que uso varias veces en el archivo y que sea mas digerible para los demas 
# por ejemplo hacer una funcion para determinar si linea empieza por ">"

#def is_header_fasta(line): return line[0] == '>'

#ya con esta funcion anterior definida puedo decir dentro de las otras funciones de mi codigo: 
#if is_header_fasta(linea): 



