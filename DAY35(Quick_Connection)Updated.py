###############################################################################################################
##################################### QUICK_CONNECTION ########################################################
###############################################################################################################


#Author:Himanshi Ahuja
#Email:himansheeahuja@gmail.com

import maya.cmds as cmds
import maya.mel as mel
import pymel.core  as pm

def quick_connection():
            
    if cmds.window('QuickConnction', exists=True ):
        cmds.deleteUI( 'QuickConnction', window=True)
    if cmds.windowPref('QuickConnction', exists=True ):
        cmds.windowPref( 'QuickConnction', r=True )
    
    cmds.window('QuickConnction', title='Quick Connection', iconName='Short Name', widthHeight=(336,260),s=0 )
    
    form = cmds.formLayout(numberOfDivisions=100,bgc =[(.284),(.284),(.284)],w=336,h=260)
    driver = cmds.textField('drivertxf',w=150,h=40)
    
    driven = cmds.textScrollList('asd',h=40,w=150)
    
    driverButton = cmds.button(l='Driver',w=150,h=35,bgc =[(.394),(.394),(.394)],c='createDriver()')
    drivenButton = cmds.button(l='Driven',w=150,h=35,bgc =[(.394),(.394),(.394)],c='createDriven()')
    connectRotate = cmds.button(l='Connect Rotate',w=310,bgc =[(.2),(.5),(.4)],h=25,c='create_rotate_connection()')
    connectTranslate = cmds.button(l='Connect Translate',w=310,bgc =[(.2),(.5),(.4)],h=25,c='create_translate_connection()')
    connectScale = cmds.button(l='Connect Scale',w=310,bgc =[(.2),(.5),(.4)],h=25,c='create_scale_connection()')
    author = cmds.symbolButton(i='UV_Freeze_Tool.png',c='author()')
    deleteButton=cmds.button(l='Delete Connections',w=310,h=25,bgc =[(0.4),(0.5),(2)],c='delete_connections()')
    
    cmds.formLayout(form,edit=True,attachForm=[
    (driver,'top',17),
    (driven,'top',17),
    (driverButton,'top',65),
    (drivenButton,'top',65),
    (author,'bottom',2),
    
    
    
    (driver,'left',12),
  (driven,'left',12),
    (driverButton,'left',12),
    (drivenButton,'left',12),
    (connectRotate,'left',12),
    (connectTranslate,'left',12),
    (connectScale,'left',12),
    (deleteButton,'left',12),
    (author,'left',151)
    
            
            
            
            	
    
    
    
    
    
    
    ],
    attachControl=[
    
    (driven, 'left', 10, driver), 
    (driverButton, 'bottom', 20, driver), 
    (drivenButton, 'left', 10, driverButton),
    (connectTranslate,'top',7,connectRotate),
    (connectScale,'top',7, connectTranslate),
    (connectRotate,'top',14,driverButton),
    (deleteButton,'top',7,connectScale) 
     
    
    
    
    
        	
        	
    
    ]
    
    
    
    
    
    
    
    )
            
            
            
            
    cmds.showWindow('QuickConnction')
        
DriverVar = []
DrivenVar = []


def createDriver():
    Sel = cmds.ls(sl=True)
    SlSize=len(Sel)
    if SlSize==1:
        print (str(Sel[0]) + ' will be the driver ')
        cmds.textField('drivertxf',e=True,tx=str(Sel[0]),ed=0)
        DriverVar.append(Sel[0])
    else:
        print 'More than one parent Selected'
             



def createDriven():
    cmds.textScrollList('asd',e=True,ra=True)
    Selc = cmds.ls(sl=True)
    try:
        for i in Selc:
            cmds.textScrollList('asd',e=True,a=i)
            DrivenVar.append(i)
            print (i+' Driven')
            
            
    except:
        print 'No children Selected'   
    
        
def create_rotate_connection():

    for i in DrivenVar:
        
        
       
        drivenpy = pm.PyNode(str(i))
        driverpy = pm.PyNode(DriverVar[0])
    
        driverpy.rotate>>drivenpy.rotate
        
        
def create_translate_connection():
    
    for i in DrivenVar:
        drivenpy = pm.PyNode(i)
        driverpy = pm.PyNode(DriverVar[0])
        
        driverpy.translate>>drivenpy.translate

        
def create_scale_connection():
    
    for i in DrivenVar:
        drivenpy = pm.PyNode(i)
        driverpy = pm.PyNode(DriverVar[0])
        
        driverpy.scale>>drivenpy.scale        
        

def delete_connections():
    
    for i in DrivenVar:
        drivenpy = pm.PyNode(i)
        driverpy = pm.PyNode(DriverVar[0])
        try:
            driverpy.scale.disconnect(drivenpy.scale)
        except:
            pass
            
        try:
            driverpy.rotate.disconnect(drivenpy.rotate)
        except:
            pass
            
            
        try:
            driverpy.translate.disconnect(drivenpy.translate)
        except:
            pass
    
 
    

        
    

def author():
    cmds.launch(web='https://www.instagram.com/rig_n_code/') 
  
  
quick_connection()
