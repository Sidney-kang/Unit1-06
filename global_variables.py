#Created by : Sidney Kang
#Created on : 27 Sept. 2017
#Created for : ICS3UR
# Daily Assignment - Unit1-06
# This program shows the difference between local and global variables

import ui

variableX = 25

def calculation_using_local_variable_touch_up_inside(sender):
    #This shows what happens with a local variable
    
    variableX = 10
    variableY = 20
    variableZ = variableX+variableY
    
    view['local_variable_label'].text = str(variableZ)

def calculation_using_global_variable_touch_up_inside(sneder):
    #This shows what happens with a global variable
    
    #uses global variableX
    variableY = 15
    variableZ = variableX+variableY
    
    view['global_variable_label'].text = str(variableZ)

view = ui.load_view()
view.present('full_screen')
