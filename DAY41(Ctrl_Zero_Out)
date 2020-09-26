##########################################################################################################################################
################################################# CTRL_ZERO_OUT ##########################################################################
##########################################################################################################################################

#Run the script and click on the interface, it will zero out all the controls with suffix *Ctrl.
#(You can change the suffix to *Ctrl,*ctrl,*control according to your choice on line 14)
#OR
#Select all the controllers ignoring the suffix and run the script ,it will zero out all the selected controls

import pymel.core as pm
import maya.cmds as cmds 


selected_object = pm.selected()

if len(selected_object) == 0:
    obj_ending_with_Ctrl=pm.ls('*Ctrl',an=True)     #an=absolute name

    for obj in obj_ending_with_Ctrl:
        obj.setTranslation([0, 0, 0])
        obj.setRotation([0, 0, 0])
        obj.setScale([1, 1, 1])
else:
    for obj in selected_object:
        obj.setTranslation([0, 0, 0])
        obj.setRotation([0, 0, 0])
        obj.setScale([1, 1, 1])
