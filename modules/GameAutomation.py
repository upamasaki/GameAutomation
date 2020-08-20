
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

class GameAutomation:
    def __init__(self, none_x = 1745, none_y =  658, move_FLAG = 1):
        self.none_x = none_x
        self.none_y = none_y
        self.move_FLAG = move_FLAG

    def sample(self):
        print("This object is GameAutomation")

    def serch_click_image(self, img_path, offset_x, offset_y, wait_time):
        try:
            img_x,img_y = pyautogui.locateCenterOnScreen(img_path, grayscale=True, confidence=0.8)
            img_x = img_x + offset_x
            img_y = img_y + offset_y

            loc = pyautogui.position()
            print("{:27} is click ({:4}, {:4})".format(img_path, img_x, img_y))
            pyautogui.moveTo(img_x, img_y, duration=0)
            #pos         = pyautogui.locateCenterOnScreen('search.png')
            pyautogui.click(img_x,img_y)
            pyautogui.moveTo(loc[0], loc[1], duration=0)
            time.sleep(wait_time)
            return True
        except:
            print('{:27} is none'.format(img_path))
            #pyautogui.click(none_x,none_y)
            return False

    def serch_click_image2(self, img_path, wait_time, conf):
        try:
            img_x,img_y = pyautogui.locateCenterOnScreen(img_path, grayscale=True, confidence=conf)
            #print(img_x)
            loc = pyautogui.position()
            print("{:27} is click ({:4}, {:4})".format(img_path, img_x, img_y))
            pyautogui.moveTo(img_x, img_y, duration=0)
            #pos         = pyautogui.locateCenterOnScreen('search.png')
            pyautogui.click(img_x,img_y)
            pyautogui.moveTo(loc[0], loc[1], duration=0)
            time.sleep(wait_time)
            return True
        except:
            print('{:27} is none'.format(img_path))
            #pyautogui.click(none_x,none_y)
            return False

    def serch_image2(self, img_path, wait_time, conf):
        try:
            img_x,img_y = pyautogui.locateCenterOnScreen(img_path, grayscale=True, confidence=conf)
            print("{:27} is click ({:4}, {:4})".format(img_path, img_x, img_y))
            time.sleep(wait_time)
            return True
        except:
            print('{:27} is none'.format(img_path))
            #pyautogui.click(none_x,none_y)
            return False

    def serch_click_image3(self, img_path, img_path2, img_path3, wait_time, conf):
        try:
            img_x,img_y = pyautogui.locateCenterOnScreen(img_path, grayscale=True, confidence=conf)
            #print(img_x)
            loc = pyautogui.position()
            print("X:{}, Y:{}, {}".format(img_x, img_y, img_path))
            pyautogui.moveTo(img_x, img_y, duration=0)
            #pos         = pyautogui.locateCenterOnScreen('search.png')
            pyautogui.click(img_x,img_y)
            pyautogui.moveTo(loc[0], loc[1], duration=0)
            for _ in range(wait_time):
                if(self.serch_click_image2(img_path2, wait_time, conf)):
                    break
                if(self.serch_click_image2(img_path3, wait_time, conf)):
                    break

                time.sleep(1)
            return True
        except:
            print(img_path + ' is none')
            #pyautogui.click(none_x,none_y)
            return False

    def serch_click_image_all(self, img_path, wait_time):
        print(img_path)
        for pos in pyautogui.locateAllOnScreen(img_path, grayscale=True, confidence=0.9):
            cpos = pyautogui.center(pos)
            print("X:{}, Y:{}, {}".format(cpos[0], cpos[1], img_path))
            #画像の中心をクリックする
            loc = pyautogui.position()
            pyautogui.click(cpos)
            pyautogui.moveTo(loc[0], loc[1], duration=0)
            pyautogui.click(loc)
            time.sleep(wait_time)


            if(self.serch_click_image('./img/syutugeki02.PNG', 0)):
                return 1

            if(self.serch_click_image('./img/kaihi.PNG', 0)):
                self.serch_click_image('./img/syutugeki01.PNG', 1)
                return 1

        return True

    def serch_click_image_all2(self, img_path, wait_time, confidence):
        print(img_path)
        #confidence = 0.95
        box = pyautogui.locateAllOnScreen(img_path, grayscale=True, confidence=confidence)
        count_max = len(list(box))
        for i, pos in enumerate(pyautogui.locateAllOnScreen(img_path, grayscale=True, confidence=confidence)):
            (x,y) = pyautogui.center(pos)
            print("({}/{})X:{}, Y:{}, {}".format(i+1, count_max, x, y, img_path))
            #画像の中心をクリックする
            loc = pyautogui.position()
            #pyautogui.moveTo(x+30,y+30, duration=4)

            offset = 0
            pyautogui.click(x+offset,y+offset)
            #pyautogui.moveTo(loc[0], loc[1], duration=0)
            #pyautogui.click(loc)
            time.sleep(wait_time)
        return True