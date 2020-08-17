name-Himanshi ahuja
email-himansheeahuja@gmail.com



#Select root joint and run thi script.
#It will zero out the orientation of all the end joints in your setup.
#Condition: your end jont should contain 'end' word in it.


import maya.cmds as cmds


Selected_joints = cmds.listRelatives(allDescendents=True, type='joint')


empty_list=[]
for i in Selected_joints:
	if 'end'in i.lower():
		empty_list.append(i)
		cmds.setAttr(i+'.jointOrientX',0)
        cmds.setAttr(i+'.jointOrientY',0)
        cmds.setAttr(i+'.jointOrientZ',0)
else:
    print'No End Joint found'
    
print empty_list 
