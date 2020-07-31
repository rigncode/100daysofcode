
############### FK Arm##############3
import pymel.core as pm
import maya.cmds as cmds

def shapeBuilderUI():

    if cmds.window('Win' ,exists=True):
       cmds.deleteUI('Win')
        
    if cmds.windowPref('Win', exists=True ):
       cmds.windowPref( 'Win', r=True )
       
    cmds.window('Win',title='FK Setup',s=0,h=600,w=300)
    cmds.showWindow('Win') 
    
    form = cmds.formLayout('form01',bgc =[(.179),(.179),(.189)],w=300,h=600)   
    
    
    cmds.text('Text_Joints',l='<font size = 4>Number Of Joints')
    cmds.intField('intField_Jnts',w=240,h=25)
    cmds.separator('S01')
    cmds.button('Button_CreateJnts',l='Create Joints',w=150,h=25,bgc=[(.2),(.5),(.4)],c='createJoints()')
    ######################################################################################
    cmds.text('txtOrient',l='ORIENT JOINTS')
    cmds.checkBox('bxyz',label='XYZ')
    cmds.checkBox('bzxy',label='ZXY')
    cmds.checkBox('byzx',label='YZX')
    cmds.button('Button_OrientJnts',l='Orient Joints',w=150,h=25,bgc=[(.2),(.5),(.4)],c='orientJoints()')
    ########################################################################
    cmds.text('textCtrl',l='<font size = 3>CONTROLLER')
    cmds.optionMenu('OptMenu', h=20,ann=('It will create the controller'),bgc=[(.2),(.5),(.4)])
    cmds.menuItem('CubeMenu',l='Cube')
    cmds.menuItem('CircleMenu',l='Sphere')
    cmds.menuItem('SquareMenu',l='Square')
    
    #######################################################################
    cmds.text('txtSize',l='<font size = 3>CONTROLLER SIZE')
    cmds.intSliderGrp('sizeSlider',l='Size',min=1,f=True,w=365)
    ###############################################################
    cmds.text('txtColor',l='<font size = 3>CONTROLLER COLOR')
    cmds.colorIndexSliderGrp('colorSlider', label='Color', min=0, max=20, value=10 )
    ##################################################
    cmds.text('Text_Suffix',l='<font size = 3>SUFFIX')
    cmds.textField('txtF',w=240,h=25)
    
    
    ######################################3
    cmds.button('Button_FkChain',l=' Build FK_Chain',c='fkSetup()',bgc=[(.057),(.074),(.1)],h=38,w=75)
    cmds.button('Button_IkChain',l=' Build IK_Chain',c='IkSetup()',bgc=[(.057),(.074),(.1)],h=38,w=75)
    cmds.button('Button_Fk_IK_Chain',l=' Build FK_IkChain',c='fk_IkSetup()',bgc=[(.057),(.074),(.1)],h=38,w=75)
    
    cmds.formLayout('form01',edit=True,attachForm=[('Text_Joints','top', 13),
    ('Text_Joints','left',98),
    ('intField_Jnts','left',30),
    ('Button_CreateJnts','left',34),
    ('Button_CreateJnts','right',30),
    ('txtOrient','left',30),
    ('txtOrient','right',30),
    ('bxyz','left',32),
    ('Button_OrientJnts','left',30),
    ('Button_OrientJnts','right',30),
    
    
    ('textCtrl','right',30),
    ('textCtrl','left',30),
    ('OptMenu','right',30),
    ('OptMenu','left',30),
    
    ('txtSize','right',30),
    ('txtSize','left',30),
    ('sizeSlider','left',-87),
    ('colorSlider','left',-87),
    ('txtColor','left',30),
    ('txtColor','right',30),
    ('Text_Suffix','right',30),
    ('Text_Suffix','left',30),
    ('Button_FkChain','left',30),
    ('txtF','left',30),
    
    ],
    
    attachControl=[('intField_Jnts','top',8,'Text_Joints'),                      
    ('Button_CreateJnts','top',5,'intField_Jnts'),
    ('txtOrient','top',12,'Button_CreateJnts'),
    ('bxyz','top',11,'txtOrient'),
    ('bzxy','top',11,'txtOrient'),
    ('byzx','top',11,'txtOrient'),
    ('Button_OrientJnts','top',10,'bzxy'),
    ('textCtrl','top',5,'Button_OrientJnts'),
    ('OptMenu','top',10,'textCtrl'),
    ('txtSize','top',10,'OptMenu'),
    ('sizeSlider','top',10,'txtSize'),
    ('txtColor','top',10,'sizeSlider'),
    ('colorSlider','top',10,'txtColor'),
    ('Text_Suffix','top',10,'colorSlider'),
    ('txtF','top',10,'Text_Suffix'),
    ('Button_FkChain','top',14,'txtF'),
    ('Button_IkChain','top',14,'txtF'),
    ('Button_Fk_IK_Chain','top',14,'txtF'),
    
    ('bzxy','left',56,'bxyz'),
    ('byzx','left',56,'bzxy'),
    ('Button_IkChain','left',5,'Button_FkChain'),
    ('Button_Fk_IK_Chain','left',5,'Button_IkChain')
    
    
    
    
    
    ])
    

    

###############################################################################    
##                        Creating Functions                                ###               
###############################################################################




#Function for creating joints
    
def createJoints():
	jntList=[]
	Jnts=cmds.intField('intField_Jnts',query=True,value=True)
	for i in range(Jnts):
		number = i+1
		a=pm.joint(n = 'Tmp_0'+str(number)+'_Jnt')
		pm.xform(t=(1,0,0))
		jntlist.append(a)		
		
def orientJoints():
    cmds.checkBox('bxyz',label='XYZ',q=True,value=True,sl=True) 
        
    for i in range(a):
        cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)	
        
        

        
        	
		
		
shapeBuilderUI()		
