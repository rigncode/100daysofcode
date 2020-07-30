# camelCase
defineThisObject
# snake_case
define_this_object # better



# variable names
i = 12
shaders = 12 # better



#NAMING LOOPS
#Even a temporary loop variable needs a proper name


objects = ['pTorus', 'pCube', 'pCone']

#purely disaster
for i in objects:
    name=i.replace('p','obj_')
    print name

# clear
for object in objects:
    name=i.replace('p','obj_')
    print name
