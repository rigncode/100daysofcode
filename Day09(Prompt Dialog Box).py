
import maya.cmds as cmds

# Create an OK/Cancel prompt dialog.
#
# +-+---------------------+
# |-|    Rename Object    |
# +-----------------------+
# | Enter Name:           |
# | +-------------------+ |
# | |                   | |
# | |                   | |
# | +-------------------+ |
# +-----------------------+
# | +-------+  +--------+ |
# | |  OK   |  | Cancel | |
# | +-------+  +--------+ |
# +-----------------------+
#

result = cmds.promptDialog(
		title='Rename Object',
		message='Enter Name:',
		button=['OK', 'Cancel'],
		defaultButton='OK',
		cancelButton='Cancel',
		dismissString='Cancel')

if result == 'OK':
	text = cmds.promptDialog(query=True, text=True)
	
print result	



################################################################### SECOND EXAMPLE####################################################################################

import maya.cmds as cmds
result = cmds.promptDialog(
		title='Rename Object',
		message='Enter Name:',
		button=['OK', 'Sid '],
		defaultButton='OK',   #default button is the left one i.e 'ok' 
		cancelButton='Sid ',  #For esc button
		dismissString='Sid again')       #If you press cross button on the side.

if result == 'OK':         #If you press 'OK'............. it will query the text which you had typed in the text box
	text = cmds.promptDialog(query=True, text=True)
	print (text+' is an idiot')   # and then it will print this
	
print result
	
	
