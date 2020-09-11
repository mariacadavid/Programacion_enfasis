#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 21:01:39 2020

@author: mariacadavid
"""

def read_command_line_arguments(args: list): 
    organism_name=args[1]
    return organism_name

def get_taxonomy_for_organism (organism_name):
    from Bio import Entrez
    Entrez.email= "mcadav29@eafit.edu.co"
    handle= Entrez.esearch(db="Taxonomy", term= organism_name)
    record = Entrez.read(handle)
    ide=(record["IdList"])[0]
    
    handle = Entrez.efetch(db="Taxonomy", id=ide, retmode="xml")
    records = Entrez.read(handle)
    simple_taxonomy= records[0]["Lineage"]
    #categories_taxonomy= records[0]["LineageEx"]
    
    return (simple_taxonomy)


import sys 
print(get_taxonomy_for_organism(read_command_line_arguments(sys.argv)))



#Lineage es el que saca lo que me pides, no lineageEX
#No sale la ultima clasificacion, deberia ponersela?