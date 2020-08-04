#######################################################################################################
################################ OVERRIDE COLOR  ######################################################
#######################################################################################################

#Name=Himanshi Ahuja
#email- himansheeahuja@gmail.com


#Select all the controllers and run the script.
#You can change the value of color in the last line.

import maya.cmds as cmds
Selected_Obj=cmds.ls(selection=True)
Shape_Nodes=cmds.listRelatives(Selected_Obj,shapes=True)
print Shape_Nodes

for shape in Shape_Nodes:

	cmds.setAttr (shape+'.overrideEnabled',1)
	cmds.setAttr(shape+'.overrideColor',15) 

