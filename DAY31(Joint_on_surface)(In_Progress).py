###############################################################################################################
#################################### Joint_On_Surface##########################################################
###############################################################################################################
#Author:Himanshi Ahuja
#Email:himansheeahuja@gmail.com

#Select (object/vertices/shape) and run the script.
#It will create joint on that position.






selected_obj = cmds.ls(sl=True)

create_cluster = cmds.cluster(selected_obj)
cmds.select(cl=True)   #clear selection

Joint = cmds.joint(n= (str(selected_obj[0])+'_Joint'))
cmds.delete(cmds.parentConstraint(create_cluster,Joint))
cmds.delete(create_cluster)

