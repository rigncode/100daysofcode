import maya.cmds as cmds
import pymel.core as pm
#Take 4 objects,randomly placed and lock one object's attribute.

#Statement01
selected_obj=pm.ls(sl=True)

for i in selected_obj:
   	pm.xform(i,t=(5,3,5))




#Statement02
selected_obj=pm.ls(sl=True) 
for i in selected_obj:
	try:
		pm.xform(i,t=(5,3,5))
	except:
		print(i+'Encountered a problem while moving')



#Statement03
selected_obj=pm.ls(sl=True)
try:
    pm.move(3,1,5)
except:
    pass
