#Adding suffix to your selected objects

def add_suffix(suffix):
    
    selected_object=cmds.ls(selection=True)
    print selected_object
    for obj in selected_object:
        print obj
        renaming=cmds.rename(obj,obj+'_'+suffix)
        
        

        
      
add_suffix('trainnnn')    
