import maya.cmds as cmds
import maya .mel as mel


#DEFINING FUNCTIONS for changing the  color of controllers.

def redCol(Y):                           #defining function)
    cmds.setAttr(y+'.overrideEnabled',1)     #Object.attribute,amount)
    cmds.setAttr(y+'.overrideColor',13)

def blueCol(y):
    cmds.setAttr(y+'.overrideEnabled',1)
    cmds.setAttr(y+'.overrideColor',15)

def yellowCol(y):
    cmds.setAttr(y+'.overrideEnabled',1)
    cmds.setAttr(y+'.overrideColor',17)

 #''''''CREATING LOCATORS''''''''

#Left Hind Locators

hindToe=cmds.spaceLocator(n='L_Loc_hindToe')
cmds.setAttr(hindToe[0]+'.translateX',12)
cmds.setAttr(hindToe[0]+'.translateZ',-20)
blueCol(hindToe[0])                   #calling function,y will be replaced by hindToe[0] 

hindAnkle=cmds.spaceLocator(n='L_Loc_hindAnkle')
cmds.setAttr(hindAnkle[0]+'.translateX',12)
cmds.setAttr(hindAnkle[0]+'.translateY',5)
cmds.setAttr(hindAnkle[0]+'.translateZ',-23)
blueCol(hindAnkle[0])

hindKnee=cmds.spaceLocator(n='L_Loc_hindKnee')
cmds.setAttr(hindKnee[0]+'.translateX',12)
cmds.setAttr(hindKnee[0]+'.translateY',25)
cmds.setAttr(hindKnee[0]+'.translateZ',-28)
blueCol(hindKnee[0])

hindUpperKnee=cmds.spaceLocator(n='L_LOC_hindUpperKnee')
cmds.setAttr(hindUpperKnee[0]+'.translateX',12)
cmds.setAttr(hindUpperKnee[0]+'.translateY',36)
cmds.setAttr(hindUpperKnee[0]+'.translateZ',-19)
blueCol(hindUpperKnee[0])

hindFemur=cmds.spaceLocator(n='L_LOC_hindFemur')
cmds.setAttr(hindFemur[0]+'.translateX',12)
cmds.setAttr(hindFemur[0]+'.translateY',50)
cmds.setAttr(hindFemur[0]+'.translateZ',-25)
blueCol(hindFemur[0])

hindPelvis=cmds.spaceLocator(n='LOC_hindPelvis')
cmds.setAttr(hindPelvis[0]+'.translateY',54)
cmds.setAttr(hindPelvis[0]+'.translateZ',-24)
yellowCol(hindPelvis[0])

hindLocGrp=cmds.group(hindToe,hindAnkle,hindKnee,hindUpperKnee,hindFemur,hindPelvis,n='Hind_Locators')

# Left Front Leg Locators

frontToe=cmds.spaceLocator(n='L_Loc_frontToe')
cmds.setAttr(frontToe[0]+'.translateX',12)
cmds.setAttr(frontToe[0]+'.translateZ',24)
blueCol(frontToe[0])

frontAnkle=cmds.spaceLocator(n='L_Loc_frontAnkle')
cmds.setAttr(frontAnkle[0]+'.translateX',12)
cmds.setAttr(frontAnkle[0]+'.translateY',5)
cmds.setAttr(frontAnkle[0]+'.translateZ',21)
blueCol(frontAnkle[0])

frontKnee=cmds.spaceLocator(n='L_Loc_frontKnee')
cmds.setAttr(frontKnee[0]+'.translateX',12)
cmds.setAttr(frontKnee[0]+'.translateY',25)
cmds.setAttr(frontKnee[0]+'.translateZ',24)
blueCol(frontKnee[0])

frontUpperKnee=cmds.spaceLocator(n='L_Loc_frontUpperKnee')
cmds.setAttr(frontUpperKnee[0]+'.translateX',12)
cmds.setAttr(frontUpperKnee[0]+'.translateY',36)
cmds.setAttr(frontUpperKnee[0]+'.translateZ',18)
blueCol(frontUpperKnee[0])

