import sqlite3 as sql
    

#Insert header information to organism table
def insert_organism(organism_data:dict, path):
    con = sql.connect(path)
    cur = con.cursor()
    
    query= 'INSERT INTO "main"."Organism" ("locus", "base_pairs", "type", "structure", "completness", "date", "definition", "accession", "version", "bioproject", "biosample", "assembly", "keywords", "organism_name", "taxonomy") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    
   
  
    values= (organism_data['locus'], 
                       organism_data['base_pairs'],
                       organism_data['seq_type'], 
                       organism_data['structure'], 
                       organism_data['completness'], 
                       organism_data['date'], 
                       organism_data['definition'], 
                       organism_data['accession'], 
                       organism_data['version'], 
                       organism_data['bioproject'], 
                       organism_data['biosample'], 
                       organism_data['assembly'], 
                       ''.join(e +',' for e in organism_data['keywords']), 
                       organism_data['organism_name'],
                       organism_data['taxonomy']) 
  
    
    cur.execute(query, values)
    con.commit()
    
    id_organism = organism_data['locus']
    con.close()
    return id_organism



#Insert info to comment table
def insert_comments(comments_table:dict, id_organism, path):
    con = sql.connect(path)
    cur = con.cursor()
    organism_ID = id_organism
    query= 'INSERT INTO "main"."Extended_comments" ("organism_ID", "comment", "value") VALUES (?,?,?)'
    
    for key in comments_table:
        values= (organism_ID, key, comments_table[key])
        cur.execute(query,values)
        
    con.commit()
    con.close()
    return


#Insert a gene data
def insert_protein(protein_dict:dict, id_organism, path) :
    con = sql.connect(path)
    cur = con.cursor()
    
    organism_ID = id_organism
    query= 'INSERT INTO "main"."Protein" ("protein_NCBI_ID", "organism_ID", "gene_name", "locus_tag", "note", "positions", "codon_start_position", "translation_table", "product") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);'
    
    values= (protein_dict['protein_ncbi_id'], 
                       organism_ID, 
                       protein_dict['gene_name'],
                       protein_dict['locus_tag'],
                       protein_dict['note'],
                       protein_dict['position'],
                       protein_dict['codon_start_position'],
                       protein_dict['translate_table'],
                       protein_dict['product'])
    cur.execute(query,values)

    protein_id =  cur.lastrowid
    con.commit()
    con.close()
    return protein_id



#Insert protein sequence for a gene.
def insert_sequence(protein_dict:dict, protein_id, path) :
    con = sql.connect(path)
    cur = con.cursor()
    protein_ID = protein_id
    query= 'INSERT INTO "main"."Sequence" ("protein_ID", "translation") VALUES (?,?);'
    values= (protein_ID, protein_dict['translation'])
    cur.execute(query, values)
    
    con.commit()
    con.close()
    return 


#Create an organism
def create_organism(organism: dict, comments: dict , proteins: list, path): 
    
    organism_id= insert_organism (organism, path)
    insert_comments (comments, organism_id, path)
    
    for protein in proteins:
        protein_id = insert_protein(protein, organism_id, path)
        insert_sequence(protein, protein_id, path)
        
    return
  
    

def delete_database(path):
    con = sql.connect(path)
    cur = con.cursor()
    query1= 'DELETE  FROM Organism'
    query2= 'DELETE FROM Extended_comments'
    query3= 'DELETE FROM Protein'
    query4= 'DELETE FROM Sequence'
    cur.execute(query1)
    cur.execute(query2)
    cur.execute(query3)
    cur.execute(query4)
    
    con.commit()
    con.close()
    
    status = 0
    return status
  