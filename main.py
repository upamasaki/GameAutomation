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

# def sakuya():
#     serch_click_image2('./img/work06_v3.PNG', 0, 0, 1, 0.9)
#     serch_click_image2('./img/start_v4.PNG', 0, 0, 1, 0.9)
#     serch_click_image2('./img/result_v2.PNG', 0, 0, 1, 0.9)
#     serch_click_image2('./img/decide_v3.PNG', 0, 0, 1, 0.9)
#     time.sleep(2)


def norm(GameAuto):
    
    GameAuto.serch_click_image2('./img/restart.PNG', 1, 0.9)
    # result_v3.PNG
    GameAuto.serch_click_image2('./img/result_v3.PNG', 1, 0.9)
    time.sleep(2)


def init(GameAuto):

    # GameAuto.serch_click_image2('./img/kyoshintoseijyo/omoi.PNG', 1, 0.9)
    if(GameAuto.serch_click_image2('./img/kyoshintoseijyo/ok2.PNG', 1, 0.9)):
        GameAuto.serch_click_image2('./img/kyoshintoseijyo/reflesh.PNG', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/ok3.PNG', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/ok4.PNG', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/screen.PNG', 1, 0.9)


def kyoshintoseijyo_norm(GameAuto):

    

    GameAuto.serch_click_image2('./img/kyoshintoseijyo/login.PNG', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/girl.PNG', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/click.PNG', 1, 0.8)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/close.PNG', 1, 0.9)
    # GameAuto.serch_click_image2('./img/kyoshintoseijyo/click.PNG', 1, 0.8)


    # GameAuto.serch_click_image2('./img/kyoshintoseijyo/ponyo.PNG', 1, 0.9)
    # GameAuto.serch_click_image2('./img/kyoshintoseijyo/ponyo.PNG', 1, 0.9)
    # GameAuto.serch_click_image2('./img/kyoshintoseijyo/ponyo.PNG', 1, 0.9)

    GameAuto.serch_click_image2('./img/kyoshintoseijyo/seika.PNG', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/kyosin.PNG', 1, 0.9)
    
    #############################################
    # order関係
    time.sleep(2)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/order_v2.PNG', 3, 0.95)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/yes.PNG', 1, 0.9)
    if(not GameAuto.serch_click_image2('./img/kyoshintoseijyo/item_get.PNG', 3, 0.8)):
        GameAuto.serch_click_image2('./img/kyoshintoseijyo/yes.PNG', 1, 0.9)
        GameAuto.serch_click_image2('./img/kyoshintoseijyo/ok5.PNG', 1, 0.8)
    else:
        GameAuto.serch_click_image2('./img/kyoshintoseijyo/close2.PNG', 1, 0.8)

    GameAuto.serch_click_image2('./img/kyoshintoseijyo/yes.PNG', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/yes2.PNG', 1, 0.8)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/ok5.PNG', 1, 0.8)

    if(not GameAuto.serch_click_image2('./img/kyoshintoseijyo/order_flag.PNG', 1, 0.8)):
        GameAuto.serch_click_image2('./img/kyoshintoseijyo/close2.PNG', 1, 0.8)
    
    if(not GameAuto.serch_click_image2('./img/kyoshintoseijyo/item_get.PNG', 3, 0.8)):
        GameAuto.serch_click_image2('./img/kyoshintoseijyo/yes.PNG', 1, 0.9)
        GameAuto.serch_click_image2('./img/kyoshintoseijyo/ok5.PNG', 1, 0.8)
    else:
        GameAuto.serch_click_image2('./img/kyoshintoseijyo/close2.PNG', 1, 0.8)

    GameAuto.serch_click_image2('./img/kyoshintoseijyo/yes.PNG', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/ok5.PNG', 1, 0.8)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/ok5.PNG', 1, 0.8)
    
    # GameAuto.serch_click_image2('./img/kyoshintoseijyo/scroll.PNG', 1, 0.75)
    # pyautogui.vscroll(-5)
    # GameAuto.serch_click_image2('./img/kyoshintoseijyo/scroll.PNG', 1, 0.75)
    if(GameAuto.serch_click_image2('./img/kyoshintoseijyo/seika_kyojin_label.PNG', 1, 0.9)):
        GameAuto.serch_click_image2('./img/kyoshintoseijyo/last_stage2.PNG', 1, 0.8)
        GameAuto.serch_click_image2('./img/kyoshintoseijyo/last_stage2.PNG', 1, 0.8)

    GameAuto.serch_click_image2('./img/kyoshintoseijyo/battle4.PNG', 1, 0.9)

    # GameAuto.serch_click_image2('./img/kyoshintoseijyo/retry.PNG', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/come_back.PNG', 1, 0.9)
    # result_v3.PNG


    GameAuto.serch_click_image2('./img/kyoshintoseijyo/battle.PNG', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/battle.PNG', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/battle.PNG', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/battle.PNG', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/battle.PNG', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/battle.PNG', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/battle.PNG', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/battle3.PNG', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/battle3.PNG', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/ok.PNG', 1, 0.9)

    GameAuto.serch_click_image2('./img/kyoshintoseijyo/omoi.PNG', 1, 0.9)


    GameAuto.serch_click_image2('./img/kyoshintoseijyo/word_space.PNG', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/word_space2.PNG', 1, 0.9)
    time.sleep(2)


def kyoshintoseijyo_battle(GameAuto):
    print("kyoshintoseijyo_battle >>>>>>>")
    if(GameAuto.serch_click_image2('./img/kyoshintoseijyo/takusu.PNG', 1, 0.9)):
        time.sleep(20)


def tourabu(GameAuto):
    
    if(GameAuto.serch_image2('./img/tourabu/honmaru.PNG', 1, 0.95)):
        GameAuto.serch_click_image2('./img/tourabu/mokuroku.PNG', 1, 0.8)
        GameAuto.serch_click_image2('./img/tourabu/mokuroku2.PNG', 1, 0.8)
    
        GameAuto.serch_click_image2('./img/tourabu/go.PNG', 1, 0.8)
        GameAuto.serch_click_image2('./img/tourabu/go2.PNG', 1, 0.8)

    if(GameAuto.serch_image2('./img/tourabu/battle_mode.PNG', 1, 0.90)):
        GameAuto.serch_click_image2('./img/tourabu/battle.PNG', 1, 0.8)
        GameAuto.serch_click_image2('./img/tourabu/choice.PNG', 1, 0.8)

        if(GameAuto.serch_image2('./img/tourabu/hirou.PNG', 1, 0.90)):
            GameAuto.serch_click_image2('./img/tourabu/back2.PNG', 1, 0.8)
            GameAuto.serch_click_image2('./img/tourabu/mokuroku.PNG', 1, 0.8)
            GameAuto.serch_click_image2('./img/tourabu/mokuroku2.PNG', 1, 0.8)
            GameAuto.serch_click_image2('./img/tourabu/honmaru3.PNG', 1, 0.8)

            for _ in tqdm(range(60*10)):
                time.sleep(1)
        else:
            GameAuto.serch_click_image2('./img/tourabu/battle2.PNG', 1, 0.8)
            GameAuto.serch_click_image2('./img/tourabu/battle3.PNG', 1, 0.8)



    GameAuto.serch_click_image2('./img/tourabu/yuri.PNG', 1, 0.8)
    GameAuto.serch_click_image2('./img/tourabu/outai.PNG', 1, 0.8)
    GameAuto.serch_click_image2('./img/tourabu/result.PNG', 1, 0.8)
    GameAuto.serch_click_image2('./img/tourabu/result.PNG', 1, 0.8)
    GameAuto.serch_click_image2('./img/tourabu/result.PNG', 1, 0.8)
    GameAuto.serch_click_image2('./img/tourabu/back.PNG', 1, 0.8)

    GameAuto.serch_click_image2('./img/tourabu/get_kanana.PNG', 1, 0.8)
    GameAuto.serch_click_image2('./img/tourabu/get_kanana.PNG', 1, 0.8)

    if(GameAuto.serch_click_image2('./img/tourabu/yes.PNG', 1, 0.8)):  
        for _ in tqdm(range(60*10)):
            time.sleep(1)
    
    time.sleep(3)



#以下、メインルーチン
if __name__ == "__main__":
    
    # 
    #
    #
    #
    GameAuto = GameAutomation.GameAutomation()
    GameAuto.sample()
    while 1:
        #Exercise()
        #story()
        #sakuya()
        # norm(GameAuto)
        init(GameAuto)
        if(GameAuto.serch_click_image2('./img/kyoshintoseijyo/battle_gage.PNG', 1, 0.8)):
            kyoshintoseijyo_battle(GameAuto)
        else:
            kyoshintoseijyo_norm(GameAuto)
        # tourabu(GameAuto)
        


