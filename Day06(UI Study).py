
import maya.cmds as cmds

if cmds .window('Jnt_Win',ex=True) :
   cmds.deleteUI('Jnt_Win' , window=True)

if cmds.windowPref('Jnt_Win',exists=True):
    cmds.windowPref('Jnt_Win',r=True)



cmds.window('Jnt_Win',t='Joint_Setup',w=20,h=20,s=False) 

cmds.columnLayout('c_layout',adj=True)

cmds.separator()

cmds.text('DEFINE YOUR JOINT(S)')

cmds.separator()

cmds.textFieldGrp('jntName',label='Name Prefix Of Prefix:')
cmds.textFieldGrp('jntAmount',label='Amount Of Joints:')
cmds.textFieldGrp('jntSpacing',label='Joint Spacing:')

cmds.separator()

cmds.text('CHOOSE AN ORIENTATION TO CREATE YOUR CHAIN')

cmds.separator()

cmds.button('b_xyz',label='XYZ',h=30,c='xyz()',p='c_layout',bgc=[(.057),(.074),(.1)])
cmds.separator(h=3)
cmds.button('b_zxy',label='ZXY',h=30,c='zxy()',p='c_layout',bgc=[(.057),(.074),(.1)])
cmds.separator(h=3)
cmds.button('b_yzx',label='yzx',h=30,c='yzx()',p='c_layout',bgc=[(.057),(.074),(.1)])


cmds.showWindow('Jnt_Win')
