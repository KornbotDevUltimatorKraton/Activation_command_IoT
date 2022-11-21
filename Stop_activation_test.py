import os 
import json 
import requests 
from itertools import count 
device_name = os.listdir("/home/")[0] # Getting the device name  
Account_data = "kornbot380@hotmail.com"
for i in count(0):
  
            try:
                res_stop_project = requests.get("https://roboreactor.com/device_stop_project_state")  
                device_stop_project = res_stop_project.json().get(Account_data)  # json type data  check 
                if device_stop_project != "None": # Getting data check to avoid none type data 
                       print("Active stop project")
                       print(device_stop_project)
                       if device_stop_project.get("Stop_project") =="ON":
                                            print("Trigger off switch project")
                                            Path_project = device_stop_project.get("Path_project")  
                                            list_local_path = Path_project.split("/")   #Getting the list of the path components 
                                            list_local_path.remove(list_local_path[0]) # remove the first list data 
                                            if len(list_local_path) == 4:
                                                     Project_name = list_local_path[len(list_local_path)-1]
                                                     file = open("Test_stopping_service.txt",'w') # Getting the 
                                                     file.write("Testing_stop_service ",Project_name) # Getting the stopping service status active
                                                     #Running the disable command function to disable service on the linux 
                                                     #os.system("sudo systemctl disable ",str(Project_name))
                                                     #os.system("sudo systemctl stop ",str(Project_name))  
                                                     #os.system("sudo systemctl status ",str(Project_name)) 
                                                     send_stop_project = {Account_data:{"Stop_project":"OFF","Path_project":Path_project}}
                                                     Stop_project_data  = requests.post("https://roboreactor.com/device_stop_project",json=send_stop_project)
                                                     print(Stop_project_data.json())                          
            except:  
                print("Error server connection to stop the project")
