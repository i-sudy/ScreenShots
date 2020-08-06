#Sudeep Dalela ScreenShots

import pyautogui
from datetime import datetime
import time
dt = datetime.now()
x=1
while x<4:
    pyautogui.screenshot("/Users/isudy/Downloads/ScreenShots/image_"+dt.strftime("%Y-%m-%d %H:%M:%S") +".png")
    x+=1
    time.sleep(2)
