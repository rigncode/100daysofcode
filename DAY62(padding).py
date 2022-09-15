#padding
a=cmds.ls(sl=True)
counter=0
for i in a:
    
    cmds.rename(i,i+'_'+str(counter))
    counter=counter+1
    print i
