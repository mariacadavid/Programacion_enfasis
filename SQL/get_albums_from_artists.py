#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 19:47:15 2020

@author: mariacadavid
"""

#Al ejecutar desde python se deben incluir dos parametros: (1)path name de la base de datos, (2)nombre o nombre parcial del artista de interés
import sys
import sqlite3 as sql
con = sql.connect(sys.argv[1])
cur = con.cursor()
cur.execute("SELECT albums.Title From albums INNER JOIN artists ON albums.ArtistId = artists.ArtistId WHERE artists.name like (?)",("%"+sys.argv[2]+"%",))
print(cur.fetchall())
