import requests
import subprocess 
from subprocess import call
import os
import shutil
import time
import glob


import os
if len(os.listdir('./static')) == 0:
    print("Directory is empty")
    call(['youtube-dl', '-ciw', '-o', '/static/%(title)s.%(ext)s', '-x', '--audio-format', 'mp3', '-a', './URL.txt'], shell=False)
    open('URL.txt', 'w').close()
    time.sleep(10)

    for file in os.listdir("./static"):
      if file.endswith(".mp3"):
        var = os.path.join("./static", file)
        print(var)
       
        okay = var.strip('.\/static\\')
        print(okay)
        f = open("filepath.txt", "w")
        f.write(okay)
        f.close()

    shutil.copy('./templates/default.txt', './templates/test.html')
    time.sleep(1)
    with open('./templates/test.html','r') as f:
        newlines = []
        for line in f.readlines():
          newlines.append(line.replace('mySong.mp3', okay))
    with open('./templates/test.html', 'w') as f:
        for line in newlines:
          f.write(line)


else:    
    print("Directory is not empty")
    files = glob.glob('./static/*.mp3')
for f in files:
    os.remove(f)
call(['youtube-dl', '-ciw', '-o', '/static/%(title)s.%(ext)s', '-x', '--audio-format', 'mp3', '-a', './URL.txt'], shell=False)
open('URL.txt', 'w').close()
time.sleep(10)

for file in os.listdir("./static"):
  if file.endswith(".mp3"):
    var = os.path.join("./static", file)
    print(var)
       
    okay = var.strip('.\/static\\')
    print(okay)
    f = open("filepath.txt", "w")
    f.write(okay)
    f.close()

    shutil.copy('./templates/default.txt', './templates/test.html')
    time.sleep(1)
  with open('./templates/test.html','r') as f:
    newlines = []
    for line in f.readlines():
        newlines.append(line.replace('mySong.mp3', okay))
  with open('./templates/test.html', 'w') as f:
    for line in newlines:
        f.write(line)


    



