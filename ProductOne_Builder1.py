#tkinter is library responsible for creating GUIs in python
# import * means import everything
from tkinter import *

#import OS module in provides functions for accessing,  creating and removing a directory (folder), fetching its contents, changing and identifying the current directory
import os 

root = Tk()

# class for our push buttons in order to avoid code reuse when doing mutliple buttons for canoe, HW1, HW1_2, Winidea, APGEN etc
class PushButton:
    #Constructor 
    def __init__ (self, buttonName, fileDirectory, cmd, height = 20 , length = 50):
        self.name=buttonName
        self.directory=fileDirectory
        self.command=cmd
        self.Height=height
        self.Length=length
        self.TkinterButon_init()

    #function that contains the whole command that will be executed when we click the button 
    def myClick(self):
        os.system('cd {} && {}'.format(self.directory, self.command))
    
    # initialize new Tkinter button inside our PushButton class
    def TkinterButon_init:
        new_button = Button(root, text = self.name, command = self.myClick, padx = self.Length, pady = self.Height)
        new_button.pack()
        root.mainloop()




Build_Hw1_master_Button = PushButton(buttonName = "Build HW1 Master", fileDirectory = 'C:\Projects\Testinggit\DAS\proj1140_gss_das\embedded_env\make_scripts', cmd = 'bootstrap_make.bat /fic= NautilusMaster.all.ren_f1km /hw_target=REN_HW1_TMPL02 -j8' )



