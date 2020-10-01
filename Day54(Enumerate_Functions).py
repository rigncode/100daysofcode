#ENUMERATE FUNCTION


#GENERAL FUNCTION
names=['apple','banana','carrot','capsicum','raddish']
pos=0
for i in names:
    print ("{}------->{}".format(pos,i))
    pos+=1



#same thing can be achieved by using ENUMERATE

names=['apple','banana','carrot','capsicum','raddish']
for pos,i in enumerate(names):
    print("{}------>{}".format(pos,i))
