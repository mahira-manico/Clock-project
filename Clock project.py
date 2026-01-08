from datetime import datetime
from datetime import timedelta
import time
import keyboard
import threading

current_time=datetime.now()
set_time_alarm=None

def running_hour():
 global current_time

 while True:
  
  current_time+=timedelta(seconds=1)
  time.sleep(1)
  
thread_for_clock=threading.Thread(target=running_hour)
thread_for_clock.start()
 
def define_time(hours, minutes, seconds):
 
 global current_time
 
 current_time=current_time.replace(hour=hours, minute=minutes, second=seconds)
 menu()
  

def set_alarm(h, m, s):
    global current_time
    global set_time_alarm

    print("\033[H\033[J", end="")
    
    set_time_alarm=current_time.replace(hour=h, minute=m, second=s)
    formatted_time_alarm=set_time_alarm.time().strftime("%H:%M:%S")
   
    print(f"alarm set at: {formatted_time_alarm}")
    menu()

def reset_time():
  global current_time
  current_time=datetime.now()   

def menu():
  global current_time
  global set_time_alarm

  
  while True:
    print("\033[?25l", end="")
    current_time_formatted=current_time.strftime("%H:%M:%S")

    print("\033[2;0H")
    print("Clock menu")
    print("\033[3;0H")
    print(current_time_formatted)
    print("\033[4;0H")
    print("1. Change time/tap a")
    print("\033[5;0H")
    print("2. Set an alarm/tap b")
    print("\033[6;0H")
    print("3. Reset time/tap c")
    time.sleep(0.01)
    print("\033[J", end="")

    if current_time==set_time_alarm:
      print("\033[H\033[J", end="")
      print("your alarm is ringing!")
      print("\033[H\033[J", end="")
      set_time_alarm= None  
      time.sleep(5)
      continue
    
  
    elif keyboard.is_pressed("a"):
      print("\033[?25h", end="")
      
      try:
       H=int(input("choose an hour: "))
       if H not in range(0,24):
        print("Invalid number! Choose 0-23 for hours!")
        time.sleep(2)
        continue 
       
       M=int(input("choose minutes: "))
       if M not in range(0,60):
        print("Invalid number! Choose 0-23 for minutes!") 
        time.sleep(2)
        continue
    
       S=int(input("choose seconds: "))
       if S not in range(0,60):
         print("Invalid number! Choose 0-23 for seconds!") 
         time.sleep(2)
         continue
       
       define_time(H,M,S)

      except ValueError:
        print("Enter numbers only!")
        time.sleep(2)
        continue
    
 
    elif keyboard.is_pressed("b"):
     print("\033[?25h", end="")

     try:
       
       hour_alarm=int(input("choose an hour: "))
       if hour_alarm not in range(0,24):
         print("Invalid entry! Choose 0-23 only!")
         time.sleep(2)
         continue
       
       minutes_alarm=int(input("choose minutes: "))
       if minutes_alarm not in range(0,60):
         print("Invalid entry! Choose 0-59 only!")
         time.sleep(2)
         continue
       
       seconds_alarm=int(input("choose seconds: "))
       if seconds_alarm not in range(0,60):
         print("Invalid entry! Choose 0-59 only!")
         time.sleep(2)
         continue

       set_alarm(hour_alarm, minutes_alarm, seconds_alarm)

     except ValueError:
      print("Enter numbers only!")
      time.sleep(2)
      continue
     
    elif keyboard.is_pressed("c"):
     reset_time()
       
   
menu()


  
  


