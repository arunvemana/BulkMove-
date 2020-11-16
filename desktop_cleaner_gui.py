# importing this for GUI
from easygui import *
# to get the files/directories 
from os import listdir
# to move the files/directories
import os,shutil


Title = "bulk move"
middle_text = "Enter your Details"
# name of the fields
column_names = ["Source Path", "Destination Path","avoid Extensions","avoid folder_name"]
# list of default text/suggestions for the fields
column_sample_text = ["C:\\Users\Desktop","D:\\Copied_folder","ini,lnk","Deskop,Desktop_old"]
# Buliding the gui
Received_data = multenterbox(middle_text,Title, column_names, column_sample_text)


print(listdir("C:\\Users\\avemana\\Desktop"))
files = listdir(Received_data[0])
_Temp = {}
for i in files:
    if i.split('.')[-1] not in Received_data[-2].split(',') and i not in Received_data[-1]:
        try:
            print(i)
            shutil.move(f"{Received_data[0]}\\{i}",f"{Received_data[1]}")
            _Temp[i]="success"
        except Exception as e:
            print("error:",e)
            _Temp[i]="Error"
            continue
        
msgbox('\n'.join(f"{i}: {x}" for i,x in _Temp.items()))
