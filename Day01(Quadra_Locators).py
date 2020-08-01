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
