# -*- coding: utf-8 -*-
##PyAutoGUIのモジュール
import pyautogui

##プロセスを制御するためにOS周りのモジュール
import re
import os
import subprocess
import sys
import time
import array

###Win32のUI情報と制御用モジュール
#import win32api
#import win32gui
#import win32con

import time
from tqdm import tqdm

none_x = 1745
none_y =  658
move_FLAG = 1

#from modules import GameAutomation

import sys
import pprint

pprint.pprint(sys.path)
sys.path.append("./modules")

import GameAutomation 

def sakuya():
    serch_click_image2('./img/work06_v3.PNG', 0, 0, 1, 0.9)
    serch_click_image2('./img/start_v4.PNG', 0, 0, 1, 0.9)
    serch_click_image2('./img/result_v2.PNG', 0, 0, 1, 0.9)
    serch_click_image2('./img/decide_v3.PNG', 0, 0, 1, 0.9)
    time.sleep(2)

def norm(GameAuto):
    
    GameAuto.serch_click_image2('./img/restart.PNG', 1, 0.9)
    # result_v3.PNG
    GameAuto.serch_click_image2('./img/result_v3.PNG', 1, 0.9)
    time.sleep(2)

#以下、メインルーチン
if __name__ == "__main__":
    
    # 
    GameAuto = GameAutomation.GameAutomation()
    GameAuto.sample()
    while 1:
        #Exercise()
        #story()
        #sakuya()
        norm(GameAuto)
        


