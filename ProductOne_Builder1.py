## Desicription: Python GUI application responsible for easily managing product one HAL, i.e. easily building, flashing openining workspaces through a simple PushButton click
## Author : AhmedElkhateeb


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
    #static variable that act as a counter which contains the number of buttons created 
    Number_of_buttons = 0
    #Constructor 
    def __init__ (self, buttonName, fileDirectory, cmd, height = 10 , length = 40   ):
        #The cstr __init__ will be called everytime a button object is created, therefore increment the counter 
        PushButton.Number_of_buttons +=1;
        #initialze the object attributes
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
    
    #Create new "Tkinter" button in the gui itself based on our object parameters
    def TkinterButonInit(self):
        new_button = Button(root, text = self.name, command = self.myClick, padx = self.Length, pady = self.Height)
        #put the new button in a new raw depending on the number of buttons
        new_button.grid(row = PushButton.Number_of_buttons)
        #Pack the button to appear in the gui pp



# How to create a New Button with a different functionality ?
## 1- Just instantiate an object from the PushButton class
## 2- pass required parameters in the object creation : 
### a - Button Name
### b - FilePath in which the file/script/program you want to execute is located
### c - The command to be typed in the cmd in the aforementioned path 

 
#create a pushButton object responsible to HW1 master
Build_Hw1_master_Button = PushButton(buttonName = "Build HW1 Master", fileDirectory = 'C:\Projects\Testinggit\DAS\proj1140_gss_das\embedded_env\make_scripts', cmd = 'bootstrap_make.bat /fic= NautilusMaster.all.ren_f1km /hw_target=REN_HW1_TMPL02 -j8' )
#create a pushButton object responsible to build HW1 slave
Build_Hw1_Gateway_Button = PushButton(buttonName = "Build HW1 Gateway", fileDirectory = 'C:\Projects\Testinggit\DAS\proj1140_gss_das\embedded_env\make_scripts', cmd = 'bootstrap_make.bat /fic= NautilusGateway.all.ren_f1km /hw_target=REN_HW1_TMPL02 -j8' )
BuildApgen_Button = PushButton(buttonName = "BuildApgen", fileDirectory = '', cmd = '' )
FlashApgenApp_Button = PushButton(buttonName = "FlashApgenApp", fileDirectory = '', cmd = '' )
Canoe_Button = PushButton(buttonName = "CanoeSim_HW1Proj", fileDirectory = 'C:\Program Files\\Vector CANoe 12.0__2\\Exec64', cmd = 'CANoe64.exe')
Canoe_APGEN_Button = PushButton(buttonName = "CanoeSim_APGEnProj", fileDirectory = '', cmd = '' )
#create a pushButton object responsible to open Winidea workspace of HW1
Winidea_Button = PushButton(buttonName = "WinIdeaWorkspace_HW1", fileDirectory = 'C:\Projects\Testinggit\DAS\proj1140_gss_das\embedded_env\\tool\\winidea', cmd = 'ZDAS_3_1_IC5500-REN-HW1.xjrf' )
#create a pushButton object responsible to open Castle UI
CastleCti_Button = PushButton(buttonName = "CastleUI", fileDirectory = 'C:\\tools\\Castle5_flasher\\Castle5_flasher\\castle\\3_Castle5_User\\3_Projects\\proj1150_c5prjusr_upa_bmw_afas_i200_24CH\\proj1150_c5prjusr_upa_bmw_afas_i200', cmd = 'run_cte_ui.cmd' )

root.mainloop()


