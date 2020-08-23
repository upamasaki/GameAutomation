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
import argparse

# def sakuya():
#     serch_click_image2('./img/work06_v3.png', 0, 0, 1, 0.9)
#     serch_click_image2('./img/start_v4.png', 0, 0, 1, 0.9)
#     serch_click_image2('./img/result_v2.png', 0, 0, 1, 0.9)
#     serch_click_image2('./img/decide_v3.png', 0, 0, 1, 0.9)
#     time.sleep(2)


def norm(GameAuto):
    
    GameAuto.serch_click_image2('./img/restart.png', 1, 0.9)
    # result_v3.png
    GameAuto.serch_click_image2('./img/result_v3.png', 1, 0.9)
    time.sleep(2)


def init(GameAuto):

    # GameAuto.serch_click_image2('./img/kyoshintoseijyo/omoi.png', 1, 0.9)
    if(GameAuto.serch_click_image2('./img/kyoshintoseijyo/ok2.png', 1, 0.9)):
        GameAuto.serch_click_image2('./img/kyoshintoseijyo/reflesh.png', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/ok3.png', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/ok4.png', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/screen.png', 1, 0.9)


def kyoshintoseijyo_norm(GameAuto):

    

    GameAuto.serch_click_image2('./img/kyoshintoseijyo/login.png', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/girl.png', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/click.png', 1, 0.8)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/close.png', 1, 0.9)
    # GameAuto.serch_click_image2('./img/kyoshintoseijyo/click.png', 1, 0.8)


    # GameAuto.serch_click_image2('./img/kyoshintoseijyo/ponyo.png', 1, 0.9)
    # GameAuto.serch_click_image2('./img/kyoshintoseijyo/ponyo.png', 1, 0.9)
    # GameAuto.serch_click_image2('./img/kyoshintoseijyo/ponyo.png', 1, 0.9)

    GameAuto.serch_click_image2('./img/kyoshintoseijyo/seika.png', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/kyosin.png', 1, 0.9)
    
    #############################################
    # order関係
    time.sleep(2)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/order_v2.png', 3, 0.95)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/yes.png', 1, 0.9)
    if(not GameAuto.serch_click_image2('./img/kyoshintoseijyo/item_get.png', 3, 0.8)):
        GameAuto.serch_click_image2('./img/kyoshintoseijyo/yes.png', 1, 0.9)
        GameAuto.serch_click_image2('./img/kyoshintoseijyo/ok5.png', 1, 0.8)
    else:
        GameAuto.serch_click_image2('./img/kyoshintoseijyo/close2.png', 1, 0.8)

    GameAuto.serch_click_image2('./img/kyoshintoseijyo/yes.png', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/yes2.png', 1, 0.8)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/ok5.png', 1, 0.8)

    if(not GameAuto.serch_click_image2('./img/kyoshintoseijyo/order_flag.png', 1, 0.8)):
        GameAuto.serch_click_image2('./img/kyoshintoseijyo/close2.png', 1, 0.8)
    
    if(not GameAuto.serch_click_image2('./img/kyoshintoseijyo/item_get.png', 3, 0.8)):
        GameAuto.serch_click_image2('./img/kyoshintoseijyo/yes.png', 1, 0.9)
        GameAuto.serch_click_image2('./img/kyoshintoseijyo/ok5.png', 1, 0.8)
    else:
        GameAuto.serch_click_image2('./img/kyoshintoseijyo/close2.png', 1, 0.8)

    GameAuto.serch_click_image2('./img/kyoshintoseijyo/yes.png', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/ok5.png', 1, 0.8)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/ok5.png', 1, 0.8)
    
    # GameAuto.serch_click_image2('./img/kyoshintoseijyo/scroll.png', 1, 0.75)
    # pyautogui.vscroll(-5)
    # GameAuto.serch_click_image2('./img/kyoshintoseijyo/scroll.png', 1, 0.75)
    if(GameAuto.serch_click_image2('./img/kyoshintoseijyo/seika_kyojin_label.png', 1, 0.9)):
        GameAuto.serch_click_image2('./img/kyoshintoseijyo/last_stage2.png', 1, 0.8)
        GameAuto.serch_click_image2('./img/kyoshintoseijyo/last_stage2.png', 1, 0.8)

    GameAuto.serch_click_image2('./img/kyoshintoseijyo/battle4.png', 1, 0.9)

    # GameAuto.serch_click_image2('./img/kyoshintoseijyo/retry.png', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/come_back.png', 1, 0.9)
    # result_v3.png


    GameAuto.serch_click_image2('./img/kyoshintoseijyo/battle.png', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/battle.png', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/battle.png', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/battle.png', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/battle.png', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/battle.png', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/battle.png', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/battle3.png', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/battle3.png', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/ok.png', 1, 0.9)

    GameAuto.serch_click_image2('./img/kyoshintoseijyo/omoi.png', 1, 0.9)


    GameAuto.serch_click_image2('./img/kyoshintoseijyo/word_space.png', 1, 0.9)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo/word_space2.png', 1, 0.9)
    time.sleep(2)



def kyoshintoseijyo_norm_linux(GameAuto):
    # GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/last_stage2.png', 1, 0.75)

    if(GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/network.png', 1, 0.8)):
        GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/retry.png', 1, 0.8)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/login.png', 1, 0.8)

    GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/close2.png', 1, 0.8)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/home.png', 3, 0.8)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/seika.png', 1, 0.8)

    if(GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/ok3.png', 1, 0.8)):
        GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/reflesh.png', 1, 0.8)
    
    GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/page_move.png', 1, 0.8)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/uid.png', 1, 0.8)

    GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/seika.png', 1, 0.8)

    GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/order_flag.png', 1, 0.8)

    GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/main_order_flag.png', 1, 0.8)
    if(GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/item_get.png', 2, 0.8)):
        GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/yes.png', 1, 0.8)
        GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/ok2.png', 1, 0.8)
    else:
        if(GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/close.png', 1, 0.8)):
            time.sleep(3)

    GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/last_stage2.png', 1, 0.75)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/last_stage.png', 1, 0.8)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/last_stage.png', 1, 0.8)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/battle_btn.png', 1, 0.8)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/come_back.png', 1, 0.8)
    GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/ok.png', 1, 0.8)
   
    time.sleep(2)

def kyoshintoseijyo_battle(GameAuto):
    print("kyoshintoseijyo_battle >>>>>>>")
    if(GameAuto.serch_click_image2('./img/kyoshintoseijyo/takusu.png', 1, 0.9)):
        time.sleep(20)


def kyoshintoseijyo_battle_linux(GameAuto):
    print("kyoshintoseijyo_battle >>>>>>>")
    if(GameAuto.serch_image2('./img/kyoshintoseijyo_note/inori_lv1.png', 0, 0.95)):
        GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/inori.png', 1, 0.8)

    if(GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/omega.png', 1, 0.8)):
        for _ in range(10):
            GameAuto.serch_click_image2('./img/kyoshintoseijyo_note/omega.png', 0, 0.8)

def tourabu(GameAuto):
    
    if(GameAuto.serch_image2('./img/tourabu/honmaru.png', 1, 0.95)):
        GameAuto.serch_click_image2('./img/tourabu/mokuroku.png', 1, 0.8)
        GameAuto.serch_click_image2('./img/tourabu/mokuroku2.png', 1, 0.8)
    
        GameAuto.serch_click_image2('./img/tourabu/go.png', 1, 0.8)
        GameAuto.serch_click_image2('./img/tourabu/go2.png', 1, 0.8)

    if(GameAuto.serch_image2('./img/tourabu/battle_mode.png', 1, 0.90)):
        GameAuto.serch_click_image2('./img/tourabu/battle.png', 1, 0.8)
        GameAuto.serch_click_image2('./img/tourabu/choice.png', 1, 0.8)

        if(GameAuto.serch_image2('./img/tourabu/hirou.png', 1, 0.90)):
            GameAuto.serch_click_image2('./img/tourabu/back2.png', 1, 0.8)
            GameAuto.serch_click_image2('./img/tourabu/mokuroku.png', 1, 0.8)
            GameAuto.serch_click_image2('./img/tourabu/mokuroku2.png', 1, 0.8)
            GameAuto.serch_click_image2('./img/tourabu/honmaru3.png', 1, 0.8)

            for _ in tqdm(range(60*10)):
                time.sleep(1)
        else:
            GameAuto.serch_click_image2('./img/tourabu/battle2.png', 1, 0.8)
            GameAuto.serch_click_image2('./img/tourabu/battle3.png', 1, 0.8)



    GameAuto.serch_click_image2('./img/tourabu/yuri.png', 1, 0.8)
    GameAuto.serch_click_image2('./img/tourabu/outai.png', 1, 0.8)
    GameAuto.serch_click_image2('./img/tourabu/result.png', 1, 0.8)
    GameAuto.serch_click_image2('./img/tourabu/result.png', 1, 0.8)
    GameAuto.serch_click_image2('./img/tourabu/result.png', 1, 0.8)
    GameAuto.serch_click_image2('./img/tourabu/back.png', 1, 0.8)

    GameAuto.serch_click_image2('./img/tourabu/get_kanana.png', 1, 0.8)
    GameAuto.serch_click_image2('./img/tourabu/get_kanana.png', 1, 0.8)

    if(GameAuto.serch_click_image2('./img/tourabu/yes.png', 1, 0.8)):  
        for _ in tqdm(range(60*10)):
            time.sleep(1)
    
    time.sleep(3)

def kyoshintoseijyo_main(GameAuto):
    init(GameAuto)
    if(GameAuto.serch_click_image2('./img/kyoshintoseijyo/battle_gage.PNG', 1, 0.8)):
        kyoshintoseijyo_battle(GameAuto)
    else:
        kyoshintoseijyo_norm(GameAuto)
def tourabu_main(GameAuto):
    while 1:
        GameAuto.serch_click_image2('./img/tourabu/apply.PNG', 1, 0.8)

        GameAuto.serch_click_image2('./img/tourabu/yuri.PNG', 1, 0.8)
        GameAuto.serch_click_image2('./img/tourabu/outai.PNG', 1, 0.8)

        GameAuto.serch_click_image2('./img/tourabu/challenge_exercise.PNG', 1, 0.8)
        GameAuto.serch_click_image2('./img/tourabu/exercise_btn.PNG', 1, 0.8)
        GameAuto.serch_click_image2('./img/tourabu/exercise_btn2.PNG', 1, 0.8)
        
        GameAuto.serch_click_image2('./img/tourabu/result.PNG', 1, 0.8)
        GameAuto.serch_click_image2('./img/tourabu/result.PNG', 1, 0.8)
        GameAuto.serch_click_image2('./img/tourabu/result.PNG', 1, 0.8)

        time.sleep(3)

def get_mouse():

    pos =  pyautogui.position()
    print(pos)

def tiktan_battle(GameAuto):
    pyautogui.keyDown('end')
    pyautogui.keyUp('end')
    time.sleep(1)
    GameAuto.serch_click_image2('./img/tiktan/come_back.PNG', 1, 0.8)
    time.sleep(3)

def tiktan_main(GameAuto):

    while 1:
        print(">>>>>>>>> tiktan >>>>>>")
        GameAuto.serch_wheel_image2('./img/tiktan/now_state.PNG', 1, 0.8, -800)


        if(GameAuto.serch_click_image2('./img/tiktan/statusp.PNG', 1, 0.95)):
            GameAuto.serch_click_image2('./img/tiktan/status1.PNG', 1, 0.8)
            GameAuto.serch_click_image2('./img/tiktan/statusp_STR2.PNG', 1, 0.8)
            pyautogui.keyDown('end')
            pyautogui.keyUp('end')
            GameAuto.serch_click_image2('./img/tiktan/ok.PNG', 1, 0.8)


        if(GameAuto.serch_click_image2('./img/tiktan/battle.PNG', 1, 0.8)):
            tiktan_battle(GameAuto)
            GameAuto.serch_click_image2('./img/tiktan/come_back.PNG', 1, 0.8)

        if(GameAuto.serch_click_image2('./img/tiktan/chanp.PNG', 1, 0.8)):
            GameAuto.serch_click_image2('./img/tiktan/chanp2.PNG', 1, 0.8)
            tiktan_battle(GameAuto)
        time.sleep(1)


def tiktan_main_linux(GameAuto):

    while 1:
        print(">>>>>>>>> tiktan >>>>>>")
        GameAuto.serch_wheel_image2('./img/tiktan/now_state.PNG', 1, 0.5, -800)


        if(GameAuto.serch_click_image2('./img/tiktan/statusp.PNG', 1, 0.5)):
            GameAuto.serch_click_image2('./img/tiktan/status1.PNG', 1, 0.5)
            GameAuto.serch_click_image2('./img/tiktan/statusp_STR2.PNG', 1, 0.5)
            pyautogui.keyDown('end')
            pyautogui.keyUp('end')
            GameAuto.serch_click_image2('./img/tiktan/ok.PNG', 1, 0.5)


        if(GameAuto.serch_click_image2('./img/tiktan/battle.PNG', 1, 0.5)):
            tiktan_battle(GameAuto)
            GameAuto.serch_click_image2('./img/tiktan/come_back.PNG', 1, 0.5)

        if(GameAuto.serch_click_image2('./img/tiktan/chanp.PNG', 1, 0.5)):
            GameAuto.serch_click_image2('./img/tiktan/chanp2.PNG', 1, 0.5)
            tiktan_battle(GameAuto)
        time.sleep(1)


#以下、メインルーチン
if __name__ == "__main__":
    
    # 
    #
    #
    #
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--gname', default='tourabu', help='game name')    # 実数値(float)
    parser.add_argument('--os', default='win', help='os info') 

    args = parser.parse_args()
    print(args)

    GameAuto = GameAutomation.GameAutomation()
    GameAuto.sample()
    
    #Exercise()
    #story()
    #sakuya()
    # norm(GameAuto)
    print("=========================")
    print(args.gname)
    print(args.gname == 'tiktan')
    if(args.gname == 'tiktan'):
        if(0):
            tiktan_main(GameAuto)
        else:
            tiktan_main_linux(GameAuto)
    
    if(args.gname == 'tourabu'):
        tourabu_main(GameAuto)

    print("=========================")
        # get_mouse()
        # tourabu(GameAuto)
        


