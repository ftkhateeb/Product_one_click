from tkinter import *
import subprocess
import os 


directory = 'C:\Projects\Testinggit\DAS\proj1140_gss_das\embedded_env\make_scripts'
buildCommand = 'bootstrap_make.bat /fic= NautilusMaster.all.ren_f1km /hw_target=REN_HW1_TMPL02 -j8'

root = Tk()
def myClick():

    os.system('cd {} && {}'.format(directory, buildCommand))
    
myButton = Button(root, text = " Build HW1 Master ", command = myClick)
myButton.pack()
root.mainloop()