frontFemur=cmds.spaceLocator(n='L_Loc_frontFemur')
cmds.setAttr(frontFemur[0]+'.translateX',12)
cmds.setAttr(frontFemur[0]+'.translateY',44)
cmds.setAttr(frontFemur[0]+'.translateZ',25)
blueCol(frontFemur[0])

frontPelvis=cmds.spaceLocator(n='Loc_frontPelvis')
cmds.setAttr(frontPelvis[0]+'.translateY',54)
cmds.setAttr(frontPelvis[0]+'.translateZ',20)
yellowCol(frontPelvis[0])

frontLocGrp=cmds.group(frontToe,frontAnkle,frontKnee,frontUpperKnee,frontFemur,frontPelvis,n='Front_Locators')

# Neck Locators

neckRoot=cmds.spaceLocator(n='Loc_NeckRoot')
cmds.setAttr(neckRoot[0]+'.translateY',48)
cmds.setAttr(neckRoot[0]+'.translateZ',30)
yellowCol(neckRoot[0])

neckEnd=cmds.spaceLocator(n='Loc_NeckEnd')
cmds.setAttr(neckEnd[0]+'.translateY',58)
cmds.setAttr(neckEnd[0]+'.translateZ',50)
yellowCol(neckEnd[0])

neckLocGrp=cmds.group(neckRoot,neckEnd,n='Neck_Locators')

#Tail Locators

tail1=cmds.spaceLocator(n='Loc_TailRoot')
cmds.setAttr(tail1[0]+'.translateY',54)
cmds.setAttr(tail1[0]+'.translateZ',-32)
yellowCol(tail1[0])

tail2=cmds.spaceLocator(n='Loc_tailEnd')
cmds.setAttr(tail2[0]+'.translateY',54)
cmds.setAttr(tail2[0]+'.translateZ',-62)
yellowCol(tail2[0])

tailLocGrp=cmds.group(tail1,tail2,n='Tail_Locators')



''' finalize placement loc module '''

mainLocGrp=cmds.group(tailLocGrp,neckLocGrp,frontLocGrp,hindLocGrp,n='Locators')


#'''''''''''''CREATING  HIND JOINTS'''''''

#Left HIND JOINTS
cmds.select(d=True)

posHindPelvis=cmds.xform(hindPelvis,q=1,t=1,ws=1)
hindPelvisJnt=cmds.joint(p=posHindPelvis,n='jnt_hindPelvis')
yellowCol(hindPelvisJnt)
cmds.select(d=True)


pos_L_HindToe=cmds.xform(hindToe,q=1,t=1,ws=1)
L_hindToeJnt=cmds.joint(p=pos_L_HindToe,n='L_jnt_hindToe')
yellowCol(L_hindToeJnt)
cmds.select(d=True)


posHindAnkle=cmds.xform(hindAnkle,q=1,t=1,ws=1)
L_hindAnkleJnt=cmds.joint(p=posHindAnkle,n='L_jnt_hindAnkle')
yellowCol(L_hindAnkleJnt)
cmds.select(d=True)

posHindKnee=cmds.xform(hindKnee,q=1,t=1,ws=1)
L_hindKneeJnt=cmds.joint(p=posHindKnee,n='L_jnt_hindKnee')
yellowCol(L_hindKneeJnt)
cmds.select(d=True)



posHindUpperKnee=cmds.xform(hindUpperKnee,q=1,t=1,ws=1)
L_hindUpperKneeJnt=cmds.joint(p=posHindUpperKnee,n='L_jnt_hindUpperKnee')
yellowCol(L_hindUpperKneeJnt)
cmds.select(d=True)


posHindFemur=cmds.xform(hindFemur,q=1,t=1,ws=1)
L_hindFemurJnt=cmds.joint(p=posHindFemur,n='L_jnt_hindFemur')
yellowCol(L_hindFemurJnt)
cmds.select(d=True)


#Mirroring HIND  joints to other side


R_hindToeJnt=cmds.duplicate(L_hindToeJnt,n='R_jnt_hindToe')   
xPos=cmds.getAttr(L_hindToeJnt+'.tx')
cmds.setAttr(R_hindToeJnt[0]+'.tx',-xPos)

