##################################################################################
############################## FK_CHAIN ##########################################
##################################################################################

#Author:Himanshi Ahuja
#Email:himansheeahuja@gmail.com

#Select a joint and run the script.
#(It will make controllers with offset group on every joint in the hierarchy including their connctions)
import maya.cmds as cmds
def fk_controller_setup():
    JointChain=cmds.ls(selection=True)
    JointRel=cmds.listRelatives(JointChain,ad=True)
    JointRel.reverse()
    JointHr=JointChain+JointRel
    
    ctrlGrpList=[]
    ctrlList=[]
    
    for i in JointHr:
        name=i.replace('_Joint','')
        ctrl=cmds.circle(n=(name+'_Ctrl'),ch=0)
        cmds.delete(cmds.parentConstraint(i,ctrl))
        cmds.parentConstraint(ctrl,i)
        groupOffset=cmds.group(ctrl,n=(name+'_Offset'))
        groupExtra=cmds.group(groupOffset,n=(name+'_Extra'))
        ctrlList.append(ctrl[0])
        ctrlGrpList.append(groupExtra)    
       
     
    #st=cmds.ls('*_Ctrl',)
    #ctrlList=cmds.ls('*_Ctrl', p=1)   josh sobel
    noofjnts=len(groupExtra)
    
    
    
    for i in range (0,noofjnts):
        cmds.parent(ctrlGrpList[i+1],ctrlList[i])
        
        
        
        
fk_controller_setup()
