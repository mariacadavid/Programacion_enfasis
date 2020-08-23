#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 19:47:15 2020

@author: mariacadavid
"""

#Al ejecutar python con el archivo get_albums_from.py se deben incluir dos parametros: (1)path name de la base de datos, (2)nombre o nombre parcial del artista de interés

def get_arguments(args: list) -> list: 
    list_variables= []
    list_variables.append(args[1])
    list_variables.append(args[2])
    return(list_variables) 
    
def get_albums_titles(list_variables: list)-> list:
    path= list_variables[0]
    partial_name= list_variables[1]
    import os 
    assert os.path.isfile(path) , "archivo no existe"
    import sqlite3 as sql
    con = sql.connect(path)
    cur = con.cursor()
    query= "SELECT albums.Title From albums INNER JOIN artists ON albums.ArtistId = artists.ArtistId WHERE artists.name like (?)"
    cur.execute(query,("%"+partial_name+"%",))
    collection= (cur.fetchall())
    con.close()
    return(collection)

def print_titles(collection:list):
    print (collection)
    
def main_fun(argv: list):
    print_titles(get_albums_titles(get_arguments(argv)))
    
if __name__ == "__main__":
    import sys
    main_fun (sys.argv)
    
    
