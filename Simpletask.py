import json
import requests

def main():
    portlist = ["32769", "32770","32771","32782"]
    ports_up = []
    ports_down = []
    i = 0
    while(i<4):
       z = portlist[i]+" is up"
       if z in open("/var/lib/awx/venv/pyats/pyatslogs/TaskLog.IOS_job.html").read():
          ports_up.append(portlist[i])
          i = i+1
       else:
          ports_down.append(portlist[i])
          i=i+1
   # print("ports_up :",ports_up)
    print("Unavailable ports from EVE:",ports_down)
if __name__ == '__main__':
    main()
