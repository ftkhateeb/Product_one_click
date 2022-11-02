#tkinter is library responsible for creating GUIs in python
# import * means import everything
from tkinter import *

#import OS module in provides functions for accessing,  creating and removing a directory (folder), fetching its contents, changing and identifying the current directory
import os 

root = Tk()
root.title("Poruduct_ONE_CLICK")

# class for our push buttons in order to avoid code reuse when doing mutliple buttons for canoe, HW1, HW1_2, Winidea, APGEN etc
# this class is used to hold the data about the button to be created, like the dimesnions, functionality and button name.. etc
class PushButton:
    Number_of_buttons = 0
    #Constructor 
    def __init__ (self, buttonName, fileDirectory, cmd, height = 10 , length = 40   ):
        #static variable that contains the number of buttons 
        PushButton.Number_of_buttons +=1;
        self.name=buttonName
        self.directory=fileDirectory
        self.command=cmd
        self.Height=height
        self.Length=length 
        #call the function that initialze and create a tkinter GUI button
        self.TkinterButonInit()

    #function that contains the whole command that will be executed when we click the button 
    def myClick(self):
        os.system('cd {} && start "" {}'.format(self.directory, self.command))
    
    #Create new Tkinter button in the gui
    def TkinterButonInit(self):
        new_button = Button(root, text = self.name, command = self.myClick, padx = self.Length, pady = self.Height)
        #put the new button in a new raw depending on the number of buttons
        new_button.grid(row = PushButton.Number_of_buttons)
        #Pack the button to appear in the gui pp



#### How to create a New Button with a different functionality ?
## 1-  
#Push button to build HW1 master
Build_Hw1_master_Button = PushButton(buttonName = "Build HW1 Master", fileDirectory = 'C:\Projects\Testinggit\DAS\proj1140_gss_das\embedded_env\make_scripts', cmd = 'bootstrap_make.bat /fic= NautilusMaster.all.ren_f1km /hw_target=REN_HW1_TMPL02 -j8' )
#Push Button to build HW1 slave
Build_Hw1_Gateway_Button = PushButton(buttonName = "Build HW1 Gateway", fileDirectory = 'C:\Projects\Testinggit\DAS\proj1140_gss_das\embedded_env\make_scripts', cmd = 'bootstrap_make.bat /fic= NautilusGateway.all.ren_f1km /hw_target=REN_HW1_TMPL02 -j8' )
#push Button to open Winidea workspace of HW1
Winidea_Button = PushButton(buttonName = "OpenWinIdea", fileDirectory = 'C:\Projects\Testinggit\DAS\proj1140_gss_das\embedded_env\\tool\\winidea', cmd = 'ZDAS_3_1_IC5500-REN-HW1.xjrf' )
Canoe_Button = PushButton(buttonName = "OpenCanoe", fileDirectory = 'C:\Program Files\\Vector CANoe 12.0__2\\Exec64', cmd = 'CANoe64.exe' )
BuildApgen_Button = PushButton(buttonName = "BuildApgen", fileDirectory = '', cmd = '' )
FlashApgenApp_Button = PushButton(buttonName = "FlashApgenApp", fileDirectory = '', cmd = '' )
root.mainloop()


