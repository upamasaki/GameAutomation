import pyautogui
import sys
import time

screen_x,screen_y = pyautogui.size()
curmus_x,curmus_y = pyautogui.position()
print (u"printについてる[u]はunicodeにするのuでマルチバイト表記が化けるときにつけるよ")
print (u"画面サイズ [" + str(screen_x) + "]/[" + str(screen_y) + "]")
print (u"現在のマウス位置 [" + str(curmus_x) + "]/[" + str(curmus_y) + "]")