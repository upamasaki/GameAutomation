
import sys
import pprint


sys.path.append("./modules")
pprint.pprint(sys.path)

import GameAutomation 
from YoujyoSenki import YoujyoSenki
from NaruKore import NaruKore
from FGO import FGO

# マルチスレッド関係
import logging
import threading
import time

##PyAutoGUIのモジュール
import pyautogui

count = 0


#以下、メインルーチン
if __name__ == "__main__":
       
    print("=========================")
    # uchu_main(GameAuto)
    # sample2(GameAuto)
    # final_gear(GameAuto)
    # kyoshin_seijo_event_humetsu(GameAuto)
    # kyoshin_seijo_event_oujya(GameAuto)
    # youjyo_senki(GameAuto)
    # youjyo_senki_battle(GameAuto)
    # narukore_Promotion_exam(GameAuto)
    # youjyo_senki_story(GameAuto)

    # YS = YoujyoSenki()
    # YS.youjyo_senki_story_v2()

    # NK = NaruKore()
    # NK.narukore_promotion_exam()

    FGO_obj = FGO()
    FGO_obj.story()



    # DOA_XVV(GameAuto)
    # for _ in range(5):
    #     print("sleep.....")
    #     time.sleep(1)
    # for _ in range(20):
    #     print("click")
    #     pyautogui.moveTo( 768,  628, duration=0)
    #     # pyautogui.click(1386, 820)
    print("=========================")

        



