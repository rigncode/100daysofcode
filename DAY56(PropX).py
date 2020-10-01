import maya.cmds as cmds
import maya.mel as mel

#function for creating offset group
def create_group(obj):
    cmds.select(cl=True)
    offset = cmds.group(n=str(str(obj) + '_Offset_Group'),em = True)
    extra= cmds.group(em=True)
    cmds.delete(cmds.parentConstraint(str(obj),extra))
    extra_pos = cmds.xform(extra, q=True, t=True, ws=True)
    extra_rotn = cmds.xform(extra, q=True, rotation=True, ws=True)
    cmds.xform(offset, translation=extra_pos, ws=True)
    cmds.xform(offset, rotation=extra_rotn, ws=True)
    cmds.makeIdentity(offset, apply=True, t=1, r=1, s=1 )
    cmds.parent(obj,offset)
    cmds.delete(extra)
    return offset
    
    
#function for UI    
def ui():
    if cmds.window('Win',exists=True):
        cmds.deleteUI('Win')
    if cmds.windowPref('Win',exists=True):
        cmds.windowPref('Win',r=True)    
        
    cmds.window('Win',title='PropX',h=110)
    form = cmds.formLayout('form01',bgc =[(.190),(.194),(.194)],h=110)
    
    Loc_text=cmds.text(l="Step01 :create Locator and use it as object's pivot.")
    Rig_text=cmds.text(l="Step02 :select the mesh and click on 'Create Rig' button.")
    
    Loc_Button=cmds.button(l='Create Locator',bgc=[(.2),(.5),(.4)],c='loc=cmds.spaceLocator()',w=200)
    Rig_Button=cmds.button(l='Create Rig',bgc=[(.2),(.5),(.4)],c='create_rig()',w=200)
    
    S01=cmds.separator(h=10,style='in',w=300)
    
    
    
    cmds.formLayout('form01',edit=True,attachForm=[(Loc_text,'top',6),
    (Loc_Button,'top',23),
    (S01,'top',49),
    (Rig_text,'top',58),
    (Rig_Button,'top',76),
    ])
    cmds.showWindow()

#Setting up the rig
def create_rig():
    selected_obj = cmds.ls(sl=True)
    
    if (len(selected_obj)==0):
        cmds.inViewMessage( amg='Please select Mesh to create a <hl>Prop Rig</hl>.', pos='botCenter', fade=True)
        
        
    else:
        locator_pos = cmds.xform(loc, q=True, t=True, ws=True)  #locator position) 
        innerCtrl = cmds.circle(r = 60,n=('Ctrl'))    #made inner ctrl
        cmds.setAttr('Ctrl.rotateX',90)
        innerCtrlGrp = create_group(str(innerCtrl[0]))      #create offset grp on ctrl
        cmds.xform(innerCtrl[0], translation=locator_pos, ws=True) #set inner ctrl on locator position
        cmds.makeIdentity(innerCtrl[0], apply=True, t=1, r=1, s=1 ) #freeze inner ctrl
        
        jnt = cmds.joint(n=('Joint'))    #create jnt
        cmds.xform(jnt, translation=locator_pos, ws=True)  #set jnt on locator position
        jointGrp = create_group(str(jnt))  #create offset grp on jnt
        
        cmds.parentConstraint(innerCtrl,jointGrp,mo=True)   #constrain innerctrl with jnt offset grp
        
        
        #create global ctrl,rename it,make offset grp 
        global_ctrl = mel.eval("curve -d 1 -p -5 0 0 -p -3 0 -2 -p -3 0 -1 -p -1 0 -1 -p -1 0 -3 -p -2 0 -3 -p 0 0 -5 -p 2 0 -3 -p 1 0 -3 -p 1 0 -1 -p 3 0 -1 -p 3 0 -2 -p 5 0 0 -p 3 0 2 -p 3 0 1 -p 1 0 1 -p 1 0 3 -p 2 0 3 -p 0 0 5 -p -2 0 3 -p -1 0 3 -p -1 0 1 -p -3 0 1 -p -3 0 2 -p -5 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 ;")
        
        global_ctrl_NN = cmds.rename(global_ctrl,('Global_Ctrl'))
        global_ctrl_NN_Grp = create_group(str(global_ctrl_NN))
        cmds.setAttr('Global_Ctrl.scale',20,20,20)
        cmds.makeIdentity(global_ctrl_NN, apply=True, t=1, r=1, s=1 )

        try:
            sknCls = cmds.skinCluster(jnt,selected_obj)
        except:
            cmds.warning( 'select a mesh first')
            print 'select a mesh first'
             
        #organising   
        cmds.parent(innerCtrlGrp,global_ctrl_NN)
        world_grp = cmds.group(global_ctrl_NN_Grp,jointGrp)
        world_grp_NN = cmds.rename(world_grp,('World'))

        geoGrp = cmds.group(selected_obj)
        geoGrpNN = cmds.rename(geoGrp,('Geo'))
        cmds.parent(geoGrpNN,world_grp_NN)
        cmds.delete(loc) 
        
        #creating attributes
       
            
        cmds.addAttr('Global_Ctrl' ,longName="GlobalScale" ,at= "float",defaultValue= 1.0,minValue= 0,k=1,dv=1)
        cmds.addAttr('Global_Ctrl',longName= "Mesh_Display",at= "enum",en= "Normal:Template:Reference")
        cmds.addAttr('Global_Ctrl',longName= "Ctrl_Visibility",at="bool",k= 1,dv=1)
        cmds.addAttr('Global_Ctrl',longName= "Mesh_Visibility",at= "bool",k= 1,dv=1)
    

        cmds.setAttr('Global_Ctrl'+".Mesh_Display",keyable=False,channelBox= True) 
        
        cmds.connectAttr('Global_Ctrl'+'.Ctrl_Visibility',innerCtrlGrp+'.visibility',f=True)
        cmds.connectAttr('Global_Ctrl'+'.Mesh_Visibility',geoGrpNN+'.visibility',f=True)
        cmds.setAttr("Geo.overrideEnabled",1)
        cmds.connectAttr('Global_Ctrl'+'.Mesh_Display','Geo'+'.overrideDisplayType')
        cmds.connectAttr('Global_Ctrl'+'.GlobalScale','Global_Ctrl'+'.scaleX')
        cmds.connectAttr('Global_Ctrl'+'.GlobalScale','Global_Ctrl'+'.scaleY')
        cmds.connectAttr('Global_Ctrl'+'.GlobalScale','Global_Ctrl'+'.scaleZ')


ui()
