
##PyAutoGUIのモジュール
import pyautogui

##プロセスを制御するためにOS周りのモジュール
import re
import os
import subprocess
import sys
import time
import array

import time

class GameAutomation:
    def __init__(self, none_x = 1745, none_y =  658, move_FLAG = 1):
        self.none_x = none_x
        self.none_y = none_y
        self.move_FLAG = move_FLAG
    ###################################
    # classのサンプルメソッド
    #
    def sample(self):
        print("This object is GameAutomation")

    ###################################
    # 対象の画像を検索しクリック
    #
    def serch_click_image2(self, img_path, wait_time, conf):
        try:
            img_x,img_y = pyautogui.locateCenterOnScreen(img_path, grayscale=True, confidence=conf)
            loc = pyautogui.position()
            print("{:27} is click ({:4}, {:4})".format(img_path, img_x, img_y))
            pyautogui.moveTo(img_x, img_y, duration=0)
            pyautogui.click(img_x,img_y)
            pyautogui.moveTo(loc[0], loc[1], duration=0)
            time.sleep(wait_time)
            return True
        except Exception as e:
            print('{:27} is none [{}]'.format(img_path, e))
            return False
            
    ###################################
    # 対象の画像を検索しその位置まで移動
    #
    def serch_image2(self, img_path, wait_time, conf):
        try:
            img_x,img_y = pyautogui.locateCenterOnScreen(img_path, grayscale=True, confidence=conf)
            print("{:27} is serch ({:4}, {:4})".format(img_path, img_x, img_y))
            time.sleep(wait_time)
            return True
        except:
            print('{:27} is none'.format(img_path))
            return False

    ###################################
    # 対象の画像を検索しその位置でホイール操作
    #
    def serch_wheel_image2(self, img_path, wait_time, conf, v):
        try:
            loc = pyautogui.position()

            img_x, img_y = pyautogui.locateCenterOnScreen(img_path, grayscale=True, confidence=conf)
            pyautogui.moveTo(img_x, img_y, duration=0)
            pyautogui.scroll(v, img_x, img_y)
            print("{:27} is wheel ({:4}, {:4})".format(img_path, img_x, img_y))

            pyautogui.moveTo(loc[0], loc[1], duration=0)
            time.sleep(wait_time)
            return True
        except:
            print('{:27} is none'.format(img_path))
            return False
