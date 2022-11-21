import os 
import json 
import configparser 
import requests 
from itertools import count 
user = os.listdir("/home/")[0] # getting the user data
email = "kornbot380@hotmail.com" 
for i in count(0):
       try:
              res_gen = requests.get("https://roboreactor.com/generation_statement") 
              devices_gen = res_gen.json().get(email)
              if str(devices_gen) == "None":
                        print("Data is not json type please check server")
              if str(devices_gen) !="None":
                     #Generate the running path file here to run the library 
                     if devices_gen.get('Generator') == "ON":
                                   print("Generate_path",devices_gen.get('Path_project'))
                                   #Getting the new path generate into the system 
                                   Path_data = devices_gen.get('Path_project').split("/")
                                   Path_data.remove(Path_data[0]) # remove the first data inside the list 
                                   Length_path = len(Path_data)
                                   if Length_path == 4: 
                                        for r in range(0,5):
                                              Project_name = Path_data[Length_path-1]
                                              print("Project_name",Project_name)                                               
                                              # Now starting to generate the systemd file to running the service
                                              print("Generate the service file")
                                              Generate_path = "/usr/lib/systemd/system/" 
                                              project_name = 'Project:'+Project_name   
                                              mode = 'multi-user.target' 
                                              Python_exc_path = "/usr/bin/python3 "
                                              Working_path = "/home/"+user+"/Roboreactor_projects/"+Project_name
                                              Execute_path = "/home/"+user+"/Roboreactor_projects/"+Project_name+"/"+Project_name+".py"   
                                              config = configparser.ConfigParser() 
                                              config.optionxform = str
                                              settings = ['Unit','Service','Install']
                                              #Unit
                                              config.add_section(settings[0]) # Getting the section added into the list topic 
                                              config.set(settings[0],'Description',str(project_name)) 
                                              config.set(settings[0],'After',str(mode))
                                              #Service 
                                              config.add_section(settings[1])
                                              config.set(settings[1],'Type','idle')
                                              config.set(settings[1],'WorkingDirectory',Working_path)
                                              config.set(settings[1],'User',str(user))
                                              config.set(settings[1],'ExecStart',str(Python_exc_path+Execute_path))
                                              config.set(settings[1],'WantedBy','always')
                                              #Install 
                                              config.add_section(settings[2])
                                              config.set(settings[2],'WantedBy',str(mode))
                                              configfile = open(Generate_path+"/"+Project_name+".service",'w')
                                              config.write(configfile)
                                              os.system("sudo chmod -R 777 "+Generate_path+"/"+Project_name+".service")                                                                                                   
                                              #Now turn off the activation 
                                              send_off_gen_com = {email:{"Generator":"OFF","Path_project":devices_gen.get('Path_project')}}
                                              res_off_gen = requests.post("https://roboreactor.com/Generator_onchange",json=send_off_gen_com)
                                              print(res_off_gen.json())                  
       except: 
           print("Error server connection") 
