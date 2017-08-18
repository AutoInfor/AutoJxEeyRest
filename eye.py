import time
import datetime
import os
import platform
import pyautogui
break_time = 8*60

os_str = platform.system()
while (1):
     work_time=40
     i=0
     while (work_time>1):
         x,y=pyautogui.position()
         time.sleep(120)
         x2,y2=pyautogui.position()
         if x2!=x:
             work_time = work_time-2
             i=0
             x=x2
             y=y2
         if x2==x:
             i=i+1
         if i==5:    
             work_time =40
             i=0
         dt=datetime.datetime.now()
         dd=dt.strftime('%I:%M %p')
         
         print('鼠标坐标',str(x2).rjust(4),str(y2).rjust(4),'离休息还有',str(work_time).rjust(3),'分钟','当前时间',dd)
         pyautogui.press('capslock')
         
     os.startfile(r"C:\Windows\System32\Bubbles.scr")
     
     insleep = 1
     start_time = time.time()
     while (insleep):
         end_time = time.time()
         if end_time-start_time > break_time:
             insleep = 0
     #os.system("nircmd.exe monitor on")
     pyautogui.click(1,400)
     
   
