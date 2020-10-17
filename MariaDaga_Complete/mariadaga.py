import os
import sys 
sys.path.append('./lib')
import transfer as orchestator
import sqlitelayer as sql



#read given arguments
def read_command_line_arguments(args: list) -> dict: 
    print(args)
    #Suficient arguments?
    if len(args) < 3:
        print ("Not sufficient arguments")
        
    #Is data base correct? 
    data_base_path = args[1]
    assert os.path.isfile(data_base_path) , "Database does not exist"
    
    #Is gbff file path correct? 
    gbff_files_path = args [2]
    assert os.path.isdir(gbff_files_path) , "Path for GBFF files does not exist"
    
    arguments= {}
    arguments.update ({"data_base_path":data_base_path})
    arguments.update ({"gbff_files_path":gbff_files_path})
    
    if len(args) > 3:
        verbose_mode = args[3]
        delete_mode= args[4] 
    
        arguments.update ({"verbose_mode":verbose_mode})
        arguments.update ({"delete_mode":delete_mode})
        
    else:
        arguments.update ({"verbose_mode":"N"})
        arguments.update ({"delete_mode":"N"})
          
    return(arguments)
     

    
def mariadaga(args): 
    arguments= read_command_line_arguments(args)
    
    if arguments['delete_mode'] == "Y": 
       sql.delete_database(arguments['data_base_path'])  
    
    else: 
        print("delete_mode = N")
       
    count= orchestator.database_import(arguments['data_base_path'],arguments['gbff_files_path'], arguments['verbose_mode'])  
    
    print(count, "files successfully processed")
    print("import finished")
    print("Process ended")
    

#Argumentos deben ser llamados asi= mariadaga.py, data_base_path, gbff_files_path, verbose_mode, delete_mode
if __name__ == "__main__":
    import sys 
    mariadaga(sys.argv)
