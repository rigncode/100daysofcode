 
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

def Locators():


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

    NeckRoot=cmds.spaceLocator(n='Loc_NeckRoot')
    cmds.setAttr(NeckRoot[0]+'.translateY',48)
    cmds.setAttr(NeckRoot[0]+'.translateZ',30)
    yellowCol(NeckRoot[0])

    NeckEnd=cmds.spaceLocator(n='Loc_NeckEnd')
    cmds.setAttr(NeckEnd[0]+'.translateY',58)
    cmds.setAttr(NeckEnd[0]+'.translateZ',50)
    yellowCol(NeckEnd[0])

    NeckLocGrp=cmds.group(NeckRoot,NeckEnd,n='Neck_Locators')

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

    mainLocGrp=cmds.group(tailLocGrp,NeckLocGrp,frontLocGrp,hindLocGrp,n='Locators')
Locators():

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


posHindToe=cmds.xform(hindToe,q=1,t=1,ws=1)
L_hindToeIKjnt=cmds.joint(p=posHindToe,n='IK_Ljnt_hindToe')
yellowCol(L_hindToeIKjnt)
cmds.select(d=True)


posHindAnkle=cmds.xform(hindAnkle,q=1,t=1,ws=1)
L_hindAnkleIKjnt=cmds.joint(p=posHindAnkle,n='IK_Ljnt_hindAnkle')
yellowCol(L_hindAnkleIKjnt)
cmds.select(d=True)

posHindKnee=cmds.xform(hindKnee,q=1,t=1,ws=1)
L_hindKneeIKjnt=cmds.joint(p=posHindKnee,n='IK_Ljnt_hindKnee')
yellowCol(L_hindKneeIKjnt)
cmds.select(d=True)



posHindUpperKnee=cmds.xform(hindUpperKnee,q=1,t=1,ws=1)
L_hindUpperKneeIKjnt=cmds.joint(p=posHindUpperKnee,n='IK_Ljnt_hindUpperKnee')
yellowCol(L_hindUpperKneeIKjnt)
cmds.select(d=True)


posHindFemur=cmds.xform(hindFemur,q=1,t=1,ws=1)
L_hindFemurIKjnt=cmds.joint(p=posHindFemur,n='IK_Ljnt_hindFemur')
yellowCol(L_hindFemurIKjnt)
cmds.select(d=True)


#Mirroring IK HIND  joints to other side


R_hindToeIKjnt=cmds.duplicate(L_hindToeIKjnt,n='IK_Rjnt_hindToe')   
xPos=cmds.getAttr(L_hindToeIKjnt+'.tx')
cmds.setAttr(R_hindToeIKjnt[0]+'.tx',-xPos)

R_hindAnkleIKjnt=cmds.duplicate(L_hindAnkleIKjnt,n='IK_Rjnt_hindAnkle')
xPos=cmds.getAttr(L_hindAnkleIKjnt+'.tx')
cmds.setAttr(R_hindAnkleIKjnt[0]+'.tx',-xPos)

R_hindKneeIKjnt=cmds.duplicate(L_hindKneeIKjnt,n='IK_Rjnt_hindKnee')
xPos=cmds.getAttr(L_hindKneeIKjnt+'.tx')
cmds.setAttr(R_hindKneeIKjnt[0]+'.tx',-xPos)

R_hindUpperKneeIKjnt=cmds.duplicate(L_hindUpperKneeIKjnt,n='IK_Rjnt_hindUpperKnee')
xPos=cmds.getAttr(L_hindUpperKneeIKjnt+'.tx')
cmds.setAttr(R_hindUpperKneeIKjnt[0]+'.tx',-xPos)


R_hindFemurIKjnt=cmds.duplicate(L_hindFemurIKjnt,n='IK_Rjnt_hindFemur')
xPos=cmds.getAttr(L_hindFemurIKjnt+'.tx')
cmds.setAttr(R_hindFemurIKjnt[0]+'.tx',-xPos)

#Parenting IK HIND joints

cmds.parent(L_hindToeIKjnt,L_hindAnkleIKjnt)
cmds.parent(L_hindAnkleIKjnt,L_hindKneeIKjnt)
cmds.parent(L_hindKneeIKjnt,L_hindUpperKneeIKjnt)
cmds.parent(L_hindUpperKneeIKjnt,L_hindFemurIKjnt)


cmds.parent(R_hindToeIKjnt,R_hindAnkleIKjnt)
cmds.parent(R_hindAnkleIKjnt,R_hindKneeIKjnt)
cmds.parent(R_hindKneeIKjnt,R_hindUpperKneeIKjnt)
cmds.parent(R_hindUpperKneeIKjnt,R_hindFemurIKjnt)


#Setting Orientation Of IK  HIND joints

