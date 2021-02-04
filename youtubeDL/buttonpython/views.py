from django.shortcuts import render
import requests
import sys
import time
from subprocess import run, PIPE

def button(request):
  return render(request,'home.html')


def external(request):
   inp= request.POST.get('param')
   if "youtu" not in inp: 
    return render(request,'error.html')
   else:
    f = open("URL.txt", "w")
    f.write(inp)
    f.close()
    out= run([sys.executable,'./main.py',inp],shell=False)
    print(out)
    return render(request,'test.html')
