import io
import os

#get the list of the gene bank files in a directory
def get_flatfile_list(gbff_files_path) -> list:
    list_files= os.listdir(gbff_files_path)
    list_gbff_files=[]
    for file in list_files:
        if file.endswith(".gbff"):
            list_gbff_files.append(file)      
    return (list_gbff_files)

#open file
def get_gbff_file_handler(gbff_files_path: str, name_file: str)->io.TextIOWrapper:
    import io
    file_complete_path= gbff_files_path + "/" + name_file
    file_handler = open(file_complete_path,"r")  
    return (file_handler)

#close file handler 
def close_gbff_file_handler(file_handler: io.TextIOWrapper):
    file_handler.close()
    return


     
def get_info_organism (file_handler: io.TextIOWrapper )-> dict:
    
    line = file_handler.readline()
    splited = line.split()
    locus= splited[1]
    base_pairs= splited[2]
    seq_type= splited[4]
    structure= splited [5]
    completness=  splited [6]
    date= splited [7]
    
    line = file_handler.readline()[:-1]
    definition = ""
    while line !="":
        definition += line[12:] + " "
        line=file_handler.readline()[:-1]
        if not line.startswith(" "):
            break
        
    
    accession=""    
    while line !="":
        accession += line[12:] + " "
        line=file_handler.readline()[:-1]
        if not line.startswith(" "):
            break

    
    version= line.split()[1]
    
    line=file_handler.readline()[:-1]
    bioproject= line.split()[2]
    
    line=file_handler.readline()[:-1]
    biosample= line.split()[1]
    
    line=file_handler.readline()[:-1]
    assembly= line.split()[1]
    
    line= file_handler.readline()[:-1]
    keywords= line.split ()[1:]

    line= file_handler.readline()[:-1]
    line= file_handler.readline()[:-1]
    organism_name= line[12:]
    
    line= file_handler.readline()[:-1]
    taxonomy= ""
    while line !="": 
        taxonomy += line [12:] + " " 
        line= file_handler.readline()[:-1]
        if not line.startswith(" "):
            break
    
    organism_info= {}
    organism_info.update ({"locus":locus})
    organism_info.update ({"base_pairs":base_pairs})
    organism_info.update ({"seq_type":seq_type})
    organism_info.update ({"structure":structure})
    organism_info.update ({"completness":completness})
    organism_info.update ({"date":date})
    organism_info.update ({"definition":definition})
    organism_info.update ({"accession":accession})
    organism_info.update ({"version":version})
    organism_info.update ({"bioproject":bioproject})
    organism_info.update ({"biosample":biosample})
    organism_info.update ({"assembly":assembly})
    organism_info.update ({"keywords":keywords})
    organism_info.update ({"organism_name":organism_name})
    organism_info.update ({"taxonomy":taxonomy})
    
    return (organism_info)

#Gets the comment section. # in: handler of a flat file already open

def get_comments (file_handler: io.TextIOWrapper )-> dict:
    
    
    comments_table = {}
    line = file_handler.readline()[:-1]
    comment= ""
    value= 0
    
    while line [12:25] !="Genes (total)": 
        line=file_handler.readline()[:-1]
    
    comment= line[12:25]
    value= line.split()[3]
    comments_table.update ({comment : value}) 
    
    line=file_handler.readline()[:-1]
    comment= line[12:24]
    value= line.split()[3]
    comments_table.update ({comment : value})
    
    line=file_handler.readline()[:-1]
    comment= line[12:26]
    value= line.split()[3]
    comments_table.update ({comment : value})
    
    line=file_handler.readline()[:-1]
    comment = line[12:15] 
    comment_2= line.split("(")[1]
    comment_3= comment_2.split(")")[0]
    comment= comment + "(" + comment_3 + ")"
    value= line.split("::")[1]
    comments_table.update ({comment : value})
    
    
    return (comments_table) 

def get_prot (file_handler: io.TextIOWrapper) -> list :  
    
    protein_list=[]
    
    for line in file_handler:
        protein_info={}
        if line [5:8] == "CDS":
            positions= line.split()[1]
            protein_info.update ({"position" : positions})
            
            line= file_handler.readline()[:-1]
            if line.split("=")[0] =="                     /gene": 
                gene_name= line.split("=")[1]
                protein_info.update ({"gene_name" : gene_name})
                
                line= file_handler.readline()[:-1]
                locus_tag= line.split("=")[1]
                protein_info.update ({"locus_tag" : locus_tag})
            
            else: 
                locus_tag= line.split("=")[1]
                protein_info.update ({"gene_name" : None})
                protein_info.update ({"locus_tag" : locus_tag})
            
            while "a" == "a":
                line= file_handler.readline()[:-1]
                if line.split("=")[0] == "                     /note":
                   break 
               
            note= ""
            while line !="":
                note += line [21:] + " "
                line= file_handler.readline()[:-1]
                if line[21:33] =="/codon_start":
                    break
            note= note.split("=")[1]    
            protein_info.update ({"note" : note})
            
            codon_start_position = line.split("=")[1]
            protein_info.update ({"codon_start_position" : codon_start_position})
         
            line= file_handler.readline()[:-1]
            translate_table = line.split("=")[1]
            protein_info.update ({"translate_table" : translate_table})
         
            line= file_handler.readline()[:-1]
            product= ""
            while line !="":
                product += line [21:] + " "
                line= file_handler.readline()[:-1]
                if line[21:32] =="/protein_id" or line[0:9] == "     gene" or line[0:6] == "CONTIG":
                    break 
            product = product.split("=")[1]    
            protein_info.update ({"product" : product})
            
            protein_ncbi_id=""
            if line[21:32] =="/protein_id":
                while line !="":
                    protein_ncbi_id += line [21:] + " "
                    line= file_handler.readline()[:-1]
                    if line[0:9] == "     gene" or line[0:6] == "CONTIG" or line [21:33] == "/translation":
                        break 
           
                protein_info.update ({"protein_ncbi_id" : protein_ncbi_id[12:]})
            else:
                protein_info.update ({"protein_ncbi_id" : None})
            
            if line [21:33] == "/translation":
                seq= ""
                while line[0:6]!="CONTIG":
                    seq += line [21:-1]
                    line= file_handler.readline()
                    if line[5:9] =="gene":
                        break
                seq= seq.split("=")[1]    
                protein_info.update ({"translation" : seq})
            
            else:
                protein_info.update ({"translation" : None})
                    
                

            protein_list.append(protein_info)
            
            #diccionario por proteina contiene:
                #protein_ncbi_id
                #gene_name (if available)
                #locus_tag
                #note
                #position
                #codon_start_position
                #translate_table
                #product
                #translation
            
    return (protein_list)