R_hindAnkleJnt=cmds.duplicate(L_hindAnkleJnt,n='R_jnt_hindAnkle')
xPos=cmds.getAttr(L_hindAnkleJnt+'.tx')
cmds.setAttr(R_hindAnkleJnt[0]+'.tx',-xPos)

R_hindKneeJnt=cmds.duplicate(L_hindKneeJnt,n='R_jnt_hindKnee')
xPos=cmds.getAttr(L_hindKneeJnt+'.tx')
cmds.setAttr(R_hindKneeJnt[0]+'.tx',-xPos)

R_hindUpperKneeJnt=cmds.duplicate(L_hindUpperKneeJnt,n='R_jnt_hindUpperKnee')
xPos=cmds.getAttr(L_hindUpperKneeJnt+'.tx')
cmds.setAttr(R_hindUpperKneeJnt[0]+'.tx',-xPos)


R_hindFemurJnt=cmds.duplicate(L_hindFemurJnt,n='R_jnt_hindFemur')
xPos=cmds.getAttr(L_hindFemurJnt+'.tx')
cmds.setAttr(R_hindFemurJnt[0]+'.tx',-xPos)

#Parenting HIND joints

cmds.parent(L_hindToeJnt,L_hindAnkleJnt)
cmds.parent(L_hindAnkleJnt,L_hindKneeJnt)
cmds.parent(L_hindKneeJnt,L_hindUpperKneeJnt)
cmds.parent(L_hindUpperKneeJnt,L_hindFemurJnt)
cmds.parent(L_hindFemurJnt,hindPelvisJnt)
cmds.parent(R_hindToeJnt,R_hindAnkleJnt)
cmds.parent(R_hindAnkleJnt,R_hindKneeJnt)
cmds.parent(R_hindKneeJnt,R_hindUpperKneeJnt)
cmds.parent(R_hindUpperKneeJnt,R_hindFemurJnt)
cmds.parent(R_hindFemurJnt,hindPelvisJnt)

#Setting Orientation Of HIND joints

