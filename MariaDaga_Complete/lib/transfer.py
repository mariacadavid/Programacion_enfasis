
import flatlayer  as flat 
import sqlitelayer as sql

        
        
def database_import(db_path, gbff_path, verbose_mode)->dict:
    
    filelist = flat.get_flatfile_list(gbff_path)
    
    count= 0
    for file in filelist:
         if verbose_mode == "Y":
            print (file)
        
         file_handler= flat.get_gbff_file_handler(gbff_path, file)  #open file
         organism = flat.get_info_organism(file_handler)
         comments = flat.get_comments(file_handler)
         proteins = flat.get_prot(file_handler) 
         flat.close_gbff_file_handler(file_handler) #close file

         sql.create_organism(organism, comments, proteins, db_path) #load to database
         count += 1
         
 
    return count

