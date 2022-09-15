#local Axis UI


import maya.cmds as cmds

def window_creation():
    
    if cmds.window('Lc',exists=True):
        cmds.deleteUI('Lc')
        
    windowbox=cmds.window('Lc',title='AxisDisplay',h=400,w=200,s=False)
    cmds.columnLayout()
 
      
    menu= cmds.optionMenu('Mode', h=20,ann=('Display local axis'))
    a= cmds.menuItem('On',l='ON')
    b= cmds.menuItem('Off',l='OFF')

    cmds.button('btnObj',label='Scene',c= ('display01()'), bgc=(0.011,0.259,0.225))
    
    
    #####################################################################################################3
    menu02 = cmds.optionMenu('JointDisplayMode', h=20,ann=('Display local axis'))
    a02= cmds.menuItem('On',l='ON')
    b02= cmds.menuItem('Off',l='OFF')

    cmds.button('btnObj02',label='Joint',c= ('display02()'), bgc=(0.011,0.259,0.225))
    cmds.showWindow()


    
def display01():
    
    
    sel_object=cmds.ls(sl=True,tr=True)
    print sel_object
    if len(sel_object)>0:
        Opt= cmds.optionMenu('Mode',query=True,select=True)
        print Opt
        if Opt == 1:
            for obj in sel_object :
                result=cmds.toggle(obj,query=True,la=True)
                print result
                if result==False:
                    cmds.setAttr(obj+'.displayLocalAxis',True)
                else:
                    pass    
        else:
            if Opt == 2:
                for obj in sel_object :
                    result=cmds.toggle(obj,query=True,la=True)
                    if result==True:
                        cmds.setAttr(obj+'.displayLocalAxis',False)
                    else:
                        pass
                    
    else:
                      
        sel_object=cmds.ls(tr=True)
        print sel_object
        
        Opt= cmds.optionMenu('Mode',query=True,select=True)
        print Opt
        if Opt == 1:
            for obj in sel_object :
                result=cmds.toggle(obj,query=True,la=True)
                print result
                if result==False:
                    cmds.setAttr(obj+'.displayLocalAxis',True)
                else:
                    pass    
        else:
            if Opt == 2:
                for obj in sel_object :
                    result=cmds.toggle(obj,query=True,la=True)
                    if result==True:
                        cmds.setAttr(obj+'.displayLocalAxis',False)
                    else:
                        pass       
                        
def display02():
    selected_object02=cmds.ls(sl=True,type='joint')
    print selected_object02
   
    
    if len(selected_object02)>0:
        Opt02= cmds.optionMenu('JointDisplayMode',query=True,select=True)
        print Opt02
        if Opt02 == 1:
            for obj02 in selected_object02 :
                result=cmds.toggle(obj02,query=True,la=True)
                print result
                if result==False:
                    cmds.setAttr(obj02+'.displayLocalAxis',True)
                else:
                    pass    
        else:
            if Opt02 == 2:
                for obj02 in selected_object02 :
                    result=cmds.toggle(obj02,query=True,la=True)
                    if result==True:
                        cmds.setAttr(obj02+'.displayLocalAxis',False)
                    else:
                        pass
                    
    else:
                      
        selected_object03=cmds.ls(type='joint')
        print selected_object03
        
        Opt02= cmds.optionMenu('JointDisplayMode',query=True,select=True)
        print Opt02
        if Opt02 == 1:
            for obj02 in selected_object03 :
                result=cmds.toggle(obj02,query=True,la=True)
                print result
                if result==False:
                    cmds.setAttr(obj02+'.displayLocalAxis',True)
                else:
                    pass    
        else:
            if Opt02 == 2:
                for obj02 in selected_object03 :
                    result=cmds.toggle(obj02,query=True,la=True)
                    if result==True:
                        cmds.setAttr(obj02+'.displayLocalAxis',False)
                    else:
                        pass     
        
        

window_creation()



