sel_object=cmds.ls(tr=True,shapes=True)

for obj in sel_object :
    a=cmds.toggle(obj,query=True,la=True)
    if a==True:
        cmds.setAttr(obj+'.displayLocalAxis',False)
    


cmds.toggle(la=True)  