cmds.select(L_hindFemurIKjnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(R_hindFemurIKjnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(d=True)

cmds.select("jnt_hindPelvis","jnt_frontPelvis")
cmds.group(n="Bind_Chain")






#'''''''''''''CREATING IK FRONT JOINTS'''''''

#Left IK  FRONT JOINTS
cmds.select(d=True)
posfrontToe=cmds.xform(frontToe,q=1,t=1,ws=1)
L_frontToeIKjnt=cmds.joint(p=posfrontToe,n='IK_Ljnt_frontToe')
yellowCol(L_frontToeIKjnt)
cmds.select(d=True)


posfrontAnkle=cmds.xform(frontAnkle,q=1,t=1,ws=1)
L_frontAnkleIKjnt=cmds.joint(p=posfrontAnkle,n='IK_Ljnt_frontAnkle')
yellowCol(L_frontAnkleIKjnt)
cmds.select(d=True)

posfrontKnee=cmds.xform(frontKnee,q=1,t=1,ws=1)
L_frontKneeIKjnt=cmds.joint(p=posfrontKnee,n='IK_Ljnt_frontKnee')
yellowCol(L_frontKneeIKjnt)
cmds.select(d=True)



posfrontUpperKnee=cmds.xform(frontUpperKnee,q=1,t=1,ws=1)
L_frontUpperKneeIKjnt=cmds.joint(p=posfrontUpperKnee,n='IK_Ljnt_frontUpperKnee')
yellowCol(L_frontUpperKneeIKjnt)
cmds.select(d=True)


posfrontFemur=cmds.xform(frontFemur,q=1,t=1,ws=1)
L_frontFemurIKjnt=cmds.joint(p=posfrontFemur,n='IK_Ljnt_frontFemur')
yellowCol(L_frontFemurIKjnt)
cmds.select(d=True)


#Mirroring IK FRONT  joints to other side


R_frontToeIKjnt=cmds.duplicate(L_frontToeIKjnt,n='IK_Rjnt_frontToe')
xPos=cmds.getAttr(L_frontToeIKjnt+'.tx')
cmds.setAttr(R_frontToeIKjnt[0]+'.tx',-xPos)   

R_frontAnkleIKjnt=cmds.duplicate(L_frontAnkleIKjnt,n='IK_Rjnt_frontAnkle')    
xPos=cmds.getAttr(L_frontAnkleIKjnt+'.tx')    
cmds.setAttr(R_frontAnkleIKjnt[0]+'.tx',-xPos)

R_frontKneeIKjnt=cmds.duplicate(L_frontKneeIKjnt,n='IK_Rjnt_frontKnee')
xPos=cmds.getAttr(L_frontKneeIKjnt+'.tx')
cmds.setAttr(R_frontKneeIKjnt[0]+'.tx',-xPos)

R_frontUpperKneeIKjnt=cmds.duplicate(L_frontUpperKneeIKjnt,n='IK_Rjnt_frontUpperKnee')
xPos=cmds.getAttr(L_frontUpperKneeIKjnt+'.tx')
cmds.setAttr(R_frontUpperKneeIKjnt[0]+'.tx',-xPos)


R_frontFemurIKjnt=cmds.duplicate(L_frontFemurIKjnt,n='IK_Rjnt_frontFemur')
xPos=cmds.getAttr(L_frontFemurIKjnt+'.tx')
cmds.setAttr(R_frontFemurIKjnt[0]+'.tx',-xPos)

#Parenting IK FRONT joints

cmds.parent(L_frontToeIKjnt,L_frontAnkleIKjnt)
cmds.parent(L_frontAnkleIKjnt,L_frontKneeIKjnt)
cmds.parent(L_frontKneeIKjnt,L_frontUpperKneeIKjnt)
cmds.parent(L_frontUpperKneeIKjnt,L_frontFemurIKjnt)
cmds.parent(R_frontToeIKjnt,R_frontAnkleIKjnt)
cmds.parent(R_frontAnkleIKjnt,R_frontKneeIKjnt)
cmds.parent(R_frontKneeIKjnt,R_frontUpperKneeIKjnt)
cmds.parent(R_frontUpperKneeIKjnt,R_frontFemurIKjnt)


#Setting Orientation Of IK FRONT joints

cmds.select(L_frontFemurIKjnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(R_frontFemurIKjnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(d=True)


#'''''''''''''CREATING FK  HIND JOINTS'''''''

#Left HIND FK  JOINTS
cmds.select(d=True)
L_hindToeFKjnt=cmds.joint(p=posHindToe,n='FK_Ljnt_hindToe')
yellowCol(L_hindToeFKjnt)
cmds.select(d=True)
 
L_hindAnkleFKjnt=cmds.joint(p=posHindAnkle,n='FK_Ljnt_hindAnkle')
yellowCol(L_hindAnkleFKjnt)
cmds.select(d=True)

posHindKnee=cmds.xform(hindKnee,q=1,t=1,ws=1)
L_hindKneeFKjnt=cmds.joint(p=posHindKnee,n='FK_Ljnt_hindKnee')
yellowCol(L_hindKneeFKjnt)
cmds.select(d=True)



posHindUpperKnee=cmds.xform(hindUpperKnee,q=1,t=1,ws=1)
L_hindUpperKneeFKjnt=cmds.joint(p=posHindUpperKnee,n='FK_Ljnt_hindUpperKnee')
yellowCol(L_hindUpperKneeFKjnt)
cmds.select(d=True)


posHindFemur=cmds.xform(hindFemur,q=1,t=1,ws=1)
L_hindFemurFKjnt=cmds.joint(p=posHindFemur,n='FK_Ljnt_hindFemur')
yellowCol(L_hindFemurFKjnt)
cmds.select(d=True)


#Mirroring FK HIND  joints to other side


R_hindToeFKjnt=cmds.duplicate(L_hindToeFKjnt,n='FK_Rjnt_hindToe')   
xPos=cmds.getAttr(L_hindToeFKjnt+'.tx')
cmds.setAttr(R_hindToeFKjnt[0]+'.tx',-xPos)

R_hindAnkleFKjnt=cmds.duplicate(L_hindAnkleFKjnt,n='FK_Rjnt_hindAnkle')
xPos=cmds.getAttr(L_hindAnkleFKjnt+'.tx')
cmds.setAttr(R_hindAnkleFKjnt[0]+'.tx',-xPos)

R_hindKneeFKjnt=cmds.duplicate(L_hindKneeFKjnt,n='FK_Rjnt_hindKnee')
xPos=cmds.getAttr(L_hindKneeFKjnt+'.tx')
cmds.setAttr(R_hindKneeFKjnt[0]+'.tx',-xPos)

R_hindUpperKneeFKjnt=cmds.duplicate(L_hindUpperKneeFKjnt,n='FK_Rjnt_hindUpperKnee')
xPos=cmds.getAttr(L_hindUpperKneeFKjnt+'.tx')
cmds.setAttr(R_hindUpperKneeFKjnt[0]+'.tx',-xPos)


R_hindFemurFKjnt=cmds.duplicate(L_hindFemurFKjnt,n='FK_Rjnt_hindFemur')
xPos=cmds.getAttr(L_hindFemurFKjnt+'.tx')
cmds.setAttr(R_hindFemurFKjnt[0]+'.tx',-xPos)

#Parenting FK HIND joints

cmds.parent(L_hindToeFKjnt,L_hindAnkleFKjnt)
cmds.parent(L_hindAnkleFKjnt,L_hindKneeFKjnt)
cmds.parent(L_hindKneeFKjnt,L_hindUpperKneeFKjnt)
cmds.parent(L_hindUpperKneeFKjnt,L_hindFemurFKjnt)

cmds.parent(R_hindToeFKjnt,R_hindAnkleFKjnt)
cmds.parent(R_hindAnkleFKjnt,R_hindKneeFKjnt)
cmds.parent(R_hindKneeFKjnt,R_hindUpperKneeFKjnt)
cmds.parent(R_hindUpperKneeFKjnt,R_hindFemurFKjnt)


#Setting Orientation Of FK  HIND joints

cmds.select(L_hindFemurFKjnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(R_hindFemurFKjnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(d=True)


#'''''''''''''CREATING FK FRONT JOINTS'''''''

#Left FK  FRONT JOINTS
cmds.select(d=True)


posfrontToe=cmds.xform(frontToe,q=1,t=1,ws=1)
L_frontToeFKjnt=cmds.joint(p=posfrontToe,n='FK_Ljnt_frontToe')
yellowCol(L_frontToeFKjnt)
cmds.select(d=True)


posfrontAnkle=cmds.xform(frontAnkle,q=1,t=1,ws=1)
L_frontAnkleFKjnt=cmds.joint(p=posfrontAnkle,n='FK_Ljnt_frontAnkle')
yellowCol(L_frontAnkleFKjnt)
cmds.select(d=True)

posfrontKnee=cmds.xform(frontKnee,q=1,t=1,ws=1)
L_frontKneeFKjnt=cmds.joint(p=posfrontKnee,n='FK_Ljnt_frontKnee')
yellowCol(L_frontKneeFKjnt)
cmds.select(d=True)



posfrontUpperKnee=cmds.xform(frontUpperKnee,q=1,t=1,ws=1)
L_frontUpperKneeFKjnt=cmds.joint(p=posfrontUpperKnee,n='FK_Ljnt_frontUpperKnee')
yellowCol(L_frontUpperKneeFKjnt)
cmds.select(d=True)


posfrontFemur=cmds.xform(frontFemur,q=1,t=1,ws=1)
L_frontFemurFKjnt=cmds.joint(p=posfrontFemur,n='FK_Ljnt_frontFemur')
yellowCol(L_frontFemurFKjnt)
cmds.select(d=True)


#Mirroring FK FRONT  joints to other side


R_frontToeFKjnt=cmds.duplicate(L_frontToeFKjnt,n='FK_Rjnt_frontToe')
xPos=cmds.getAttr(L_frontToeFKjnt+'.tx')
cmds.setAttr(R_frontToeFKjnt[0]+'.tx',-xPos)   

R_frontAnkleFKjnt=cmds.duplicate(L_frontAnkleFKjnt,n='FK_Rjnt_frontAnkle')    
xPos=cmds.getAttr(L_frontAnkleFKjnt+'.tx')    
cmds.setAttr(R_frontAnkleFKjnt[0]+'.tx',-xPos)

R_frontKneeFKjnt=cmds.duplicate(L_frontKneeFKjnt,n='FK_Rjnt_frontKnee')
xPos=cmds.getAttr(L_frontKneeFKjnt+'.tx')
cmds.setAttr(R_frontKneeFKjnt[0]+'.tx',-xPos)

R_frontUpperKneeFKjnt=cmds.duplicate(L_frontUpperKneeFKjnt,n='FK_Rjnt_frontUpperKnee')
xPos=cmds.getAttr(L_frontUpperKneeFKjnt+'.tx')
cmds.setAttr(R_frontUpperKneeFKjnt[0]+'.tx',-xPos)


R_frontFemurFKjnt=cmds.duplicate(L_frontFemurFKjnt,n='FK_Rjnt_frontFemur')
xPos=cmds.getAttr(L_frontFemurFKjnt+'.tx')
cmds.setAttr(R_frontFemurFKjnt[0]+'.tx',-xPos)

#Parenting FK FRONT joints

cmds.parent(L_frontToeFKjnt,L_frontAnkleFKjnt)
cmds.parent(L_frontAnkleFKjnt,L_frontKneeFKjnt)
cmds.parent(L_frontKneeFKjnt,L_frontUpperKneeFKjnt)
cmds.parent(L_frontUpperKneeFKjnt,L_frontFemurFKjnt)

cmds.parent(R_frontToeFKjnt,R_frontAnkleFKjnt)
cmds.parent(R_frontAnkleFKjnt,R_frontKneeFKjnt)
cmds.parent(R_frontKneeFKjnt,R_frontUpperKneeFKjnt)
cmds.parent(R_frontUpperKneeFKjnt,R_frontFemurFKjnt)


#Setting Orientation Of FK FRONT joints

cmds.select(L_frontFemurFKjnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(R_frontFemurFKjnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(d=True)



cmds.select("FK_Rjnt_frontFemur","FK_Ljnt_frontFemur","FK_Rjnt_hindFemur","FK_Ljnt_hindFemur")
cmds.group(n="FK_Chain")

cmds.select(d=True)
cmds.select("IK_Rjnt_frontFemur","IK_Ljnt_frontFemur","IK_Rjnt_hindFemur","IK_Ljnt_hindFemur")
cmds.group(n="IK_Chain")

cmds.select(d=True)
cmds.select("IK_Chain","FK_Chain","Bind_Chain")
cmds.group(n="Jnt_Setup")

cmds.select(d=True)
cmds.select("Locators","Jnt_Setup")
cmds.group(n="Rig_Setup")


#IK SETUP



''' L hind leg IK'''
# IK controller...
L_Ik=cmds.ikHandle(sol='ikRPsolver',n='l_hindLeg_IK',sj=L_hindFemurIKjnt,ee=L_hindAnkleIKjnt )
L_hindIkCtrl_TMP=mel.eval("curve -d 1 -p -1 1 1 -p -1 1 -1 -p 1 1 -1 -p 1 1 1 -p -1 1 1 -p -1 -1 1 -p -1 -1 -1 -p -1 1 -1 -p -1 1 1 -p -1 -1 1 -p 1 -1 1 -p 1 1 1 -p 1 1 -1 -p 1 -1 -1 -p 1 -1 1 -p 1 -1 -1 -p -1 -1 -1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16;")
L_hindIkCtrl=cmds.rename(L_hindIkCtrl_TMP,'IkRp_L_Hind')
# get distance to get controller with decent scale...
dist=cmds.createNode('distanceDimShape',n='delete_me_I_am_in_pain')
legStart=cmds.xform(L_hindToeIKjnt,q=True,ws=True,rp=True)
legEnd=cmds.xform(L_frontToeIKjnt,q=True,ws=True,rp=True)
cmds.setAttr(dist+'.endPoint',*(legStart))
cmds.setAttr(dist+'.startPoint',*(legEnd))
distance=cmds.getAttr(dist+'.distance')
cmds.delete(cmds.listRelatives(dist,p=True))
distance=distance/8
cmds.setAttr(L_hindIkCtrl+'.sx',distance)
cmds.setAttr(L_hindIkCtrl+'.sy',distance)
cmds.setAttr(L_hindIkCtrl+'.sz',distance)
cmds.makeIdentity(L_hindIkCtrl,apply=True,t=1,r=1,s=1,n=0)

L_hindIkCtrlGrp=cmds.group(L_hindIkCtrl,n='Offset_LfootIKCtrl')
blueCol(L_hindIkCtrlGrp)
constr=cmds.pointConstraint(L_hindToeJnt,L_hindIkCtrlGrp)
cmds.delete(constr)
cmds.parent(L_Ik[0],L_hindIkCtrl)
cmds.setAttr(L_Ik[0]+'.visibility',0)
# aim constraint makes the upper hind femur joint follow by some but lets the leg fold up like it should...
cmds.aimConstraint(L_hindIkCtrl,L_hindFemurIKjnt,n='l_femur_aim_towards_footCtrl',mo=True,wu=[0,0,0])
L_IkToe=cmds.ikHandle(sol='ikRPsolver',n='l_hindToe_IK', sj=L_hindAnkleIKjnt,ee=L_hindToeIKjnt)
cmds.parent(L_IkToe[0],L_hindIkCtrl)
cmds.setAttr(L_IkToe[0]+'.visibility',0)

''' r hind leg IK'''
# IK controller...
R_Ik=cmds.ikHandle(sol='ikRPsolver',n='r_hindLeg_IK',sj=R_hindFemurIKjnt[0],ee=R_hindAnkleIKjnt[0] )
R_hindIkCtrl_TMP=mel.eval("curve -d 1 -p -1 1 1 -p -1 1 -1 -p 1 1 -1 -p 1 1 1 -p -1 1 1 -p -1 -1 1 -p -1 -1 -1 -p -1 1 -1 -p -1 1 1 -p -1 -1 1 -p 1 -1 1 -p 1 1 1 -p 1 1 -1 -p 1 -1 -1 -p 1 -1 1 -p 1 -1 -1 -p -1 -1 -1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16;")
R_hindIkCtrl=cmds.rename(R_hindIkCtrl_TMP,'IkRp_R_Hind')
cmds.setAttr(R_hindIkCtrl+'.sx',distance)
cmds.setAttr(R_hindIkCtrl+'.sy',distance)
cmds.setAttr(R_hindIkCtrl+'.sz',distance)
cmds.makeIdentity(R_hindIkCtrl,apply=True,t=1,r=1,s=1,n=0)
R_hindIkCtrlGrp=cmds.group(R_hindIkCtrl,n='r_footIKCtrl_GRP')

constr=cmds.pointConstraint(R_hindToeJnt,R_hindIkCtrlGrp)
cmds.delete(constr)
cmds.parent(R_Ik[0],R_hindIkCtrl)
cmds.setAttr(R_Ik[0]+'.visibility',0)
# aim constraint makes the upper hind femur joint follow by some but lets the leg fold up like it should...
cmds.aimConstraint(R_hindIkCtrl,R_hindFemurIKjnt,n='r_femur_aim_towards_footCtrl',mo=True,wu=[0,0,0])
R_IkToe=cmds.ikHandle(sol='ikRPsolver',n='r_hindToe_IK', sj=R_hindAnkleIKjnt[0],ee=R_hindToeIKjnt[0])
cmds.parent(R_IkToe[0],R_hindIkCtrl)
cmds.setAttr(R_IkToe[0]+'.visibility',0)

''' l front leg IK'''
L_FIk=cmds.ikHandle(sol='ikRPsolver',n='l_frontLeg_IK',sj=L_frontFemurIKjnt,ee=L_frontAnkleIKjnt )
L_frontIkCtrl_TMP=mel.eval("curve -d 1 -p -1 1 1 -p -1 1 -1 -p 1 1 -1 -p 1 1 1 -p -1 1 1 -p -1 -1 1 -p -1 -1 -1 -p -1 1 -1 -p -1 1 1 -p -1 -1 1 -p 1 -1 1 -p 1 1 1 -p 1 1 -1 -p 1 -1 -1 -p 1 -1 1 -p 1 -1 -1 -p -1 -1 -1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16;")
L_frontIkCtrl=cmds.rename(L_frontIkCtrl_TMP,'IkRp_L_Front')
cmds.setAttr(L_frontIkCtrl+'.sx',distance)
cmds.setAttr(L_frontIkCtrl+'.sy',distance)
cmds.setAttr(L_frontIkCtrl+'.sz',distance)
cmds.makeIdentity(L_frontIkCtrl,apply=True,t=1,r=1,s=1,n=0)
L_frontIkCtrlGrp=cmds.group(L_frontIkCtrl,n='l_frontFootIKCtrl_GRP')
blueCol(L_frontIkCtrlGrp)
constr=cmds.pointConstraint(L_frontToeJnt,L_frontIkCtrlGrp)
cmds.delete(constr)
cmds.parent(L_FIk[0],L_frontIkCtrl)
cmds.setAttr(L_FIk[0]+'.visibility',0)
L_FToeIk=cmds.ikHandle(sol='ikRPsolver',n='l_frontToe_IK',sj=L_frontAnkleIKjnt,ee=L_frontToeIKjnt)
cmds.parent(L_FToeIk[0],L_frontIkCtrl)


''' l ik front leg rotation ctrl '''
L_frontLegRotation=cmds.circle(nr=(1,0,0), c=(0,0,0), n='l_frontLegRotate_CTRL')
L_frontLegRotationGrp=cmds.group(L_frontLegRotation, n='l_frontLegRotateCtrl_GRP')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_frontLegRotationGrp,apply=True, t=1,r=1,s=1,n=0)
constr=cmds.pointConstraint(L_frontFemurIKjnt,L_frontLegRotationGrp)
cmds.delete(constr)
blueCol(L_frontLegRotation[0])


''' r front leg IK'''
R_FIk=cmds.ikHandle(sol='ikRPsolver',n='r_frontLeg_IK',sj=R_frontFemurIKjnt[0],ee=R_frontAnkleIKjnt[0] )

R_frontIkCtrl_TMP=mel.eval("curve -d 1 -p -1 1 1 -p -1 1 -1 -p 1 1 -1 -p 1 1 1 -p -1 1 1 -p -1 -1 1 -p -1 -1 -1 -p -1 1 -1 -p -1 1 1 -p -1 -1 1 -p 1 -1 1 -p 1 1 1 -p 1 1 -1 -p 1 -1 -1 -p 1 -1 1 -p 1 -1 -1 -p -1 -1 -1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16;")
R_frontIkCtrl=cmds.rename(R_frontIkCtrl_TMP,'IkRp_R_Front')
cmds.setAttr(R_frontIkCtrl+'.sx',distance)
cmds.setAttr(R_frontIkCtrl+'.sy',distance)
cmds.setAttr(R_frontIkCtrl+'.sz',distance)
cmds.makeIdentity(R_frontIkCtrl,apply=True,t=1,r=1,s=1,n=0)

R_frontIkCtrlGrp=cmds.group(R_frontIkCtrl,n='r_frontFootIKCtrl_GRP')

constr=cmds.pointConstraint(R_frontToeJnt,R_frontIkCtrlGrp)
cmds.delete(constr)
cmds.parent(R_FIk[0],R_frontIkCtrl)
cmds.setAttr(R_FIk[0]+'.visibility',0)
''' r ik front leg rotation ctrl '''
R_frontLegRotation=cmds.circle(nr=(1,0,0), c=(0,0,0), n='r_frontLegRotate_CTRL')
R_frontLegRotationGrp=cmds.group(R_frontLegRotation, n='r_frontLegRotateCtrl_GRP')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_frontLegRotationGrp,apply=True, t=1,r=1,s=1,n=0)
constr=cmds.pointConstraint(R_frontFemurIKjnt,R_frontLegRotationGrp)
cmds.delete(constr)

cmds.setAttr(R_FIk[0]+'.visibility',0)
R_FToeIk=cmds.ikHandle(sol='ikRPsolver',n='r_frontToe_IK',sj=R_frontAnkleIKjnt[0],ee=R_frontToeIKjnt[0])
cmds.parent(R_FToeIk[0],R_frontIkCtrl)

''' create IK polevector '''
# l hind IK
L_hindPole_TMP=mel.eval("curve -d 1 -p 0 0 2 -p 0 0 1.001092 -p 0 0.383101 0.924889 -p 0 0.707879 0.707879 -p 0 0.924889 0.383101 -p 0 1.001092 0 -p 0 2 0 -p 0 1.001092 0 -p 0 0.924889 -0.383101 -p 0 0.707879 -0.707879 -p 0 0.383101 -0.924889 -p 0 0 -1.001092 -p 0 0 -2 -p 0 0 -1.001092 -p 0 -0.383101 -0.924889 -p 0 -0.707879 -0.707879 -p 0 -0.924889 -0.383101 -p 0 -1.001092 0 -p 0 -2 0 -p 0 -1.001092 0 -p 0 -0.924889 0.383101 -p 0 -0.707879 0.707879 -p 0 -0.383101 0.924889 -p 0 0 1.001092 -p -0.383101 0 0.924889 -p -0.707879 0 0.707879 -p -0.924889 0 0.383101 -p -1.001092 0 0 -p -2 0 0 -p -1.001092 0 0 -p -0.924889 0 -0.383101 -p -0.707879 0 -0.707879 -p -0.383101 0 -0.924889 -p 0 0 -1.001092 -p 0.383101 0 -0.924889 -p 0.707879 0 -0.707879 -p 0.924889 0 -0.383101 -p 1.001092 0 0 -p 2 0 0 -p 1.001092 0 0 -p 0.924889 0.383101 0 -p 0.707879 0.707879 0 -p 0.383101 0.924889 0 -p 0 1.001092 0 -p -0.383101 0.924889 0 -p -0.707879 0.707879 0 -p -0.924889 0.383101 0 -p -1.001092 0 0 -p -0.924889 -0.383101 0 -p -0.707879 -0.707879 0 -p -0.383101 -0.924889 0 -p 0 -1.001092 0 -p 0.383101 -0.924889 0 -p 0.707879 -0.707879 0 -p 0.924889 -0.383101 0 -p 1.001092 0 0 -p 0.924889 0 0.383101 -p 0.707879 0 0.707879 -p 0.383101 0 0.924889 -p 0 0 1.001092 -p 0 0 0 -p 0 0 -1.001092 -p 0 0 0 -p 1.001092 0 0 -p 0 0 0 -p -1.001092 0 0 -p 0 0 0 -p 0 -1.001092 0 -p 0 0 0 -p 0 1.001092 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 -k 69 ;")
L_hindPole=cmds.rename(L_hindPole_TMP,'PV_L_Hind')
cmds.scale(distance/3,distance/3,distance/3)    
cmds.makeIdentity(L_hindPole,apply=True,t=1,r=1,s=1,n=0)
L_hindPoleGrp=cmds.group(L_hindPole,n='L_hindPoleVectorCtrl_GRP')
constr=cmds.parentConstraint(hindKnee,L_hindPoleGrp)
cmds.delete(constr)
addDist=cmds.getAttr(L_hindPoleGrp+'.tz')
cmds.setAttr(L_hindPoleGrp+'.tz',addDist*2)

cmds.poleVectorConstraint(L_hindPole,L_Ik[0])
cmds.setAttr(L_Ik[0]+'.twist',180)
# r hind IK
R_hindPole_TMP=mel.eval("curve -d 1 -p 0 0 2 -p 0 0 1.001092 -p 0 0.383101 0.924889 -p 0 0.707879 0.707879 -p 0 0.924889 0.383101 -p 0 1.001092 0 -p 0 2 0 -p 0 1.001092 0 -p 0 0.924889 -0.383101 -p 0 0.707879 -0.707879 -p 0 0.383101 -0.924889 -p 0 0 -1.001092 -p 0 0 -2 -p 0 0 -1.001092 -p 0 -0.383101 -0.924889 -p 0 -0.707879 -0.707879 -p 0 -0.924889 -0.383101 -p 0 -1.001092 0 -p 0 -2 0 -p 0 -1.001092 0 -p 0 -0.924889 0.383101 -p 0 -0.707879 0.707879 -p 0 -0.383101 0.924889 -p 0 0 1.001092 -p -0.383101 0 0.924889 -p -0.707879 0 0.707879 -p -0.924889 0 0.383101 -p -1.001092 0 0 -p -2 0 0 -p -1.001092 0 0 -p -0.924889 0 -0.383101 -p -0.707879 0 -0.707879 -p -0.383101 0 -0.924889 -p 0 0 -1.001092 -p 0.383101 0 -0.924889 -p 0.707879 0 -0.707879 -p 0.924889 0 -0.383101 -p 1.001092 0 0 -p 2 0 0 -p 1.001092 0 0 -p 0.924889 0.383101 0 -p 0.707879 0.707879 0 -p 0.383101 0.924889 0 -p 0 1.001092 0 -p -0.383101 0.924889 0 -p -0.707879 0.707879 0 -p -0.924889 0.383101 0 -p -1.001092 0 0 -p -0.924889 -0.383101 0 -p -0.707879 -0.707879 0 -p -0.383101 -0.924889 0 -p 0 -1.001092 0 -p 0.383101 -0.924889 0 -p 0.707879 -0.707879 0 -p 0.924889 -0.383101 0 -p 1.001092 0 0 -p 0.924889 0 0.383101 -p 0.707879 0 0.707879 -p 0.383101 0 0.924889 -p 0 0 1.001092 -p 0 0 0 -p 0 0 -1.001092 -p 0 0 0 -p 1.001092 0 0 -p 0 0 0 -p -1.001092 0 0 -p 0 0 0 -p 0 -1.001092 0 -p 0 0 0 -p 0 1.001092 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 -k 69 ;")
R_hindPole=cmds.rename(R_hindPole_TMP,'PV_R_Hind')
cmds.scale(distance/3,distance/3,distance/3)    
cmds.makeIdentity(R_hindPole,apply=True,t=1,r=1,s=1,n=0)
R_hindPoleGrp=cmds.group(R_hindPole,n='R_hindPoleVectorCtrl_GRP')
constr=cmds.parentConstraint(hindKnee,R_hindPoleGrp)
cmds.delete(constr)
cmds.setAttr(R_hindPoleGrp+'.tz',addDist*2)

revDist=cmds.getAttr(R_hindPoleGrp+'.tx')
cmds.setAttr(R_hindPoleGrp+'.tx',-revDist)
cmds.poleVectorConstraint(R_hindPole,R_Ik[0])
cmds.setAttr(R_Ik[0]+'.twist',180)
# l front IK
L_frontPole_TMP=mel.eval("curve -d 1 -p 0 0 2 -p 0 0 1.001092 -p 0 0.383101 0.924889 -p 0 0.707879 0.707879 -p 0 0.924889 0.383101 -p 0 1.001092 0 -p 0 2 0 -p 0 1.001092 0 -p 0 0.924889 -0.383101 -p 0 0.707879 -0.707879 -p 0 0.383101 -0.924889 -p 0 0 -1.001092 -p 0 0 -2 -p 0 0 -1.001092 -p 0 -0.383101 -0.924889 -p 0 -0.707879 -0.707879 -p 0 -0.924889 -0.383101 -p 0 -1.001092 0 -p 0 -2 0 -p 0 -1.001092 0 -p 0 -0.924889 0.383101 -p 0 -0.707879 0.707879 -p 0 -0.383101 0.924889 -p 0 0 1.001092 -p -0.383101 0 0.924889 -p -0.707879 0 0.707879 -p -0.924889 0 0.383101 -p -1.001092 0 0 -p -2 0 0 -p -1.001092 0 0 -p -0.924889 0 -0.383101 -p -0.707879 0 -0.707879 -p -0.383101 0 -0.924889 -p 0 0 -1.001092 -p 0.383101 0 -0.924889 -p 0.707879 0 -0.707879 -p 0.924889 0 -0.383101 -p 1.001092 0 0 -p 2 0 0 -p 1.001092 0 0 -p 0.924889 0.383101 0 -p 0.707879 0.707879 0 -p 0.383101 0.924889 0 -p 0 1.001092 0 -p -0.383101 0.924889 0 -p -0.707879 0.707879 0 -p -0.924889 0.383101 0 -p -1.001092 0 0 -p -0.924889 -0.383101 0 -p -0.707879 -0.707879 0 -p -0.383101 -0.924889 0 -p 0 -1.001092 0 -p 0.383101 -0.924889 0 -p 0.707879 -0.707879 0 -p 0.924889 -0.383101 0 -p 1.001092 0 0 -p 0.924889 0 0.383101 -p 0.707879 0 0.707879 -p 0.383101 0 0.924889 -p 0 0 1.001092 -p 0 0 0 -p 0 0 -1.001092 -p 0 0 0 -p 1.001092 0 0 -p 0 0 0 -p -1.001092 0 0 -p 0 0 0 -p 0 -1.001092 0 -p 0 0 0 -p 0 1.001092 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 -k 69 ;")
L_frontPole=cmds.rename(L_frontPole_TMP,'PV_L_Front')
cmds.scale(distance/3,distance/3,distance/3)    
cmds.makeIdentity(L_frontPole,apply=True,t=1,r=1,s=1,n=0)

L_frontPoleGrp=cmds.group(L_frontPole,n='L_frontPoleVecorCtrl_GRP')
constr=cmds.parentConstraint(frontKnee,L_frontPoleGrp)
cmds.delete(constr)
addDist=cmds.getAttr(L_frontPoleGrp+'.tz')
cmds.setAttr(L_frontPoleGrp+'.tz', distance*2)
blueCol(L_frontPole)
cmds.poleVectorConstraint(L_frontPole,L_FIk[0])

# r front IK
R_frontPole_TMP=mel.eval("curve -d 1 -p 0 0 2 -p 0 0 1.001092 -p 0 0.383101 0.924889 -p 0 0.707879 0.707879 -p 0 0.924889 0.383101 -p 0 1.001092 0 -p 0 2 0 -p 0 1.001092 0 -p 0 0.924889 -0.383101 -p 0 0.707879 -0.707879 -p 0 0.383101 -0.924889 -p 0 0 -1.001092 -p 0 0 -2 -p 0 0 -1.001092 -p 0 -0.383101 -0.924889 -p 0 -0.707879 -0.707879 -p 0 -0.924889 -0.383101 -p 0 -1.001092 0 -p 0 -2 0 -p 0 -1.001092 0 -p 0 -0.924889 0.383101 -p 0 -0.707879 0.707879 -p 0 -0.383101 0.924889 -p 0 0 1.001092 -p -0.383101 0 0.924889 -p -0.707879 0 0.707879 -p -0.924889 0 0.383101 -p -1.001092 0 0 -p -2 0 0 -p -1.001092 0 0 -p -0.924889 0 -0.383101 -p -0.707879 0 -0.707879 -p -0.383101 0 -0.924889 -p 0 0 -1.001092 -p 0.383101 0 -0.924889 -p 0.707879 0 -0.707879 -p 0.924889 0 -0.383101 -p 1.001092 0 0 -p 2 0 0 -p 1.001092 0 0 -p 0.924889 0.383101 0 -p 0.707879 0.707879 0 -p 0.383101 0.924889 0 -p 0 1.001092 0 -p -0.383101 0.924889 0 -p -0.707879 0.707879 0 -p -0.924889 0.383101 0 -p -1.001092 0 0 -p -0.924889 -0.383101 0 -p -0.707879 -0.707879 0 -p -0.383101 -0.924889 0 -p 0 -1.001092 0 -p 0.383101 -0.924889 0 -p 0.707879 -0.707879 0 -p 0.924889 -0.383101 0 -p 1.001092 0 0 -p 0.924889 0 0.383101 -p 0.707879 0 0.707879 -p 0.383101 0 0.924889 -p 0 0 1.001092 -p 0 0 0 -p 0 0 -1.001092 -p 0 0 0 -p 1.001092 0 0 -p 0 0 0 -p -1.001092 0 0 -p 0 0 0 -p 0 -1.001092 0 -p 0 0 0 -p 0 1.001092 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 -k 69 ;")
R_frontPole=cmds.rename(R_frontPole_TMP,'PV_R_Front')
cmds.scale(distance/3,distance/3,distance/3)    
cmds.makeIdentity(R_frontPole,apply=True,t=1,r=1,s=1,n=0)
R_frontPoleGrp=cmds.group(R_frontPole,n='R_frontPoleVecorCtrl_GRP')
constr=cmds.parentConstraint(frontKnee,R_frontPoleGrp)
cmds.delete(constr)
addDist=cmds.getAttr(R_frontPoleGrp+'.tz')
cmds.setAttr(R_frontPoleGrp+'.tz', distance*2)
revDist=cmds.getAttr(R_frontPoleGrp+'.tx')
cmds.setAttr(R_frontPoleGrp+'.tx',-revDist)
cmds.poleVectorConstraint(R_frontPole,R_FIk[0])

# group IK...
poleVectorGrp=cmds.group(L_frontPoleGrp,R_frontPoleGrp,L_hindPoleGrp,R_hindPoleGrp,n='c_poleVector_GRP')
IkCtrlGrp=cmds.group(poleVectorGrp,R_frontLegRotationGrp,L_frontLegRotationGrp,R_frontIkCtrlGrp,L_frontIkCtrlGrp,R_hindIkCtrlGrp,L_hindIkCtrlGrp, n='c_IkCtrl_GRP')

''' fk leg setup '''
''' fk leg setup '''
# l fk hind leg...
L_hindLegFkCtrl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='l_hindLegFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_hindLegFkCtrl,apply=True, t=1, r=1, s=1, n=0)
L_hindLegFkCtrlGrp=cmds.group(L_hindLegFkCtrl,n='l_hindLegFkCtrl GRP')
constr=cmds.pointConstraint(L_hindFemurFKjnt,L_hindLegFkCtrlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(L_hindLegFkCtrlGrp,L_hindFemurFKjnt,mo=True)


L_hindUpperKneeFkCtrl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='l_hindUpperKneeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_hindUpperKneeFkCtrl,apply=True, t=1, r=1, s=1, n=0)
L_hindUpperKneeFkCtrlGrp=cmds.group(L_hindUpperKneeFkCtrl,n='l_hindUpperKneeFKCtrl GRP')
constr=cmds.pointConstraint(L_hindUpperKneeFKjnt,L_hindUpperKneeFkCtrlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(L_hindUpperKneeFkCtrl,L_hindUpperKneeFKjnt,mo=True)


L_hindKneeFkCtrl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='l_hindKneeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_hindKneeFkCtrl,apply=True, t=1, r=1, s=1, n=0)
L_hindKneeFkCtrlGrp=cmds.group(L_hindKneeFkCtrl,n='l_hindKneeFKCtrl GRP')
constr=cmds.pointConstraint(L_hindKneeFKjnt,L_hindKneeFkCtrlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(L_hindKneeFkCtrl,L_hindKneeFKjnt,mo=True)


L_hindAnkleFkCtrl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='l_hindAnkleFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_hindAnkleFkCtrl,apply=True, t=1, r=1, s=1, n=0)
L_hindAnkleFkCtrlGrp=cmds.group(L_hindAnkleFkCtrl,n='l_hindAnkleFKCtrl GRP')
constr=cmds.pointConstraint(L_hindAnkleFKjnt,L_hindAnkleFkCtrlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(L_hindAnkleFkCtrl,L_hindAnkleFKjnt,mo=True)


L_hindToeFkCtrl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='l_hindToeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_hindToeFkCtrl,apply=True, t=1, r=1, s=1, n=0)
L_hindToeFkCtrlGrp=cmds.group(L_hindToeFkCtrl,n='l_hindToeFKCtrl_GRP')
constr=cmds.pointConstraint(L_hindToeFKjnt,L_hindToeFkCtrlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(L_hindToeFkCtrl,L_hindToeFKjnt,mo=True)

# parent fk...
cmds.parent(L_hindToeFkCtrlGrp,L_hindAnkleFkCtrl[0])
cmds.parent(L_hindAnkleFkCtrlGrp,L_hindKneeFkCtrl[0])
cmds.parent(L_hindKneeFkCtrlGrp,L_hindUpperKneeFkCtrl[0])
cmds.parent(L_hindUpperKneeFkCtrlGrp,L_hindLegFkCtrl[0])
blueCol(L_hindLegFkCtrl[0])
cmds.parentConstraint(hindPelvisJnt,L_hindLegFkCtrlGrp,mo=True)

# r fk hind leg...
R_hindLegFkCtrl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='r_hindLegFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_hindLegFkCtrl,apply=True, t=1, r=1, s=1, n=0)
R_hindLegFkCtrlGrp=cmds.group(R_hindLegFkCtrl,n='r_hindLegFkCtrl GRP')
constr=cmds.pointConstraint(R_hindFemurFKjnt,R_hindLegFkCtrlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(R_hindLegFkCtrlGrp,R_hindFemurFKjnt,mo=True)


R_hindUpperKneeFkCtrl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='r_hindUpperKneeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_hindUpperKneeFkCtrl,apply=True, t=1, r=1, s=1, n=0)
R_hindUpperKneeFkCtrlGrp=cmds.group(R_hindUpperKneeFkCtrl,n='r_hindUpperKneeFKCtrl GRP')
constr=cmds.pointConstraint(R_hindUpperKneeFKjnt,R_hindUpperKneeFkCtrlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(R_hindUpperKneeFkCtrl,R_hindUpperKneeFKjnt,mo=True)


R_hindKneeFkCtrl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='r_hindKneeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_hindKneeFkCtrl,apply=True, t=1, r=1, s=1, n=0)
R_hindKneeFkCtrlGrp=cmds.group(R_hindKneeFkCtrl,n='r_hindKneeFKCtrl GRP')
constr=cmds.pointConstraint(R_hindKneeFKjnt,R_hindKneeFkCtrlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(R_hindKneeFkCtrl,R_hindKneeFKjnt,mo=True)


R_hindAnkleFkCtrl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='r_hindAnkleFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_hindAnkleFkCtrl,apply=True, t=1, r=1, s=1, n=0)
R_hindAnkleFkCtrlGrp=cmds.group(R_hindAnkleFkCtrl,n='r_hindAnkleFKCtrl GRP')
constr=cmds.pointConstraint(R_hindAnkleFKjnt,R_hindAnkleFkCtrlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(R_hindAnkleFkCtrl,R_hindAnkleFKjnt,mo=True)


R_hindToeFkCtrl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='R_hindToeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_hindToeFkCtrl,apply=True, t=1, r=1, s=1, n=0)
R_hindToeFkCtrlGrp=cmds.group(R_hindToeFkCtrl,n='r_hindToeFKCtrR_GRP')
constr=cmds.pointConstraint(R_hindToeFKjnt,R_hindToeFkCtrlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(R_hindToeFkCtrl,R_hindToeFKjnt,mo=True)


# parent fk...
cmds.parent(R_hindToeFkCtrlGrp,R_hindAnkleFkCtrl[0])
cmds.parent(R_hindAnkleFkCtrlGrp,R_hindKneeFkCtrl[0])
cmds.parent(R_hindKneeFkCtrlGrp,R_hindUpperKneeFkCtrl[0])
cmds.parent(R_hindUpperKneeFkCtrlGrp,R_hindLegFkCtrl[0])
cmds.parentConstraint(hindPelvisJnt,R_hindLegFkCtrlGrp,mo=True)

# l fk front leg...
L_frontLegFkCtrl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='l_frontLegFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_frontLegFkCtrl,apply=True, t=1, r=1, s=1, n=0)
L_frontLegFkCtrlGrp=cmds.group(L_frontLegFkCtrl,n='l_frontLegFkCtrl GRP')
constr=cmds.pointConstraint(L_frontFemurFKjnt,L_frontLegFkCtrlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(L_frontLegFkCtrlGrp,L_frontFemurFKjnt,mo=True)


L_frontUpperKneeFkCtrl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='l_frontUpperKneeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_frontUpperKneeFkCtrl,apply=True, t=1, r=1, s=1, n=0)
L_frontUpperKneeFkCtrlGrp=cmds.group(L_frontUpperKneeFkCtrl,n='l_frontUpperKneeFKCtrl GRP')
constr=cmds.pointConstraint(L_frontUpperKneeFKjnt,L_frontUpperKneeFkCtrlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(L_frontUpperKneeFkCtrl,L_frontUpperKneeFKjnt,mo=True)


L_frontKneeFkCtrl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='l_frontKneeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_frontKneeFkCtrl,apply=True, t=1, r=1, s=1, n=0)
L_frontKneeFkCtrlGrp=cmds.group(L_frontKneeFkCtrl,n='l_frontKneeFKCtrl GRP')
constr=cmds.pointConstraint(L_frontKneeFKjnt,L_frontKneeFkCtrlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(L_frontKneeFkCtrl,L_frontKneeFKjnt,mo=True)


L_frontAnkleFkCtrl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='l_frontAnkleFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_frontAnkleFkCtrl,apply=True, t=1, r=1, s=1, n=0)
L_frontAnkleFkCtrlGrp=cmds.group(L_frontAnkleFkCtrl,n='l_frontAnkleFKCtrl GRP')
constr=cmds.pointConstraint(L_frontAnkleFKjnt,L_frontAnkleFkCtrlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(L_frontAnkleFkCtrl,L_frontAnkleFKjnt,mo=True)


L_frontToeFkCtrl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='l_frontToeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_frontToeFkCtrl,apply=True, t=1, r=1, s=1, n=0)
L_frontToeFkCtrlGrp=cmds.group(L_frontToeFkCtrl,n='l_frontToeFKCtrl_GRP')
constr=cmds.pointConstraint(L_frontToeFKjnt,L_frontToeFkCtrlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(L_frontToeFkCtrl,L_frontToeFKjnt,mo=True)

# parent fk...
cmds.parent(L_frontToeFkCtrlGrp,L_frontAnkleFkCtrl[0])
cmds.parent(L_frontAnkleFkCtrlGrp,L_frontKneeFkCtrl[0])
cmds.parent(L_frontKneeFkCtrlGrp,L_frontUpperKneeFkCtrl[0])
cmds.parent(L_frontUpperKneeFkCtrlGrp,L_frontLegFkCtrl[0])
blueCol(L_frontLegFkCtrl[0])
cmds.parentConstraint(frontPelvisJnt,L_frontLegFkCtrlGrp,mo=True)

# r fk front leg...
R_frontLegFkCtrl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='r_frontLegFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_frontLegFkCtrl,apply=True, t=1, r=1, s=1, n=0)
R_frontLegFkCtrlGrp=cmds.group(R_frontLegFkCtrl,n='r_frontLegFkCtrl GRP')
constr=cmds.pointConstraint(R_frontFemurFKjnt,R_frontLegFkCtrlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(R_frontLegFkCtrlGrp,R_frontFemurFKjnt,mo=True)


R_frontUpperKneeFkCtrl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='r_frontUpperKneeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_frontUpperKneeFkCtrl,apply=True, t=1, r=1, s=1, n=0)
R_frontUpperKneeFkCtrlGrp=cmds.group(R_frontUpperKneeFkCtrl,n='r_frontUpperKneeFKCtrl GRP')
constr=cmds.pointConstraint(R_frontUpperKneeFKjnt,R_frontUpperKneeFkCtrlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(R_frontUpperKneeFkCtrl,R_frontUpperKneeFKjnt,mo=True)


R_frontKneeFkCtrl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='r_frontKneeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_frontKneeFkCtrl,apply=True, t=1, r=1, s=1, n=0)
R_frontKneeFkCtrlGrp=cmds.group(R_frontKneeFkCtrl,n='r_frontKneeFKCtrl GRP')
constr=cmds.pointConstraint(R_frontKneeFKjnt,R_frontKneeFkCtrlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(R_frontKneeFkCtrl,R_frontKneeFKjnt,mo=True)


R_frontAnkleFkCtrl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='r_frontAnkleFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_frontAnkleFkCtrl,apply=True, t=1, r=1, s=1, n=0)
R_frontAnkleFkCtrlGrp=cmds.group(R_frontAnkleFkCtrl,n='r_frontAnkleFKCtrl GRP')
constr=cmds.pointConstraint(R_frontAnkleFKjnt,R_frontAnkleFkCtrlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(R_frontAnkleFkCtrl,R_frontAnkleFKjnt,mo=True)


R_frontToeFkCtrl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='R_frontToeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_frontToeFkCtrl,apply=True, t=1, r=1, s=1, n=0)
R_frontToeFkCtrlGrp=cmds.group(R_frontToeFkCtrl,n='r_frontToeFKCtrR_GRP')
constr=cmds.pointConstraint(R_frontToeFKjnt,R_frontToeFkCtrlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(R_frontToeFkCtrl,R_frontToeFKjnt,mo=True)


# parent fk...
cmds.parent(R_frontToeFkCtrlGrp,R_frontAnkleFkCtrl[0])
cmds.parent(R_frontAnkleFkCtrlGrp,R_frontKneeFkCtrl[0])
cmds.parent(R_frontKneeFkCtrlGrp,R_frontUpperKneeFkCtrl[0])
cmds.parent(R_frontUpperKneeFkCtrlGrp,R_frontLegFkCtrl[0])

cmds.parentConstraint(frontPelvisJnt,R_frontLegFkCtrlGrp,mo=True)

# group fk controllers...
FlCtrlGrp=cmds.group(L_hindLegFkCtrlGrp,R_hindLegFkCtrlGrp,L_frontLegFkCtrlGrp,R_frontLegFkCtrlGrp, n='c_FKCtrl_GRP')



#SWITCH




                           #TAIL SETUP


#Calculating the distance btw locators using dist nodes

dist=cmds.createNode('distanceDimShape',n='delete thisnode')
tailStart=cmds.xform(tail1,q=1,ws=True,rp=True)
tailEnd=cmds.xform(tail2,q=1,ws=True,rp=True)
cmds.setAttr(dist+'.endPoint',*(tailEnd))
cmds.setAttr(dist+'.startPoint',*(tailStart))
distance=cmds.getAttr(dist+'.distance')
cmds.delete(cmds.listRelatives(dist,p=True))

#Setting up joints for tail
initialAmountOfJoint=5
amountOfJoints=initialAmountOfJoint-1
cmds.select(d=True)
tailRootJnt=cmds.joint(n='jnt_tail05')
while amountOfJoints > 0:
     tailJnt=cmds.joint(n='jnt_tail'+str(amountOfJoints))
     amountOfJoints-=1
cmds.select(tailRootJnt,hi=True)
tailJointChain=cmds.ls(sl=True) 

#Calculating distance btw each joint

amountOfJoints=initialAmountOfJoint-1   #defining initialAmountOfJoints again otherwise it will take value of 672,when loops end,it's value will be -1 )
distancePerJoint=distance/amountOfJoints

for i in tailJointChain :
    cmds.setAttr(i+'.tz',-distancePerJoint)

cmds.setAttr(tailRootJnt+'.tz',0)
constr=cmds.pointConstraint(tail1,tailJointChain[0])     
    
                
# rotate joint to aim for the end of the chain...
tempcon=cmds.aimConstraint(tail2,tailRootJnt, aimVector=(0,0,-1))
rotation=cmds.getAttr(tailRootJnt+'.rx')
cmds.delete(tempcon)
cmds.parent(tailJointChain[1],w=True)
cmds.setAttr(tailRootJnt+'.rx',0)
cmds.setAttr(tailRootJnt+'.ry',0)
cmds.setAttr(tailRootJnt+'.rz',0)
cmds.parent(tailJointChain[1],tailRootJnt)
cmds.joint(e=True, zso=True, oj='xyz', secondaryAxisOrient='yup', ch=True)


#Creating IK Solver
IkTailHandle=cmds.ikHandle(sol='ikSplineSolver',ns=4,n='IkSolver_Tail',ee=tailJointChain[-1],sj=tailRootJnt)
IkHandleGrp=cmds.group(IkTailHandle[0],IkTailHandle[2],n='IK_Tail_Grp')
cmds.setAttr(IkHandleGrp+'.inheritsTransform',0)
cmds.rename(IkTailHandle[1],'IkTail_effector')
cmds.rename(IkTailHandle[2],'IkTail_SolverCurve')

#Creating clusters for tail

cmds.select('IkTail_SolverCurve.cv[1:2]')
Cl01=cmds.cluster(rel=True,n='cluster_TailRoot')

cmds.select('IkTail_SolverCurve.cv[2:3]')
Cl02=cmds.cluster(rel=True,n='cluster_TailMid')

cmds.select('IkTail_SolverCurve.cv[3:4]')
Cl03=cmds.cluster(rel=True,n='cluster_TailEnd')
 
 #Grouping the clusters

Cl01Grp=cmds.group(Cl01,n='Offset_ClusterTail01')
Cl02Grp=cmds.group(Cl02,n='Offset_ClusterTail02')
Cl03Grp=cmds.group(Cl03,n='Offset_ClusterTail03')

#Move all the clusters in IkHandle group
cmds.parent(Cl01Grp,Cl02Grp,Cl03Grp,IkHandleGrp)

# a left over cv to be static in rig...
cmds.select('IkTail_SolverCurve.cv[0]')
Cl04=cmds.cluster( rel=True, n='c_neutral_cls')
Cl04Grp=cmds.group(Cl04, n='Offset_ClusterTail03')

#Creating Controllers for tail
 
tailCtrl1=cmds.circle(nr=(0,0,1),c=(0,0,0),n='Ctrl_TailRoot')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(tailCtrl1,apply=True,t=1,r=1,s=1,n=0)
tailCtrl1Grp=cmds.group(tailCtrl1,n='Offset_TailRoot')

tailCtrl2=cmds.circle(nr=(0,0,1),c=(0,0,0),n='Ctrl_TailMid')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(tailCtrl2,apply=True,t=1,r=1,s=1,n=0)
tailCtrl2Grp=cmds.group(tailCtrl2,n='Offset_TailMid')

tailCtrl3=cmds.circle(nr=(0,0,1),c=(0,0,0),n='Ctrl_TailEnd')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(tailCtrl3,apply=True,t=1,r=1,s=1,n=0)
tailCtrl3Grp=cmds.group(tailCtrl3,n='Offset_TailEnd')


 #Placing controllers on joints

cmds.setAttr(tailCtrl1Grp+'.rx',rotation)
cmds.setAttr(tailCtrl2Grp+'.rx',rotation)
cmds.setAttr(tailCtrl3Grp+'.rx',rotation)

clsXform=cmds.xform(Cl01[1], piv=True,q=True)
cmds.setAttr(tailCtrl1Grp+'.tx',clsXform[0])
cmds.setAttr(tailCtrl1Grp+'.ty',clsXform[1])
cmds.setAttr(tailCtrl1Grp+'.tz',clsXform[2])

clsXform=cmds.xform(Cl02[1], piv=True, q=True)
cmds.setAttr(tailCtrl2Grp+'.tx',clsXform[0])
cmds.setAttr(tailCtrl2Grp+'.ty',clsXform[1])
cmds.setAttr(tailCtrl2Grp+'.tz',clsXform[2])

clsXform=cmds.xform(Cl03[1], piv=True, q=True)
cmds.setAttr(tailCtrl3Grp+'.tx',clsXform[0])
cmds.setAttr(tailCtrl3Grp+'.ty',clsXform[1])
cmds.setAttr(tailCtrl3Grp+'.tz',clsXform[2])


#Connecting tail controllers
#Putting parent constraint btw controller and cluster

cmds.parentConstraint(tailCtrl1,Cl01,mo=True)
cmds.parentConstraint(tailCtrl2,Cl02,mo=True)
cmds.parentConstraint(tailCtrl3,Cl03,mo=True)   

#FK Controller for Tail-

tailFkCtrl1=cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)], k=[0,1,2,3,4], n='FkCtrl_Tail01')
cmds.scale(distance/4,distance/4,distance/4)
cmds.makeIdentity(tailFkCtrl1,apply=True,t=1,r=1,s=1,n=0)
tailFkCtrlGrp=cmds.group(tailFkCtrl1, n='Offset_FkCtrl_Tail01')


tailFkCtrl2=cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)], k=[0,1,2,3,4], n='FkCtrl_Tail02')
cmds.scale(distance/4,distance/4,distance/4)
cmds.makeIdentity(tailFkCtrl2,apply=True,t=1,r=1,s=1,n=0)
tailFkCtrl2Grp=cmds.group(tailFkCtrl2, n='Offset_FkCtrl_Tail02')


rotation=cmds.getAttr(tailCtrl1Grp+'.rx')
cmds.setAttr(tailFkCtrlGrp+'.rx',rotation)
cmds.setAttr(tailFkCtrl2Grp+'.rx',rotation)
constr=cmds.pointConstraint(tailCtrl1,tailFkCtrlGrp)
cmds.delete(constr)
constr=cmds.pointConstraint(tailCtrl2,tailFkCtrl2Grp)
cmds.delete(constr)

# place pivot at tail root...
coordinate=cmds.xform(tail1, ws=True, t=True, q=True)
cmds.xform(tailFkCtrl1, piv=(coordinate), ws=True)
cmds.parent(tailFkCtrl2Grp, tailFkCtrl1)
cmds.parent(tailCtrl1Grp, tailFkCtrl1)
cmds.parent(tailCtrl2Grp,tailFkCtrl2)
cmds.parent(tailCtrl3Grp, tailFkCtrl2)

# group the tail elements...
tailGrp=cmds.group(tailRootJnt, IkHandleGrp, tailFkCtrlGrp, n='c_tailRig_GRP')
cmds.setAttr(IkHandleGrp+'.visibility', 0)

# parentConstraint the neutral cluster to make tail follow the parent group and enable scaling...
cmds.parentConstraint(tailFkCtrl1,Cl04, mo=True)

# twist and no twist
mult=cmds.shadingNode('multiplyDivide', asUtility=True, n='c_tailTwist_reverseValueRotation_multiply')
cmds.setAttr(mult+'.input2X',-1)
cmds.connectAttr(tailCtrl3[0]+'.rz',mult+'.input1X')
cmds.connectAttr(mult+'.outputX', IkTailHandle[0]+'.twist')





#Spine SETUP'''''''''''''

#Calculating the distance btw locators using dist nodes

dist=cmds.createNode('distanceDimShape',n='delete thisnode')
SpineStart=cmds.xform(hindPelvis,q=1,ws=True,rp=True)
SpineEnd=cmds.xform(frontPelvis,q=1,ws=True,rp=True)
cmds.setAttr(dist+'.endPoint',*(SpineEnd))
cmds.setAttr(dist+'.startPoint',*(SpineStart))
distance=cmds.getAttr(dist+'.distance')
cmds.delete(cmds.listRelatives(dist,p=True))

#Setting up joints for Spine
initialAmountOfJoint=8
amountOfJoints=initialAmountOfJoint-1
cmds.select(d=True)
SpineRootJnt=cmds.joint(n='jnt_Spine09')
while amountOfJoints > 0:
     SpineJnt=cmds.joint(n='jnt_Spine'+str(amountOfJoints))
     amountOfJoints-=1
cmds.select(SpineRootJnt,hi=True)
SpineJointChain=cmds.ls(sl=True) 

#Calculating distance btw each joint

amountOfJoints=initialAmountOfJoint-1   #defining initialAmountOfJoints again otherwise it will take value of 672,when loops end,it's value will be -1 )
distancePerJoint=distance/amountOfJoints

for i in SpineJointChain :
    cmds.setAttr(i+'.tz',-distancePerJoint)

cmds.setAttr(SpineRootJnt+'.tz',0)
constr=cmds.pointConstraint(frontPelvis,SpineJointChain[0])     
    
                
# rotate joint to aim for the end of the chain...
tempcon=cmds.aimConstraint(hindPelvis,SpineRootJnt, aimVector=(0,0,-1))
rotation=cmds.getAttr(SpineRootJnt+'.rx')
cmds.delete(tempcon)
cmds.parent(SpineJointChain[1],w=True)
cmds.setAttr(SpineRootJnt+'.rx',0)
cmds.setAttr(SpineRootJnt+'.ry',0)
cmds.setAttr(SpineRootJnt+'.rz',0)
cmds.parent(SpineJointChain[1],SpineRootJnt)
cmds.joint(e=True, zso=True, oj='xyz', secondaryAxisOrient='yup', ch=True)


#Creating IK Solver
IkSpineHandle=cmds.ikHandle(sol='ikSplineSolver',ns=4,n='IkSolver_Spine',ee=SpineJointChain[-1],sj=SpineRootJnt)
IkHandleGrp=cmds.group(IkSpineHandle[0],IkSpineHandle[2],n='IK_Spine_Grp')
cmds.setAttr(IkHandleGrp+'.inheritsTransform',0)
cmds.rename(IkSpineHandle[1],'IkSpine_effector')
cmds.rename(IkSpineHandle[2],'IkSpine_SolverCurve')

#Creating clusters for Spine

cmds.select('IkSpine_SolverCurve.cv[1:2]')
Cl01=cmds.cluster(rel=True,n='cluster_SpineRoot')

cmds.select('IkSpine_SolverCurve.cv[2:3]')
Cl02=cmds.cluster(rel=True,n='cluster_SpineMid')

cmds.select('IkSpine_SolverCurve.cv[3:4]')
Cl03=cmds.cluster(rel=True,n='cluster_SpineEnd')
 
 #Grouping the clusters

Cl01Grp=cmds.group(Cl01,n='Offset_ClusterSpine01')
Cl02Grp=cmds.group(Cl02,n='Offset_ClusterSpine02')
Cl03Grp=cmds.group(Cl03,n='Offset_ClusterSpine03')

#Move all the clusters in IkHandle group
cmds.parent(Cl01Grp,Cl02Grp,Cl03Grp,IkHandleGrp)

# a left over cv to be static in rig...
cmds.select('IkSpine_SolverCurve.cv[0]')
Cl04=cmds.cluster( rel=True, n='c_neutral_cls')
Cl04Grp=cmds.group(Cl04, n='Offset_ClusterSpine03')

#Creating Controllers for Spine
 
SpineCtrl1=cmds.circle(nr=(0,0,1),c=(0,0,0),n='Ctrl_SpineRoot')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(SpineCtrl1,apply=True,t=1,r=1,s=1,n=0)
SpineCtrl1Grp=cmds.group(SpineCtrl1,n='Offset_SpineRoot')

SpineCtrl2=cmds.circle(nr=(0,0,1),c=(0,0,0),n='Ctrl_SpineMid')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(SpineCtrl2,apply=True,t=1,r=1,s=1,n=0)
SpineCtrl2Grp=cmds.group(SpineCtrl2,n='Offset_SpineMid')

SpineCtrl3=cmds.circle(nr=(0,0,1),c=(0,0,0),n='Ctrl_SpineEnd')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(SpineCtrl3,apply=True,t=1,r=1,s=1,n=0)
SpineCtrl3Grp=cmds.group(SpineCtrl3,n='Offset_SpineEnd')


 #Placing controllers on joints

cmds.setAttr(SpineCtrl1Grp+'.rx',rotation)
cmds.setAttr(SpineCtrl2Grp+'.rx',rotation)
cmds.setAttr(SpineCtrl3Grp+'.rx',rotation)

clsXform=cmds.xform(Cl01[1], piv=True,q=True)
cmds.setAttr(SpineCtrl1Grp+'.tx',clsXform[0])
cmds.setAttr(SpineCtrl1Grp+'.ty',clsXform[1])
cmds.setAttr(SpineCtrl1Grp+'.tz',clsXform[2])

clsXform=cmds.xform(Cl02[1], piv=True, q=True)
cmds.setAttr(SpineCtrl2Grp+'.tx',clsXform[0])
cmds.setAttr(SpineCtrl2Grp+'.ty',clsXform[1])
cmds.setAttr(SpineCtrl2Grp+'.tz',clsXform[2])

clsXform=cmds.xform(Cl03[1], piv=True, q=True)
cmds.setAttr(SpineCtrl3Grp+'.tx',clsXform[0])
cmds.setAttr(SpineCtrl3Grp+'.ty',clsXform[1])
cmds.setAttr(SpineCtrl3Grp+'.tz',clsXform[2])


#Connecting Spine controllers
#Putting parent constraint btw controller and cluster

cmds.parentConstraint(SpineCtrl1,Cl01,mo=True)
cmds.parentConstraint(SpineCtrl2,Cl02,mo=True)
cmds.parentConstraint(SpineCtrl3,Cl03,mo=True)   

#FK Controller for Spine-

SpineFkCtrl1=cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)], k=[0,1,2,3,4], n='FkCtrl_Spine01')
cmds.scale(distance/4,distance/4,distance/4)
cmds.makeIdentity(SpineFkCtrl1,apply=True,t=1,r=1,s=1,n=0)
SpineFkCtrlGrp=cmds.group(SpineFkCtrl1, n='Offset_FkCtrl_Spine01')


SpineFkCtrl2=cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)], k=[0,1,2,3,4], n='FkCtrl_Spine02')
cmds.scale(distance/4,distance/4,distance/4)
cmds.makeIdentity(SpineFkCtrl2,apply=True,t=1,r=1,s=1,n=0)
SpineFkCtrl2Grp=cmds.group(SpineFkCtrl2, n='Offset_FkCtrl_Spine02')


rotation=cmds.getAttr(SpineCtrl1Grp+'.rx')
cmds.setAttr(SpineFkCtrlGrp+'.rx',rotation)
cmds.setAttr(SpineFkCtrl2Grp+'.rx',rotation)
constr=cmds.pointConstraint(SpineCtrl1,SpineFkCtrlGrp)
cmds.delete(constr)
constr=cmds.pointConstraint(SpineCtrl2,SpineFkCtrl2Grp)
cmds.delete(constr)

# connect Spine end to hind JNT...
cmds.parentConstraint(SpineCtrl1[0],SpineCtrl2Grp, mo=True)
cmds.parentConstraint(SpineCtrl3[0],SpineCtrl2Grp, mo=True)
cmds.parentConstraint(SpineCtrl1[0],frontPelvisJnt, mo=True)
cmds.parentConstraint(SpineCtrl3[0],hindPelvisJnt, mo=True)
cmds.parentConstraint(SpineCtrl3[0],tailFkCtrlGrp, mo=True)

# master Spine controller...
SpineMasterCtrl=cmds.curve(d=1, p=[(0.5,0.5,0.5),(0.5,0.5,-0.5),(-0.5,0.5,-0.5),(-0.5,-0.5,-0.5),(0.5,-0.5,-0.5),(0.5,0.5,-0.5),(-0.5,0.5,-0.5),(-0.5,0.5,0.5),(0.5,0.5,0.5),(0.5,-0.5,0.5),(0.5,-0.5,-0.5),(-0.5,-0.5,-0.5),(-0.5,-0.5,0.5),(0.5,-0.5,0.5),(-0.5,-0.5,0.5),(-0.5,0.5,0.5)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],n='c_SpineMaster_CTRL')
cmds.scale(distance/4,distance/4,distance*1.5)
cmds.makeIdentity(SpineMasterCtrl, apply=True, t=1, r=1, s=1, n=0)
SpineMasterCtrlGrp=cmds.group(SpineMasterCtrl, n='c_SpineMasterCtrl_GRP')
constr=cmds.pointConstraint(SpineFkCtrl2, SpineMasterCtrlGrp)
cmds.delete(constr)
dist=cmds.getAttr(SpineMasterCtrlGrp+'.ty')
cmds.setAttr(SpineMasterCtrlGrp+'.ty',dist*1.5)
cmds.parent(SpineFkCtrl2Grp, SpineFkCtrl1)
cmds.parent(SpineCtrl1Grp, SpineFkCtrl1)
cmds.parent(SpineCtrl2Grp,SpineFkCtrl2)
cmds.parent(SpineCtrl3Grp, SpineFkCtrl2)
cmds.parentConstraint(SpineCtrl1[0],Cl04, mo=True)

cmds.setAttr(IkHandleGrp+'.visibility',0)
SpineGrp=cmds.group(IkHandleGrp, SpineRootJnt, SpineFkCtrlGrp, n='c_SpineRig_GRP')






#Neck SETUP'''''''''''''

#Calculating the distance btw locators using dist nodes

dist=cmds.createNode('distanceDimShape',n='delete thisnode')
NeckStartPnt=cmds.xform(NeckRoot,q=1,ws=True,rp=True)
NeckEndPnt=cmds.xform(NeckEnd,q=1,ws=True,rp=True)
cmds.setAttr(dist+'.endPoint',*(NeckEndPnt))
cmds.setAttr(dist+'.startPoint',*(NeckStartPnt))
distance=cmds.getAttr(dist+'.distance')
cmds.delete(cmds.listRelatives(dist,p=True))

#Setting up joints for Neck
initialAmountOfJoint=8
amountOfJoints=initialAmountOfJoint-1
cmds.select(d=True)
NeckRootJnt=cmds.joint(n='jnt_Neck09')
while amountOfJoints > 0:
     NeckJnt=cmds.joint(n='jnt_Neck'+str(amountOfJoints))
     amountOfJoints-=1
cmds.select(NeckRootJnt,hi=True)
NeckJointChain=cmds.ls(sl=True) 

#Calculating distance btw each joint

amountOfJoints=initialAmountOfJoint-1   #defining initialAmountOfJoints again otherwise it will take value of 672,when loops end,it's value will be -1 )
distancePerJoint=distance/amountOfJoints

for i in NeckJointChain :
    cmds.setAttr(i+'.tz',-distancePerJoint)

cmds.setAttr(NeckRootJnt+'.tz',0)
cmds.rename(NeckJointChain[-1],NeckJointChain[-1]+'End')
constr=cmds.pointConstraint(NeckRoot,NeckJointChain[0])     
    
                
# rotate joint to aim for the end of the chain...
tempcon=cmds.aimConstraint(NeckEnd,NeckRootJnt, aimVector=(0,0,1))
rotation=cmds.getAttr(NeckRootJnt+'.rx')
cmds.delete(tempcon)
cmds.parent(NeckJointChain[1],w=True)
cmds.setAttr(NeckRootJnt+'.rx',0)
cmds.setAttr(NeckRootJnt+'.ry',0)
cmds.setAttr(NeckRootJnt+'.rz',0)
cmds.parent(NeckJointChain[1],NeckRootJnt)
cmds.joint(e=True, zso=True, oj='xyz', secondaryAxisOrient='yup', ch=True)


#Creating IK Solver
IkNeckHandle=cmds.ikHandle(sol='ikSplineSolver',ns=4,n='IkSolver_Neck',ee=NeckJointChain[-1]+'End',sj=NeckRootJnt)
IkHandleGrp=cmds.group(IkNeckHandle[0],IkNeckHandle[2],n='IK_Neck_Grp')
cmds.setAttr(IkHandleGrp+'.inheritsTransform',0)
cmds.rename(IkNeckHandle[1],'IkNeck_effector')
cmds.rename(IkNeckHandle[2],'IkNeck_SolverCurve')

#Creating clusters for Neck

cmds.select('IkNeck_SolverCurve.cv[1:2]')
Cl01=cmds.cluster(rel=True,n='cluster_NeckRoot')

cmds.select('IkNeck_SolverCurve.cv[2:3]')
Cl02=cmds.cluster(rel=True,n='cluster_NeckMid')

cmds.select('IkNeck_SolverCurve.cv[3:4]')
Cl03=cmds.cluster(rel=True,n='cluster_NeckEnd')
 
 #Grouping the clusters

Cl01Grp=cmds.group(Cl01,n='Offset_ClusterNeck01')
Cl02Grp=cmds.group(Cl02,n='Offset_ClusterNeck02')
Cl03Grp=cmds.group(Cl03,n='Offset_ClusterNeck03')

#Move all the clusters in IkHandle group
cmds.parent(Cl01Grp,Cl02Grp,Cl03Grp,IkHandleGrp)

# a left over cv to be static in rig...
cmds.select('IkNeck_SolverCurve.cv[0]')
Cl04=cmds.cluster( rel=True, n='c_neutral_cls')
Cl04Grp=cmds.group(Cl04, n='Offset_ClusterNeck03')

#Creating Controllers for Neck
 
NeckCtrl1=cmds.circle(nr=(0,0,1),c=(0,0,0),n='Ctrl_NeckRoot')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(NeckCtrl1,apply=True,t=1,r=1,s=1,n=0)
NeckCtrl1Grp=cmds.group(NeckCtrl1,n='Offset_NeckRoot')

NeckCtrl2=cmds.circle(nr=(0,0,1),c=(0,0,0),n='Ctrl_NeckMid')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(NeckCtrl2,apply=True,t=1,r=1,s=1,n=0)
NeckCtrl2Grp=cmds.group(NeckCtrl2,n='Offset_NeckMid')

NeckCtrl3=cmds.circle(nr=(0,0,1),c=(0,0,0),n='Ctrl_NeckEnd')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(NeckCtrl3,apply=True,t=1,r=1,s=1,n=0)
NeckCtrl3Grp=cmds.group(NeckCtrl3,n='Offset_NeckEnd')


 #Placing controllers on joints
cmds.setAttr(NeckCtrl1Grp+'.rx',rotation)
cmds.setAttr(NeckCtrl2Grp+'.rx',rotation)
cmds.setAttr(NeckCtrl3Grp+'.rx',rotation)

clsXform=cmds.xform(Cl01[1], piv=True,q=True)
cmds.setAttr(NeckCtrl1Grp+'.tx',clsXform[0])
cmds.setAttr(NeckCtrl1Grp+'.ty',clsXform[1])
cmds.setAttr(NeckCtrl1Grp+'.tz',clsXform[2])

clsXform=cmds.xform(Cl02[1], piv=True, q=True)
cmds.setAttr(NeckCtrl2Grp+'.tx',clsXform[0])
cmds.setAttr(NeckCtrl2Grp+'.ty',clsXform[1])
cmds.setAttr(NeckCtrl2Grp+'.tz',clsXform[2])

clsXform=cmds.xform(Cl03[1], piv=True, q=True)
cmds.setAttr(NeckCtrl3Grp+'.tx',clsXform[0])
cmds.setAttr(NeckCtrl3Grp+'.ty',clsXform[1])
cmds.setAttr(NeckCtrl3Grp+'.tz',clsXform[2])


#Connecting Neck controllers
#Putting parent constraint btw controller and cluster

cmds.parentConstraint(NeckCtrl1,Cl01,mo=True)
cmds.parentConstraint(NeckCtrl2,Cl02,mo=True)
cmds.parentConstraint(NeckCtrl3,Cl03,mo=True)   

#FK Controller for Neck-

NeckFkCtrl1=cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)], k=[0,1,2,3,4], n='FkCtrl_Neck01')
cmds.scale(distance/4,distance/4,distance/4)
cmds.makeIdentity(NeckFkCtrl1,apply=True,t=1,r=1,s=1,n=0)
NeckFkCtrlGrp=cmds.group(NeckFkCtrl1, n='Offset_FkCtrl_Neck01')


NeckFkCtrl2=cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)], k=[0,1,2,3,4], n='FkCtrl_Neck02')
cmds.scale(distance/4,distance/4,distance/4)
cmds.makeIdentity(NeckFkCtrl2,apply=True,t=1,r=1,s=1,n=0)
NeckFkCtrl2Grp=cmds.group(NeckFkCtrl2, n='Offset_FkCtrl_Neck02')


rotation=cmds.getAttr(NeckCtrl1Grp+'.rx')
cmds.setAttr(NeckFkCtrlGrp+'.rx',rotation)
cmds.setAttr(NeckFkCtrl2Grp+'.rx',rotation)
constr=cmds.pointConstraint(NeckCtrl1,NeckFkCtrlGrp)
cmds.delete(constr)
constr=cmds.pointConstraint(NeckCtrl2,NeckFkCtrl2Grp)
cmds.delete(constr)

# connect neck controllers...
cmds.parentConstraint(NeckCtrl1,Cl01, mo=True, n='c_neckRoot_controller')
cmds.parentConstraint(NeckCtrl2,Cl02, mo=True, n='c_neckMid_controller')
cmds.parentConstraint(NeckCtrl3,Cl03, mo=True, n='c_neckPoint_controller')

# neck FK controllers...
NeckFkCtrl1=cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)], k=[0,1,2,3,4], n='c_Neck1FK_CTRL')
cmds.scale(distance/4,distance/4,distance/4)
cmds.makeIdentity(NeckFkCtrl1,apply=True,t=1,r=1,s=1,n=0)

NeckFkCtrlGrp=cmds.group(NeckFkCtrl1, n='c_NeckFkCtrl1_GRP')
NeckFkCtrl2=cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)], k=[0,1,2,3,4], n='c_Neck2FK_CTRL')
cmds.scale(distance/4,distance/4,distance/4)
cmds.makeIdentity(NeckFkCtrl2,apply=True,t=1,r=1,s=1,n=0)

NeckFkCtrl2Grp=cmds.group(NeckFkCtrl2, n='c_NeckFkCtrl2_GRP')
rotation=cmds.getAttr(NeckCtrl1Grp+'.rx')
cmds.setAttr(NeckFkCtrlGrp+'.rx',rotation)
cmds.setAttr(NeckFkCtrl2Grp+'.rx',rotation)
constr=cmds.pointConstraint(NeckCtrl1,NeckFkCtrlGrp)
cmds.delete(constr)
constr=cmds.pointConstraint(NeckCtrl2,NeckFkCtrl2Grp)
cmds.delete(constr)

# move Neck root pivot and parent controllers...
coordinate=cmds.xform(NeckRoot, ws=True, t=True, q=True)
cmds.xform(NeckFkCtrl1, piv=(coordinate), ws=True)
cmds.parent(NeckFkCtrl2Grp, NeckFkCtrl1)
cmds.parent(NeckCtrl1Grp, NeckFkCtrl1)
cmds.parent(NeckCtrl2Grp,NeckFkCtrl2)
cmds.parent(NeckCtrl3Grp, NeckFkCtrl2)

# cleanup...
cmds.setAttr(IkHandleGrp+'.visibility',0)
NeckGrp=cmds.group(NeckRootJnt,IkHandleGrp,NeckFkCtrlGrp, n='c_NeckRig_GRP')

#FOOT ROLL SETUP 

# l side hind...
cmds.select(d=True)
LHAnkleRotate=cmds.joint(n='l_hindAnkleRotate_JNT')
LHHeelJnt=cmds.joint(n='l_hindHeelRool_JNT')
LHBallJnt=cmds.joint(n='l_hindBallRool_JNT')
LHAnkleJnt=cmds.joint(n='l_hindAnkleRool_JNT')
constr=cmds.pointConstraint(L_hindAnkleJnt, LHAnkleRotate)
cmds.delete(constr)
constr=cmds.pointConstraint(L_hindToeJnt, LHHeelJnt)
cmds.delete(constr)
cmds.setAttr(LHHeelJnt+'.tz',0)
constr=cmds.pointConstraint(L_hindToeJnt, LHBallJnt)
cmds.delete(constr)
constr=cmds.pointConstraint(L_hindAnkleJnt, LHAnkleJnt)
cmds.delete(constr)
cmds.parent(L_Ik[0], LHAnkleJnt)
cmds.parent(L_IkToe[0], LHBallJnt)
coordinate=cmds.xform(LHAnkleRotate, ws=True, t=True, q=True)
cmds.xform(L_hindIkCtrl, piv=(coordinate), ws=True)
LHHeelCtrl=cmds.circle(nr=(1,0,0), r=distance/4, n='l_hindHeel_CTRL')
LHHeelCtrlGrp=cmds.group(n='l_hindHeelCtrl_GRP')
constr=cmds.pointConstraint(LHHeelJnt, LHHeelCtrl[0])
cmds.delete(constr)
LHToeTipCtrl=cmds.circle(nr=(1,0,0), r=distance/4, n='l_hindToeTip_CTRL')
LHToeTipCtrlGrp=cmds.group(n='l_hindToeTipCtrl_GRP')
constr=cmds.pointConstraint(LHBallJnt, LHToeTipCtrlGrp)
cmds.delete(constr)
cmds.parent(LHToeTipCtrlGrp, LHHeelCtrl[0])
cmds.parentConstraint(LHHeelCtrl[0], LHHeelJnt, mo=True)
cmds.parentConstraint(LHToeTipCtrl[0], LHBallJnt, mo=True)
cmds.parent(LHHeelCtrlGrp, L_hindIkCtrl)
cmds.parentConstraint(L_hindIkCtrl, LHAnkleRotate, mo=True)
cmds.setAttr(LHAnkleRotate+'.visibility',0)
# r side hind...
cmds.select(d=True)
RHAnkleRotate=cmds.joint(n='r_hindAnkleRotate_JNT')
RHHeelJnt=cmds.joint(n='r_hindHeelRool_JNT')
RHBallJnt=cmds.joint(n='r_hindBallRool_JNT')
RHAnkleJnt=cmds.joint(n='r_hindAnkleRool_JNT')
constr=cmds.pointConstraint(R_hindAnkleJnt, RHAnkleRotate)
cmds.delete(constr)
constr=cmds.pointConstraint(R_hindToeJnt, RHHeelJnt)
cmds.delete(constr)
cmds.setAttr(RHHeelJnt+'.tz',0)
constr=cmds.pointConstraint(R_hindToeJnt, RHBallJnt)
cmds.delete(constr)
constr=cmds.pointConstraint(R_hindAnkleJnt, RHAnkleJnt)
cmds.delete(constr)
cmds.parent(R_Ik[0], RHAnkleJnt)
cmds.parent(R_IkToe[0], RHBallJnt)
coordinate=cmds.xform(RHAnkleRotate, ws=True, t=True, q=True)
cmds.xform(R_hindIkCtrl, piv=(coordinate), ws=True)
RHHeelCtrl=cmds.circle(nr=(1,0,0), r=distance/4, n='r_hindHeel_CTRL')
RHHeelCtrlGrp=cmds.group(n='r_hindHeelCtrl_GRP')
constr=cmds.pointConstraint(RHHeelJnt, RHHeelCtrl[0])
cmds.delete(constr)
RHToeTipCtrl=cmds.circle(nr=(1,0,0), r=distance/4, n='r_hindToeTip_CTRL')
RHToeTipCtrlGrp=cmds.group(n='r_hindToeTipCtrl_GRP')
constr=cmds.pointConstraint(RHBallJnt, RHToeTipCtrlGrp)
cmds.delete(constr)
cmds.parent(RHToeTipCtrlGrp, RHHeelCtrl[0])
cmds.parentConstraint(RHHeelCtrl[0], RHHeelJnt, mo=True)
cmds.parentConstraint(RHToeTipCtrl[0], RHBallJnt, mo=True)
cmds.parent(RHHeelCtrlGrp, R_hindIkCtrl)
cmds.parentConstraint(R_hindIkCtrl, RHAnkleRotate, mo=True)
cmds.setAttr(RHAnkleRotate+'.visibility',0)
# l front leg...
cmds.select(d=True)
LFAnkleRotate=cmds.joint(n='l_frontAnkleRotate_JNT')
LFHeelJnt=cmds.joint(n='l_frontHeelRool_JNT')
LFBallJnt=cmds.joint(n='l_frontBallRool_JNT')
LFAnkleJnt=cmds.joint(n='l_frontAnkleRool_JNT')
constr=cmds.pointConstraint(L_frontAnkleJnt, LFAnkleRotate)
cmds.delete(constr)
constr=cmds.pointConstraint(L_frontToeJnt, LFHeelJnt)
cmds.delete(constr)
cmds.setAttr(LFHeelJnt+'.tz',0)
constr=cmds.pointConstraint(L_frontToeJnt, LFBallJnt)
cmds.delete(constr)
constr=cmds.pointConstraint(L_frontAnkleJnt, LFAnkleJnt)
cmds.delete(constr)
cmds.parent(L_FIk[0], LFAnkleJnt)
cmds.parent(L_FToeIk[0], LFBallJnt)
coordinate=cmds.xform(LFAnkleRotate, ws=True, t=True, q=True)
cmds.xform(L_frontIkCtrl, piv=(coordinate), ws=True)
LFHeelCtrl=cmds.circle(nr=(1,0,0), r=distance/4, n='l_frontHeel_CTRL')
LFHeelCtrlGrp=cmds.group(n='l_frontHeelCtrl_GRP')
constr=cmds.pointConstraint(LFHeelJnt, LFHeelCtrl[0])
cmds.delete(constr)
LFToeTipCtrl=cmds.circle(nr=(1,0,0), r=distance/4, n='l_frontToeTip_CTRL')
LFToeTipCtrlGrp=cmds.group(n='l_frontToeTipCtrl_GRP')
constr=cmds.pointConstraint(LFBallJnt, LFToeTipCtrlGrp)
cmds.delete(constr)
cmds.parent(LFToeTipCtrlGrp, LFHeelCtrl[0])
cmds.parentConstraint(LFHeelCtrl[0], LFHeelJnt, mo=True)
cmds.parentConstraint(LFToeTipCtrl[0], LFBallJnt, mo=True)
cmds.parent(LFHeelCtrlGrp, L_frontIkCtrl)
cmds.parentConstraint(L_frontIkCtrl, LFAnkleRotate, mo=True)
cmds.setAttr(LFAnkleRotate+'.visibility',0)
# r front leg...
cmds.select(d=True)
RFAnkleRotate=cmds.joint(n='r_frontAnkleRotate_JNT')
RFHeelJnt=cmds.joint(n='r_frontHeelRool_JNT')
RFBallJnt=cmds.joint(n='r_frontBallRool_JNT')
RFAnkleJnt=cmds.joint(n='r_frontAnkleRool_JNT')
constr=cmds.pointConstraint(R_frontAnkleJnt, RFAnkleRotate)
cmds.delete(constr)
constr=cmds.pointConstraint(R_frontToeJnt, RFHeelJnt)
cmds.delete(constr)
cmds.setAttr(RFHeelJnt+'.tz',0)
constr=cmds.pointConstraint(R_frontToeJnt, RFBallJnt)
cmds.delete(constr)
constr=cmds.pointConstraint(R_frontAnkleJnt, RFAnkleJnt)
cmds.delete(constr)
cmds.parent(R_FIk[0], RFAnkleJnt)
cmds.parent(R_FToeIk[0], RFBallJnt)
coordinate=cmds.xform(RFAnkleRotate, ws=True, t=True, q=True)
cmds.xform(R_frontIkCtrl, piv=(coordinate), ws=True)
RFHeelCtrl=cmds.circle(nr=(1,0,0), r=distance/4, n='r_frontHeel_CTRL')
RFHeelCtrlGrp=cmds.group(n='r_frontHeelCtrl_GRP')
constr=cmds.pointConstraint(RFHeelJnt, RFHeelCtrl[0])
cmds.delete(constr)
RFToeTipCtrl=cmds.circle(nr=(1,0,0), r=distance/4, n='r_frontToeTip_CTRL')
RFToeTipCtrlGrp=cmds.group(n='r_frontToeTipCtrl_GRP')
constr=cmds.pointConstraint(RFBallJnt, RFToeTipCtrlGrp)
cmds.delete(constr)
cmds.parent(RFToeTipCtrlGrp, RFHeelCtrl[0])
cmds.parentConstraint(RFHeelCtrl[0], RFHeelJnt, mo=True)
cmds.parentConstraint(RFToeTipCtrl[0], RFBallJnt, mo=True)
cmds.parent(RFHeelCtrlGrp, R_frontIkCtrl)
cmds.parentConstraint(R_frontIkCtrl, RFAnkleRotate, mo=True)
cmds.setAttr(RFAnkleRotate+'.visibility',0)

roolJntGrp=cmds.group(LFAnkleRotate,RFAnkleRotate,LHAnkleRotate,RHAnkleRotate, n='c_footRoolJnt_GRP')

# constraint front leg rotation ctrl to IK controller...
constrpoint=cmds.parentConstraint(frontPelvisJnt, L_frontLegRotationGrp, mo=True)
cmds.parentConstraint(L_frontLegRotation, L_frontFemurIKjnt, mo=True)
cmds.parentConstraint(L_frontIkCtrl, L_frontLegRotationGrp, mo=True)
cmds.setAttr(constrpoint[0]+'.l_frontIK_CTRLW1',.3)
constrpoint=cmds.parentConstraint(frontPelvisJnt, R_frontLegRotationGrp, mo=True)
cmds.parentConstraint(R_frontLegRotation, R_frontFemurIKjnt, mo=True)
cmds.parentConstraint(R_frontIkCtrl, R_frontLegRotationGrp, mo=True)
cmds.setAttr(constrpoint[0]+'.r_frontIK_CTRLW1',.3)


# nullify placement locators...
cmds.delete(mainLocGrp)

''' cleanup '''
''' cleanup '''
# group body...
cmds.parent(SpineGrp, SpineMasterCtrl)
rigGrp=cmds.group(tailGrp,legCtrlGrp,legSwitchGrp,SpineMasterCtrlGrp,NeckGrp, n='c_rig_GRP')
jntGrp=cmds.group(roolJntGrp,hindPelvisJnt,frontPelvisJnt,tailRootJnt,SpineRootJnt,NeckRootJnt, n='c_jnt_GRP')

cmds.parent(rigGrp,jntGrp,subworld)
cmds.setAttr(L_hindFemurIKjnt+'.visibility',0)
cmds.setAttr(R_hindFemurIKjnt+'.visibility',0)
cmds.setAttr(L_frontFemurIKjnt+'.visibility',0)
cmds.setAttr(R_frontFemurIKjnt+'.visibility',0)
