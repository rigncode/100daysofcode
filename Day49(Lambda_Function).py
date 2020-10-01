### LAMBDA FUNCTIONS #####


def add(a,b):   #function
    return a+b

new_add=lambda a,b:a+b #it can be written in Lambda    
print(new_add(2,3))

####################################################################################################################

def multiply(x,y):
    return x*y

new_multiply=lamda x,y:x*y
print(new_multiply(5,6))

#####################################################################################################################

def last_char(s):
    returns[-1]

lc=lambda s:s[-1] 
print(lc('abcxz'))

#############################################################################################################################
#if-else with lambda

def func(s):
    if len(s)>6:
        return True
    else:
        return False

func=lambda s: True if len(s)>6 else False
print(fnc('axcvbc'))


#It can also be done without if-else

def func(s):
    return len(s)>6

func=lambda s:len(s)>6
print(func('azx'))    


