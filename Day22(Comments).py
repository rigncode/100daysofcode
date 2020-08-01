#This function is used to constrain objects
def constrain():
    
    #Find the item selected in our Text Scroll List
    tsl_item = cmds.textScrollList("myList", q=True, si=True)
    
    #If "Maintain Offset" IS checked, apply the constraint WITH "Maintain Offset"
    if cmds.checkBox("myChBx", q=True, v=True) == 1:
        #This line checks if "Parent Constrain" is selected in our Text Scroll List
        if tsl_item[0] == "Parent Constrain":
            cmds.parentConstraint(mo=True)
    
    #If "Maintain Offset" is NOT checked, apply the constraint WITHOUT "Maintain Offset"
    else:
        if tsl_item[0] == "Parent Constrain":
            
            cmds.parentConstraint()
            
    if cmds.checkBox("myChBx", q=True, v=True) == 1:
        if tsl_item[0] == "Orient Constrain":
            cmds.orientConstraint(mo=True)
    else:
        if tsl_item[0] == "Orient Constrain":
            cmds.orientConstraint()
