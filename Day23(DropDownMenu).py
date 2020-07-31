import maya.cmds as cmds


if cmds.window('Win',exists=True):
    cmds.deleteUI('Win')
    
cmds.window('Win',title='Shape Builder',h=300,w=600)
cmds.showWindow('Win')
cmds.columnLayout('Lyt')

cmds.separator(h=20)

Obj = cmds.optionMenu('Object', h=20,ann=('It will create the object'))
a= cmds.menuItem('cubeMenu',l='Cube')
b= cmds.menuItem('sphereMenu',l='Sphere')

cmds.button('btnObj',label='Create Object',c= ('createObj()'), bgc=(0.011,0.259,0.225))


    
def createObj():
    Opt= cmds.optionMenu('Object',query=True,select=True)
    if Opt == 1:
       cmds.polyCube()
    else:
        pass
      
    if Opt==2:
        cmds.polySphere()
    else:
        pass        
        
createWindow()

#########################################################
##                  ALTERNATIVE FOR LINE 18 TO 28      ##                             ##
#########################################################
#def createObj():
#    Opt= cmds.optionMenu('Object',query=True,select=True)
#    if Opt == 1:
#       cmds.polyCube()
#    else:
#        cmds.polySphere()
