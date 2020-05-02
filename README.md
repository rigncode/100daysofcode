# 100DaysOfCode

**RULES**

Code atleast for 1hour everyday for the next 100 Days.
Post your progress on insta/twitter/github.
Don't forget to write what you have learnt each day.

**TARGETS-** 
Qaudraped
Studying UI
Learning functions,classes,loops,OOP
Skinning Tool
basic fk chain
Prop Tool
Mirrioring Tool
MAKE YOUR OWN CTRL SETUP SCRIPT



**DAY1, 01'MAY'20**

**Project**:  *QUADRAPED*

**Progress**: I have made the basic placement of LOCATORS for entire rig which will help in setting up the joints.

**Points To Ponder**: 
1) You can change the **color of a ctrl** using cmds.setAttr(y+'.overrideEnabled',1)
                                            cmds.setAttr(y+'.overrideColor',15)
                                            
                                            
2) Instead of repeating these commands for every ctrl,you can define a funct.
def bluecol(y):
       cmds.setAttr(y+'.overrideEnabled',1)
       cmds.setAttr(y+'.overrideColor',15)
       
hindToe=cmds.spaceLocator(n='L_Loc_hindToe')
cmds.setAttr(hindToe[0]+'.translateX',12)
blueCol(hindToe[0]) 
y will be replaced by hindToe[0].


3)[u'nurbsCircle1',u'makeNurbCircle1']- there are 2 nodes in maya. **TRANSFORM NODE**(1st one) is used to interact/alter with maya viewport.
  It is denoted using [0] since it is the first item of the list.
  
  Joint doesn't have two nodes.
       
       
**DAY2,   02'MAY'20**

**Project**: *QUADRAPED*


**Progress**: Using the locators I have made joint setup of front and hind(back)joints of one side then mirrored them.
          I have also made FK and IK joint setup by duplicating the previous setup.
          
          
**Points To Ponder** :
1) **JOINT SETUP** can be done in two ways.
a) You can put parent constrain btw locators and joints and then deleting the constraint. JOINT and LOCATOR will be on the same place.
b) You can usse **xform** command to get the information about position of locator and then put it in the position of the jnt in jnt      command.
posAnkle=cmds.xform(Ankle,q=1,t=1,ws=1)
L_AnkleJnt=cmds.joint(p=posAnkle,n='L_jnt_Ankle')

2) **getAttr** command
I duplicated the L_jnt then used getAttr to take out the position and then put it in the setAttr of R_jnt.

3) **Orientation** command
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
       
       
       
                                            
