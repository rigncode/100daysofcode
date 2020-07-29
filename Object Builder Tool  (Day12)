#################################################################
######################    Object Builder    ########################
 #################################################################
#Author:Himnanshi Ahuja
#Email:himansheeahuja@gmail.com



#Copy&Run

import maya.cmds as cmds
import maya.mel as mel
def ui():
    if cmds.window('Win',exists=True):
        cmds.deleteUI('Win')
        
    if cmds.windowPref('Win',exists=True):
       cmds.windowPref('Win',r=True)
        
    cmds.window('Win',title='OBJECT BUILDER',h=300,w=150)
    cmds.showWindow('Win')
    
    cmds.columnLayout('Lyt',adj=True)  #(adj=adjustable Column)
    cmds.text(l='Input The  Amount')
    cmds.intField('intFCube')  #where you can type integers)
    #this will create a button,c=command,that button will give this commnand)
    cmds.button ('BtnCube',label='Cube', c='createCube()',bgc =[(.2),(.5),(.4)])  
    cmds.separator(h=8)
    
    cmds.intField('intFSphere')
    cmds.button('BtnSphere',label='Sphere',c='createSphere()',bgc =[(.2),(.5),(.4)])
    cmds.separator(h=8)
    
    
    cmds.intField('intFCylinder')
    cmds.button('BtnCylinder',label='Cylinder',c='createCylinder()',bgc =[(.2),(.5),(.4)])
    cmds.separator(h=8)
    
    cmds.intField('intFCone')
    cmds.button('BtnCone',label='Cone',c='createCone()',bgc =[(.2),(.5),(.4)])
    cmds.separator(h=8)
     
     
    cmds.intField('intFPlane')
    cmds.button('BtnPlane',label='Plane',c='createPlane()',bgc =[(.2),(.5),(.4)])       
    cmds.separator(h=8)
    
    
    cmds.intField('intFTorus')
    cmds.button('BtnTorus',label='Torus',c='createTorus()',bgc =[(.2),(.5),(.4)])
    cmds.separator(h=20,ut=1)
    
    cmds.text ('txt',l='Object Size')
    cmds.intSliderGrp('sizeSlider',l='Size',f=True)
    cmds.button('BtnSize',label='Change Size',c='changeSize()')
    
  ######################Center Pivot ....Delete History....Freeze Transform#######################  
    cmds.button('BtnCP',label='Center Pivot',c='centerPivot()',bgc =[(0.002),(0.004),(.130)])
    cmds.separator(h=8)
    
    cmds.button('BtnDH',label='Delete History',c='deleteHistory()',bgc =[(0.002),(0.004),(.130)])
    cmds.separator(h=8)
    
    cmds.button('BtnFT',label='Freeze Transform',c='freezeTransform()',bgc =[(0.002),(0.004),(.130)])
    cmds.separator(h=8)
    
    author = cmds.symbolButton(i='UV_Freeze_Tool.png',c='author()')
    
    
    
   
#when I will click on the cube button.
#it will run this function.
#1) it will query the intField(it will get the information of what is typed in intField)
#then it will run the loop and make cube.    
def createCube():
    intFld_Cube=cmds.intField('intFCube',q=True,value=True)
   
    for i in range(intFld_Cube):
        cmds.polyCube(h=5,w=5,n=('Cube_'+str(i)))
    
def createSphere():
    intFld_Sphere=cmds.intField('intFSphere',q=True,value=True)
    
    for i in range (intFld_Sphere):
        cmds.polySphere(r=5,n=('Sphere_'+str(i)))
        
def createCylinder():
    intFld_Cylinder=cmds.intField('intFCylinder',q=True,value=True)
    
    for i in range(intFld_Cylinder):
        cmds.polyCylinder(r=3,h=5,n=('Cylinder_'+str(i)))
        
def createPlane():
    intFld_Plane=cmds.intField('intFPlane',q=True,value=True)
    
    for i in range(intFld_Plane):
        cmds.polyPlane(h=5,n=('Plane_'+str(i)))     
        
        
def createCone():
    intFld_Cone=cmds.intField('intFCone',q=True,value=True)
    
    for i in range(intFld_Cone):
        cmds.polyCone(n=('Cone_'+str(i)))
        
        
def createTorus():
    intFld_Torus=cmds.intField('intFTorus',q=True,value=True)
    
    for i in range(intFld_Torus):
        cmds.polyTorus(r=3,n=('Torus_'+str(i)))
        
def changeSize():
    isgQ=cmds.intSliderGrp('sizeSlider',query=True,value=True)
    
    for i in range(isgQ):
        cmds.scale(isgQ,isgQ,isgQ)    
      
        
def centerPivot():   
    cmds.xform (cpc=True)
    
def deleteHistory():
    cmds.delete(ch=True)  
    
def freezeTransform():
    cmds.makeIdentity(apply=True,t=1,r=1,s=1)  
    
def author():
    cmds.launch(web='https://www.instagram.com/rig_code/')                                  
               
    
ui()
