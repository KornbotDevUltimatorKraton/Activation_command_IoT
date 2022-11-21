import os 
import json 
import requests 
from itertools import count 
device_name = os.listdir("/home/")[0] # Getting the device name data 
Account_data = "kornbot380@hotmail.com" 
for i in count(0):
  
            #Running the request of the 
            try:
                  res_restart_devices = requests.get('https://roboreactor.com/device_restart_status')
                  data_restart_status =  res_restart_devices.json()                
                  device_restart = data_restart_status.get(Account_data) 
                  #print(device_restart)	
                  if device_restart.get('Restart_project') == "ON":
                                    print("Activate the onchange request")  
                                    Path_project = device_restart.get("Path_project") # Getting the path data      
                                    #Getting the Path splitter 
                                    list_path = Path_project.split("/") # Getting the first path remove
                                    list_path.remove(list_path[0])
                                    #checking the length 
                                    Project_name = list_path[len(list_path)-1] # Getting the Project path 
                                    if len(list_path) == 4:
                                            print("Enable project to start....")
                                            #os.system("sudo systemctl enable "+Project_name+".service") # Getting the project_name enable 
                                            #os.system("sudo systemctl restart "+Project_name+".service") # Getting the Project_name restart 
                                            #os.system("sudo systemctl status "+Project_name+".service") # Getting the status of the Project name 
                                            send_activation_restart = {Account_data:{'Restart_project':"OFF","Path_project":Path_project}}  
                                            restart_state_off = requests.post("https://roboreactor.com/device_restart",json=send_activation_restart)
                                            print(restart_state_off.json()) # restart status   
                                    
                                          
            except:
                  print('Error server not found') # checking the data error not found 
