import os
import datetime
from playsound import playsound
from AppKit import NSSound
os. system('clear')

alarmH = int(input("Hours? "))
alarmM = int(input("Minutes? "))
ampm = str(input("AM or PM? "))

os. system('clear')
print("Alarm ringing - ",alarmH,alarmM,ampm)
if (ampm == "PM"):
        alarmH = alarmH + 12
while(1 == 1):
    if(alarmH == datetime.datetime.now().hour and
        alarmM == datetime.datetime.now().minute) :
        print("Wakey-Wakey")
        playsound('C:\Users\hp\Downloads')
        break
