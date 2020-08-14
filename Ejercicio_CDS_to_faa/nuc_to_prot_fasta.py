#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 18:09:25 2020

@author: mariacadavid
"""

#General Practice in Python
#Instruction:
#Build a Python function that opens a nucleotide .fna CDS file, and creates the associated CDS .faa file.


#Import 
import os 
import io #tipo para un archivo "io.TextIOWrapper"

#Funcion para traducir fasta CDS genomico a peptidos
def get_polipeptides_from_genomicfasta(nucfasta: io.TextIOWrapper )-> io.TextIOWrapper:
    #Definición código genético
    gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
    dataout= []

    #Validaciones 
    assert os.path.isfile(nucfasta) , "archivo no existe"
    
    #Abrir archivo nucleotidos 
    inputdata = open(nucfasta,"r") 
    
    
    #logica
    linea = inputdata.readline()                 
    while linea != '':
        if linea[0] == ">":
            namesplit= linea.split("_cds_")  #cambiarle el "cds" por "prot" en el header
            newname= str(namesplit[0])+"_prot_"+str(namesplit[1])[:-1]
            dataout.append(newname)
            linea= inputdata.readline()
            seqnuc=""
            while linea != '':
                if linea[0] != ">":
                    seqnuc += str(linea)[:-1]  #aca quitar el salto de linea
                    linea= inputdata.readline()
                else:
                    break
            seqprot=""
            for i in range (0,len(seqnuc),3):
                codon= (seqnuc[i:i+3]) 
                if codon in gencode:
                    seqprot += str(gencode[codon])
            fullprot=("M"+str(seqprot)[1:-1]) #iniciar siempre con M
            for i in range(0,len(fullprot),80): 
                protsec=(fullprot[i:i+80])
                dataout.append(protsec)    
        else:
            linea= inputdata.readline()
    inputdata.close() 
    return(dataout)

   
    
#Funcion para escribir polipeptidos en nuevo archivo fasta .faa
def write_polipeptides_to_faa(polipeptides:list, output_filename:io.TextIOWrapper): 
    outputdata= open(output_filename,"w")
    outputdata.writelines("%s\n" % s for s in polipeptides)
    outputdata.close()

#Funcion main 
def main (nucfasta, output_filename): 
   poli= get_polipeptides_from_genomicfasta(nucfasta)
   write_polipeptides_to_faa (poli,output_filename)
    
    
#Llamada de prueba  
if __name__ == "__main__" :
    main("cds_from_genomic.fna", "prot_fasta.faa")
    