cmds.select(L_hindFemurJnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(R_hindFemurJnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(d=True)


#'''''''''''''CREATING  FRONT JOINTS'''''''

#Left  FRONT JOINTS
cmds.select(d=True)

posfrontPelvis=cmds.xform(frontPelvis,q=1,t=1,ws=1)
frontPelvisJnt=cmds.joint(p=posfrontPelvis,n='jnt_frontPelvis')
yellowCol(frontPelvisJnt)
cmds.select(d=True)


posfrontToe=cmds.xform(frontToe,q=1,t=1,ws=1)
L_frontToeJnt=cmds.joint(p=posfrontToe,n='L_jnt_frontToe')
yellowCol(L_frontToeJnt)
cmds.select(d=True)


posfrontAnkle=cmds.xform(frontAnkle,q=1,t=1,ws=1)
L_frontAnkleJnt=cmds.joint(p=posfrontAnkle,n='L_jnt_frontAnkle')
yellowCol(L_frontAnkleJnt)
cmds.select(d=True)

posfrontKnee=cmds.xform(frontKnee,q=1,t=1,ws=1)
L_frontKneeJnt=cmds.joint(p=posfrontKnee,n='L_jnt_frontKnee')
yellowCol(L_frontKneeJnt)
cmds.select(d=True)



posfrontUpperKnee=cmds.xform(frontUpperKnee,q=1,t=1,ws=1)
L_frontUpperKneeJnt=cmds.joint(p=posfrontUpperKnee,n='L_jnt_frontUpperKnee')
yellowCol(L_frontUpperKneeJnt)
cmds.select(d=True)


posfrontFemur=cmds.xform(frontFemur,q=1,t=1,ws=1)
L_frontFemurJnt=cmds.joint(p=posfrontFemur,n='L_jnt_frontFemur')
yellowCol(L_frontFemurJnt)
cmds.select(d=True)


#Mirroring FRONT  joints to other side


R_frontToeJnt=cmds.duplicate(L_frontToeJnt,n='R_jnt_frontToe')
xPos=cmds.getAttr(L_frontToeJnt+'.tx')
cmds.setAttr(R_frontToeJnt[0]+'.tx',-xPos)   

R_frontAnkleJnt=cmds.duplicate(L_frontAnkleJnt,n='R_jnt_frontAnkle')    
xPos=cmds.getAttr(L_frontAnkleJnt+'.tx')    
cmds.setAttr(R_frontAnkleJnt[0]+'.tx',-xPos)

R_frontKneeJnt=cmds.duplicate(L_frontKneeJnt,n='R_jnt_frontKnee')
xPos=cmds.getAttr(L_frontKneeJnt+'.tx')
cmds.setAttr(R_frontKneeJnt[0]+'.tx',-xPos)

R_frontUpperKneeJnt=cmds.duplicate(L_frontUpperKneeJnt,n='R_jnt_frontUpperKnee')
xPos=cmds.getAttr(L_frontUpperKneeJnt+'.tx')
cmds.setAttr(R_frontUpperKneeJnt[0]+'.tx',-xPos)


R_frontFemurJnt=cmds.duplicate(L_frontFemurJnt,n='R_jnt_frontFemur')
xPos=cmds.getAttr(L_frontFemurJnt+'.tx')
cmds.setAttr(R_frontFemurJnt[0]+'.tx',-xPos)

#Parenting  FRONT joints

cmds.parent(L_frontToeJnt,L_frontAnkleJnt)
cmds.parent(L_frontAnkleJnt,L_frontKneeJnt)
cmds.parent(L_frontKneeJnt,L_frontUpperKneeJnt)
cmds.parent(L_frontUpperKneeJnt,L_frontFemurJnt)
cmds.parent(L_frontFemurJnt,frontPelvisJnt)
cmds.parent(R_frontToeJnt,R_frontAnkleJnt)
cmds.parent(R_frontAnkleJnt,R_frontKneeJnt)
cmds.parent(R_frontKneeJnt,R_frontUpperKneeJnt)
cmds.parent(R_frontUpperKneeJnt,R_frontFemurJnt)
cmds.parent(R_frontFemurJnt,frontPelvisJnt)

#Setting Orientation Of  FRONT joints

cmds.select(L_frontFemurJnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(R_frontFemurJnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(d=True)


#'''''''''''''CREATING IK  HIND JOINTS'''''''

#Left HIND IK  JOINTS
cmds.select(d=True)

posHindPelvis=cmds.xform(hindPelvis,q=1,t=1,ws=1)
hindPelvisIKjnt=cmds.joint(p=posHindPelvis,n='IKjnt_hindPelvis')
yellowCol(hindPelvisIKjnt)
cmds.select(d=True)


posHindToe=cmds.xform(hindToe,q=1,t=1,ws=1)
L_hindToeIKjnt=cmds.joint(p=posHindToe,n='L_IKjnt_hindToe')
yellowCol(L_hindToeIKjnt)
cmds.select(d=True)


posHindAnkle=cmds.xform(hindAnkle,q=1,t=1,ws=1)
L_hindAnkleIKjnt=cmds.joint(p=posHindAnkle,n='L_IKjnt_hindAnkle')
yellowCol(L_hindAnkleIKjnt)
cmds.select(d=True)

posHindKnee=cmds.xform(hindKnee,q=1,t=1,ws=1)
L_hindKneeIKjnt=cmds.joint(p=posHindKnee,n='L_IKjnt_hindKnee')
yellowCol(L_hindKneeIKjnt)
cmds.select(d=True)



posHindUpperKnee=cmds.xform(hindUpperKnee,q=1,t=1,ws=1)
L_hindUpperKneeIKjnt=cmds.joint(p=posHindUpperKnee,n='L_IKjnt_hindUpperKnee')
yellowCol(L_hindUpperKneeIKjnt)
cmds.select(d=True)


posHindFemur=cmds.xform(hindFemur,q=1,t=1,ws=1)
L_hindFemurIKjnt=cmds.joint(p=posHindFemur,n='L_IKjnt_hindFemur')
yellowCol(L_hindFemurIKjnt)
cmds.select(d=True)


#Mirroring IK HIND  joints to other side


R_hindToeIKjnt=cmds.duplicate(L_hindToeIKjnt,n='R_IKjnt_hindToe')   
xPos=cmds.getAttr(L_hindToeIKjnt+'.tx')
cmds.setAttr(R_hindToeIKjnt[0]+'.tx',-xPos)

R_hindAnkleIKjnt=cmds.duplicate(L_hindAnkleIKjnt,n='R_IKjnt_hindAnkle')
xPos=cmds.getAttr(L_hindAnkleIKjnt+'.tx')
cmds.setAttr(R_hindAnkleIKjnt[0]+'.tx',-xPos)

R_hindKneeIKjnt=cmds.duplicate(L_hindKneeIKjnt,n='R_IKjnt_hindKnee')
xPos=cmds.getAttr(L_hindKneeIKjnt+'.tx')
cmds.setAttr(R_hindKneeIKjnt[0]+'.tx',-xPos)

R_hindUpperKneeIKjnt=cmds.duplicate(L_hindUpperKneeIKjnt,n='R_IKjnt_hindUpperKnee')
xPos=cmds.getAttr(L_hindUpperKneeIKjnt+'.tx')
cmds.setAttr(R_hindUpperKneeIKjnt[0]+'.tx',-xPos)


R_hindFemurIKjnt=cmds.duplicate(L_hindFemurIKjnt,n='R_IKjnt_hindFemur')
xPos=cmds.getAttr(L_hindFemurIKjnt+'.tx')
cmds.setAttr(R_hindFemurIKjnt[0]+'.tx',-xPos)

#Parenting IK HIND joints

cmds.parent(L_hindToeIKjnt,L_hindAnkleIKjnt)
cmds.parent(L_hindAnkleIKjnt,L_hindKneeIKjnt)
cmds.parent(L_hindKneeIKjnt,L_hindUpperKneeIKjnt)
cmds.parent(L_hindUpperKneeIKjnt,L_hindFemurIKjnt)
cmds.parent(L_hindFemurIKjnt,hindPelvisIKjnt)
cmds.parent(R_hindToeIKjnt,R_hindAnkleIKjnt)
cmds.parent(R_hindAnkleIKjnt,R_hindKneeIKjnt)
cmds.parent(R_hindKneeIKjnt,R_hindUpperKneeIKjnt)
cmds.parent(R_hindUpperKneeIKjnt,R_hindFemurIKjnt)
cmds.parent(R_hindFemurIKjnt,hindPelvisIKjnt)

#Setting Orientation Of IK  HIND joints

cmds.select(L_hindFemurIKjnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(R_hindFemurIKjnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(d=True)


#'''''''''''''CREATING IK FRONT JOINTS'''''''

#Left IK  FRONT JOINTS
cmds.select(d=True)

posfrontPelvis=cmds.xform(frontPelvis,q=1,t=1,ws=1)
frontPelvisIKjnt=cmds.joint(p=posfrontPelvis,n='IKjnt_frontPelvis')
yellowCol(frontPelvisIKjnt)
cmds.select(d=True)


posfrontToe=cmds.xform(frontToe,q=1,t=1,ws=1)
L_frontToeIKjnt=cmds.joint(p=posfrontToe,n='L_IKjnt_frontToe')
yellowCol(L_frontToeIKjnt)
cmds.select(d=True)


posfrontAnkle=cmds.xform(frontAnkle,q=1,t=1,ws=1)
L_frontAnkleIKjnt=cmds.joint(p=posfrontAnkle,n='L_IKjnt_frontAnkle')
yellowCol(L_frontAnkleIKjnt)
cmds.select(d=True)

posfrontKnee=cmds.xform(frontKnee,q=1,t=1,ws=1)
L_frontKneeIKjnt=cmds.joint(p=posfrontKnee,n='L_IKjnt_frontKnee')
yellowCol(L_frontKneeIKjnt)
cmds.select(d=True)



posfrontUpperKnee=cmds.xform(frontUpperKnee,q=1,t=1,ws=1)
L_frontUpperKneeIKjnt=cmds.joint(p=posfrontUpperKnee,n='L_IKjnt_frontUpperKnee')
yellowCol(L_frontUpperKneeIKjnt)
cmds.select(d=True)


posfrontFemur=cmds.xform(frontFemur,q=1,t=1,ws=1)
L_frontFemurIKjnt=cmds.joint(p=posfrontFemur,n='L_IKjnt_frontFemur')
yellowCol(L_frontFemurIKjnt)
cmds.select(d=True)


#Mirroring IK FRONT  joints to other side


R_frontToeIKjnt=cmds.duplicate(L_frontToeIKjnt,n='R_IKjnt_frontToe')
xPos=cmds.getAttr(L_frontToeIKjnt+'.tx')
cmds.setAttr(R_frontToeIKjnt[0]+'.tx',-xPos)   

R_frontAnkleIKjnt=cmds.duplicate(L_frontAnkleIKjnt,n='R_IKjnt_frontAnkle')    
xPos=cmds.getAttr(L_frontAnkleIKjnt+'.tx')    
cmds.setAttr(R_frontAnkleIKjnt[0]+'.tx',-xPos)

R_frontKneeIKjnt=cmds.duplicate(L_frontKneeIKjnt,n='R_IKjnt_frontKnee')
xPos=cmds.getAttr(L_frontKneeIKjnt+'.tx')
cmds.setAttr(R_frontKneeIKjnt[0]+'.tx',-xPos)

R_frontUpperKneeIKjnt=cmds.duplicate(L_frontUpperKneeIKjnt,n='R_IKjnt_frontUpperKnee')
xPos=cmds.getAttr(L_frontUpperKneeIKjnt+'.tx')
cmds.setAttr(R_frontUpperKneeIKjnt[0]+'.tx',-xPos)


R_frontFemurIKjnt=cmds.duplicate(L_frontFemurIKjnt,n='R_IKjnt_frontFemur')
xPos=cmds.getAttr(L_frontFemurIKjnt+'.tx')
cmds.setAttr(R_frontFemurIKjnt[0]+'.tx',-xPos)

#Parenting IK FRONT joints

cmds.parent(L_frontToeIKjnt,L_frontAnkleIKjnt)
cmds.parent(L_frontAnkleIKjnt,L_frontKneeIKjnt)
cmds.parent(L_frontKneeIKjnt,L_frontUpperKneeIKjnt)
cmds.parent(L_frontUpperKneeIKjnt,L_frontFemurIKjnt)
cmds.parent(L_frontFemurIKjnt,frontPelvisIKjnt)
cmds.parent(R_frontToeIKjnt,R_frontAnkleIKjnt)
cmds.parent(R_frontAnkleIKjnt,R_frontKneeIKjnt)
cmds.parent(R_frontKneeIKjnt,R_frontUpperKneeIKjnt)
cmds.parent(R_frontUpperKneeIKjnt,R_frontFemurIKjnt)
cmds.parent(R_frontFemurIKjnt,frontPelvisIKjnt)

#Setting Orientation Of IK FRONT joints

cmds.select(L_frontFemurIKjnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(R_frontFemurIKjnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(d=True)


#'''''''''''''CREATING FK  HIND JOINTS'''''''

#Left HIND FK  JOINTS
cmds.select(d=True)

posHindPelvis=cmds.xform(hindPelvis,q=1,t=1,ws=1)
hindPelvisFKjnt=cmds.joint(p=posHindPelvis,n='FKjnt_hindPelvis')
yellowCol(hindPelvisFKjnt)
cmds.select(d=True)


posHindToe=cmds.xform(hindToe,q=1,t=1,ws=1)
L_hindToeFKjnt=cmds.joint(p=posHindToe,n='L_FKjnt_hindToe')
yellowCol(L_hindToeFKjnt)
cmds.select(d=True)


posHindAnkle=cmds.xform(hindAnkle,q=1,t=1,ws=1)
L_hindAnkleFKjnt=cmds.joint(p=posHindAnkle,n='L_FKjnt_hindAnkle')
yellowCol(L_hindAnkleFKjnt)
cmds.select(d=True)

posHindKnee=cmds.xform(hindKnee,q=1,t=1,ws=1)
L_hindKneeFKjnt=cmds.joint(p=posHindKnee,n='L_FKjnt_hindKnee')
yellowCol(L_hindKneeFKjnt)
cmds.select(d=True)



posHindUpperKnee=cmds.xform(hindUpperKnee,q=1,t=1,ws=1)
L_hindUpperKneeFKjnt=cmds.joint(p=posHindUpperKnee,n='L_FKjnt_hindUpperKnee')
yellowCol(L_hindUpperKneeFKjnt)
cmds.select(d=True)


posHindFemur=cmds.xform(hindFemur,q=1,t=1,ws=1)
L_hindFemurFKjnt=cmds.joint(p=posHindFemur,n='L_FKjnt_hindFemur')
yellowCol(L_hindFemurFKjnt)
cmds.select(d=True)


#Mirroring FK HIND  joints to other side


R_hindToeFKjnt=cmds.duplicate(L_hindToeFKjnt,n='R_FKjnt_hindToe')   
xPos=cmds.getAttr(L_hindToeFKjnt+'.tx')
cmds.setAttr(R_hindToeFKjnt[0]+'.tx',-xPos)

R_hindAnkleFKjnt=cmds.duplicate(L_hindAnkleFKjnt,n='R_FKjnt_hindAnkle')
xPos=cmds.getAttr(L_hindAnkleFKjnt+'.tx')
cmds.setAttr(R_hindAnkleFKjnt[0]+'.tx',-xPos)

R_hindKneeFKjnt=cmds.duplicate(L_hindKneeFKjnt,n='R_FKjnt_hindKnee')
xPos=cmds.getAttr(L_hindKneeFKjnt+'.tx')
cmds.setAttr(R_hindKneeFKjnt[0]+'.tx',-xPos)

R_hindUpperKneeFKjnt=cmds.duplicate(L_hindUpperKneeFKjnt,n='R_FKjnt_hindUpperKnee')
xPos=cmds.getAttr(L_hindUpperKneeFKjnt+'.tx')
cmds.setAttr(R_hindUpperKneeFKjnt[0]+'.tx',-xPos)


R_hindFemurFKjnt=cmds.duplicate(L_hindFemurFKjnt,n='R_FKjnt_hindFemur')
xPos=cmds.getAttr(L_hindFemurFKjnt+'.tx')
cmds.setAttr(R_hindFemurFKjnt[0]+'.tx',-xPos)

#Parenting FK HIND joints

cmds.parent(L_hindToeFKjnt,L_hindAnkleFKjnt)
cmds.parent(L_hindAnkleFKjnt,L_hindKneeFKjnt)
cmds.parent(L_hindKneeFKjnt,L_hindUpperKneeFKjnt)
cmds.parent(L_hindUpperKneeFKjnt,L_hindFemurFKjnt)
cmds.parent(L_hindFemurFKjnt,hindPelvisFKjnt)
cmds.parent(R_hindToeFKjnt,R_hindAnkleFKjnt)
cmds.parent(R_hindAnkleFKjnt,R_hindKneeFKjnt)
cmds.parent(R_hindKneeFKjnt,R_hindUpperKneeFKjnt)
cmds.parent(R_hindUpperKneeFKjnt,R_hindFemurFKjnt)
cmds.parent(R_hindFemurFKjnt,hindPelvisFKjnt)

#Setting Orientation Of FK  HIND joints

cmds.select(L_hindFemurFKjnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(R_hindFemurFKjnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(d=True)


#'''''''''''''CREATING FK FRONT JOINTS'''''''

#Left FK  FRONT JOINTS
cmds.select(d=True)

posfrontPelvis=cmds.xform(frontPelvis,q=1,t=1,ws=1)
frontPelvisFKjnt=cmds.joint(p=posfrontPelvis,n='FKjnt_frontPelvis')
yellowCol(frontPelvisFKjnt)
cmds.select(d=True)


posfrontToe=cmds.xform(frontToe,q=1,t=1,ws=1)
L_frontToeFKjnt=cmds.joint(p=posfrontToe,n='L_FKjnt_frontToe')
yellowCol(L_frontToeFKjnt)
cmds.select(d=True)


posfrontAnkle=cmds.xform(frontAnkle,q=1,t=1,ws=1)
L_frontAnkleFKjnt=cmds.joint(p=posfrontAnkle,n='L_FKjnt_frontAnkle')
yellowCol(L_frontAnkleFKjnt)
cmds.select(d=True)

posfrontKnee=cmds.xform(frontKnee,q=1,t=1,ws=1)
L_frontKneeFKjnt=cmds.joint(p=posfrontKnee,n='L_FKjnt_frontKnee')
yellowCol(L_frontKneeFKjnt)
cmds.select(d=True)



posfrontUpperKnee=cmds.xform(frontUpperKnee,q=1,t=1,ws=1)
L_frontUpperKneeFKjnt=cmds.joint(p=posfrontUpperKnee,n='L_FKjnt_frontUpperKnee')
yellowCol(L_frontUpperKneeFKjnt)
cmds.select(d=True)


posfrontFemur=cmds.xform(frontFemur,q=1,t=1,ws=1)
L_frontFemurFKjnt=cmds.joint(p=posfrontFemur,n='L_FKjnt_frontFemur')
yellowCol(L_frontFemurFKjnt)
cmds.select(d=True)


#Mirroring FK FRONT  joints to other side


R_frontToeFKjnt=cmds.duplicate(L_frontToeFKjnt,n='R_FKjnt_frontToe')
xPos=cmds.getAttr(L_frontToeFKjnt+'.tx')
cmds.setAttr(R_frontToeFKjnt[0]+'.tx',-xPos)   

R_frontAnkleFKjnt=cmds.duplicate(L_frontAnkleFKjnt,n='R_FKjnt_frontAnkle')    
xPos=cmds.getAttr(L_frontAnkleFKjnt+'.tx')    
cmds.setAttr(R_frontAnkleFKjnt[0]+'.tx',-xPos)

R_frontKneeFKjnt=cmds.duplicate(L_frontKneeFKjnt,n='R_FKjnt_frontKnee')
xPos=cmds.getAttr(L_frontKneeFKjnt+'.tx')
cmds.setAttr(R_frontKneeFKjnt[0]+'.tx',-xPos)

R_frontUpperKneeFKjnt=cmds.duplicate(L_frontUpperKneeFKjnt,n='R_FKjnt_frontUpperKnee')
xPos=cmds.getAttr(L_frontUpperKneeFKjnt+'.tx')
cmds.setAttr(R_frontUpperKneeFKjnt[0]+'.tx',-xPos)


R_frontFemurFKjnt=cmds.duplicate(L_frontFemurFKjnt,n='R_FKjnt_frontFemur')
xPos=cmds.getAttr(L_frontFemurFKjnt+'.tx')
cmds.setAttr(R_frontFemurFKjnt[0]+'.tx',-xPos)

#Parenting FK FRONT joints

cmds.parent(L_frontToeFKjnt,L_frontAnkleFKjnt)
cmds.parent(L_frontAnkleFKjnt,L_frontKneeFKjnt)
cmds.parent(L_frontKneeFKjnt,L_frontUpperKneeFKjnt)
cmds.parent(L_frontUpperKneeFKjnt,L_frontFemurFKjnt)
cmds.parent(L_frontFemurFKjnt,frontPelvisFKjnt)
cmds.parent(R_frontToeFKjnt,R_frontAnkleFKjnt)
cmds.parent(R_frontAnkleFKjnt,R_frontKneeFKjnt)
cmds.parent(R_frontKneeFKjnt,R_frontUpperKneeFKjnt)
cmds.parent(R_frontUpperKneeFKjnt,R_frontFemurFKjnt)
cmds.parent(R_frontFemurFKjnt,frontPelvisFKjnt)

#Setting Orientation Of FK FRONT joints

cmds.select(L_frontFemurFKjnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(R_frontFemurFKjnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(d=True)

