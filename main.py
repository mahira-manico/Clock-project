import keyboard
import time
from datetime import datetime
from display import *
from function import *

def menu():
 
 current_time=datetime.now()
 set_time_alarm=None
 time_format="24h"
 is_paused=False
 last_update=time.time()

 clear_screen()
 while True:

  try:

   now=time.time()
   if now-last_update >=1:
    current_time=running_hour(current_time, is_paused)
    last_update=now

   time_string=format_time(time_format, current_time)
   display_menu(time_string, time_format, is_paused)
  
   if check_time_alarm(current_time, set_time_alarm)==True:
      set_time_alarm=None
      time.sleep(5)
      clear_screen()
      continue
  
   elif keyboard.is_pressed("a"):
      show_cursor()
      
      H=check_hour()
      M=check_minutes()
      S=check_seconds()
      clear_screen()

      current_time=define_time(current_time, H,M,S)
    
   elif keyboard.is_pressed("b"):
       show_cursor()
     
       H=check_hour()
       M=check_minutes()
       S=check_seconds()
       clear_screen()
       
       set_time_alarm=set_alarm(H,M,S)
       
       print(f"Alarm set at {H:02d}:{M:02d}:{S:02d}")

   elif keyboard.is_pressed("c"):
     current_time=reset_time()
     time.sleep(0.3)
    
   elif keyboard.is_pressed("d"):
     time_format=change_time(time_format)
     time.sleep(0.3)
  
   elif keyboard.is_pressed("e"):
     is_paused=paused(is_paused)
     time.sleep(0.3)
 
   time.sleep(0.01)

  except KeyboardInterrupt:
    clear_screen()
    print("Goodbye!")
    break 
   
  
if __name__=="__main__":
    menu()
    
    
   