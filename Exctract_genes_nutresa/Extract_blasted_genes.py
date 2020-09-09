#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 00:08:45 2020

@author: mariacadavid
"""

import time

def obtain_sequence(blast_output_file, complete_fasta_file):
    
   #Open file
   blastdata = open(blast_output_file,"r")
   line = blastdata.readline()[:-1]
  
   genes= []
   while line != '':
        if line.split(",")[1] == "0.0":
            header=">"+line.split(",")[0] 
            start_position= int( line.split(",")[2] )
            end_position=int (line.split(",")[3])
            line= blastdata.readline()
            referencedata = open(complete_fasta_file,"r")
            line_fasta = referencedata.readline()[:-1]
            start = time.time()
            while line_fasta != '':
                if header == line_fasta:
                    seqnuc=""
                    line_fasta = referencedata.readline()[:-1]
                    while line_fasta != '':
                        if line_fasta[0] != ">":
                            seqnuc += str(line_fasta) 
                            line_fasta = referencedata.readline()[:-1]
                        else:
                            break
                    gene= seqnuc[start_position -1 :end_position]
                    genes.append(header)
                    genes.append(gene)
                    
                else:
                    line_fasta =referencedata.readline()[:-1]
            end = time.time()
            delta = end - start
            print ("took %.2f seconds to process" % delta)
                
        else:
            line= blastdata.readline()
            
   blastdata.close()
   referencedata.close()
   print (genes)
   return (genes)
  

   
def write_genes_to_fasta(genes:list, output_filename:str): 
    genes_fasta= open(output_filename,"w")
    genes_fasta.writelines("%s\n" % s for s in genes)
    genes_fasta.close()

genes= obtain_sequence("/Users/mariacadavid/Desktop/Tesis_Clostridiales/Data/Reference_genomes_ncbi/CDS_clostridia_NCBI/genome_assemblies_cds_fasta/blastout_dnak1_tblastn_ref1uniprot_ncbiCDS_tabular5.txt", "/Users/mariacadavid/Desktop/Tesis_Clostridiales/Data/Reference_genomes_ncbi/CDS_clostridia_NCBI/genome_assemblies_cds_fasta/ncbi-genomes-2020-09-01/ncbi_all_genomes.fna")
write_genes_to_fasta(genes, "/Users/mariacadavid/Desktop/Tesis_Clostridiales/Data/Reference_genomes_ncbi/CDS_clostridia_NCBI/genes_dnak1_NCBI_tblastn(abriendoycerrandoarchivo).txt")