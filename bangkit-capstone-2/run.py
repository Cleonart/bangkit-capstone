#! /usr/bin/env python3

import os
import requests

path = "/data/feedback"
dirs = os.listdir(path)
dict = {}

index = 0
for file in dirs:
  with open(path + "/" + str(file)) as f:
   title = f.readline() # get title respectively line number 1
   name  = f.readline() # get name respectively line number 2
   date  = str(f.readline()) # get date respectively line number 3
   feedback = f.readlines()
   dict['title'] = title.split("\n")[0]
   dict['name']  = name.split("\n")[0]
   dict['date']  = date.split("\n")[0]
   dict['feedback'] = feedback[0].split("\n")[0]
   response = requests.post("http://35.238.88.215/feedback/", data=dict);
   if (response.status_code):
     print("Success : " + str(response.status_code))
   f.close()
  index = index + 1
