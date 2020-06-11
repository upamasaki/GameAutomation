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

from modules import GameAutomation



def itaku():

    serch_click_image2('./img/itaku_comp_FLAG.png', none_x, none_y, 1, 0.8)
    serch_click_image2('./img/itaku_1h.PNG', none_x, none_y, 1, 0.8)
    serch_click_image2('./img/osusume.PNG', none_x, none_y, 0, 0.9)
    serch_click_image2('./img/itaku_kaishi.PNG', none_x, none_y, 0, 0.9)

    serch_click_image2('./img/itaku_comp_FLAG.png', none_x, none_y, 1, 0.9)
    serch_click_image2('./img/itaku_01.PNG', none_x, none_y, 1, 0.8)
    serch_click_image('./img/osusume.PNG', none_x, none_y, 0)
    serch_click_image('./img/itaku_kaishi.PNG', none_x, none_y, 0)

    serch_click_image2('./img/itaku_comp_FLAG.png', none_x, none_y, 1, 0.9)
    serch_click_image2('./img/itaku_02.PNG', none_x, none_y, 1, 0.8)
    serch_click_image('./img/osusume.PNG', none_x, none_y, 0)
    serch_click_image('./img/itaku_kaishi.PNG', none_x, none_y, 0)


def main():

    #serch_click_image_all2('./img/level3.PNG', none_x, none_y, 0)
    serch_click_image('./img/ge/begi_tiguiro.PNG', 0, 0, 1)
    #serch_click_image('./img/ge/med_tiguiro.PNG', 0, 0, 1)
    #serch_click_image2('./img/ge/top_tiguiro.PNG', 0, 0, 1, 0.95)
    if(serch_click_image('./img/ge/no_mission.PNG', 0, 0, 1)):
        #serch_click_image('./img/ge/back.PNG', 0, 0, 1)    
        serch_click_image2('./img/ge/mission_comp.PNG', 0, 0, 1, 0.8)    
        serch_click_image('./img/ge/close.PNG', 0, 0, 1)
        serch_click_image('./img/ge/mission2.PNG', 0, 0, 1)    
        serch_click_image('./img/ge/mission3.PNG', 0, 0, 1)   
    serch_click_image('./img/ge/mission.PNG', 0, 0, 1)
    serch_click_image('./img/ge/tiguiro.PNG', 0, 0, 1)
    serch_click_image('./img/ge/decide.PNG', 0, 0, 1)
    serch_click_image('./img/ge/go.PNG', 0, 0, 1)
    serch_click_image2('./img/ge/fullfight.PNG', 0, 0, 1, 0.98)
    serch_click_image('./img/ge/go.PNG', 0, 0, 1)
    serch_click_image('./img/ge/close.PNG', 0, 0, 1)
    serch_click_image('./img/ge/battle_end.PNG', 0, 0, 1)
    serch_click_image('./img/ge/ok.PNG', 0, 0, 1)
    serch_click_image('./img/ge/ok2.PNG', 0, 0, 1)
    print("============>  time.sleep")
    time.sleep(2)
    #aaa
    #serch_click_image_all2('./img/level2.PNG', none_x, none_y, 0)
    #serch_click_image('./img/boss.PNG', none_x, none_y, 3)
    #serch_click_image_all2('./img/level1.PNG', none_x, none_y, 0)

def Exercise():
    serch_click_image('./img/kan/go1.PNG', 0, 0, 1)
    serch_click_image('./img/kan/go1.PNG', 0, 0, 1)
    serch_click_image('./img/kan/exercise_icon.PNG', 0, 0, 1)
    
    serch_click_image2('./img/kan/enemy_list1.PNG', 0, 0, 1, 0.9)
    serch_click_image2('./img/kan/enemy_list2.PNG', 0, 0, 1, 0.9)
    serch_click_image2('./img/kan/enemy_list3.PNG', 0, 0, 1, 0.9)

    serch_click_image('./img/kan/exercise_go1.PNG', 0, 0, 1)
    serch_click_image('./img/kan/exercise_go2.PNG', 0, 0, 1)

    serch_click_image('./img/kan/exercise_start1.PNG', 0, 0, 1)
    serch_click_image('./img/kan/exercise_start2.PNG', 0, 0, 1)

    serch_click_image('./img/kan/tanou.PNG', 0, 0, 1)
    serch_click_image('./img/kan/tsuigeki.PNG', 0, 0, 1)
    serch_click_image('./img/kan/next.PNG', 0, 0, 1)
    serch_click_image('./img/kan/next.PNG', 0, 0, 1)
    serch_click_image('./img/kan/next.PNG', 0, 0, 1)
    
    Replenishment()
    
    #aaa
    print("============>  time.sleep")
    time.sleep(2)

def Replenishment():
    serch_click_image('./img/kan/Replenishment.PNG', 0, 0, 1)
    serch_click_image('./img/kan/Replenishment_all.PNG', 0, 0, 1)
    serch_click_image('./img/kan/go_home.PNG', 0, 0, 1)

def sakuya():
    serch_click_image2('./img/work06_v3.PNG', 0, 0, 1, 0.9)
    serch_click_image2('./img/start_v4.PNG', 0, 0, 1, 0.9)
    serch_click_image2('./img/result_v2.PNG', 0, 0, 1, 0.9)
    serch_click_image2('./img/decide_v3.PNG', 0, 0, 1, 0.9)
    time.sleep(2)

def norm():
    
    serch_click_image2('./img/restart.PNG', 0, 0, 1, 0.9)
    # result_v3.PNG
    serch_click_image2('./img/result_v3.PNG', 0, 0, 1, 0.9)
    time.sleep(2)
#以下、メインルーチン
if __name__ == "__main__":
    #実行前の待機(秒)
    time.sleep(1)
    none_x = 1745
    none_y =  658
    count = 0
    base_t = time.time()
    t = 0
    expedi_FLAG = False
    GameAuto = GameAutomation.GameAutomation()
    GameAuto.sample()
    # while 1:
    #     #Exercise()
    #     #story()
    #     #sakuya()
    #     norm()
        


