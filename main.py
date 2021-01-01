
import sys
import pprint


sys.path.append("./modules")
pprint.pprint(sys.path)

import GameAutomation 
from YoujyoSenki import YoujyoSenki

# マルチスレッド関係
import logging
import threading
import time

##PyAutoGUIのモジュール
import pyautogui

count = 0

def temp(GameAuto):
    counter = 0
    item_get_count = 10
    start = time.time()
    elapsed_time = -1
    
    while 1:
        eval_mode = True
        
        ###############################################
        # 自動化のコードだよ
        #
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/order_flag2.PNG', wait_time=1, conf=0.8, offset=(20, 20), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/item_get_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/close3.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/ok6.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        
def uchu_main(GameAuto):
    while 1:
        print(">>>>>>>>> uchu >>>>>>")
        GameAuto.serch_click_image2('./img/uchu/start.png', 1, 0.8)
        # GameAuto.serch_click_image2('./img/uchu/close.png', 1, 0.7)
        # GameAuto.serch_click_image2('./img/uchu/close2.png', 1, 0.7)
        GameAuto.serch_click_image2('./img/uchu/close3.png', 1, 0.8)
        GameAuto.serch_click_image2('./img/uchu/close4.png', 1, 0.8)
        GameAuto.serch_click_image2('./img/uchu/close5.png', 1, 0.8)
        GameAuto.serch_click_image2('./img/uchu/close6.png', 1, 0.8)
        GameAuto.serch_click_image2('./img/uchu/close7.png', 1, 0.8)
        GameAuto.serch_click_image2('./img/uchu/close8.png', 1, 0.8)
        GameAuto.serch_click_image2('./img/uchu/close9.png', 1, 0.8)
        GameAuto.serch_click_image2('./img/uchu/close10.png', 1, 0.8)
        GameAuto.serch_click_image2('./img/uchu/close11.png', 1, 0.8)
        GameAuto.serch_click_image2('./img/uchu/retry.png', 1, 0.8)
        time.sleep(2)

def sample2(GameAuto):
    while 1:
        GameAuto.press('e')
        time.sleep(1)

def final_gear(GameAuto):
    while 1:
        GameAuto.serch_click_image2('./img/final_gear/event_norm.PNG', 1, 0.8)
        GameAuto.serch_click_image2('./img/final_gear/start.PNG', 1, 0.8)

def DOA_XVV(GameAuto):
    while 1:
        eval_mode = True
        # GameAuto.serch_click_image2(img_path='./img/doaxvv/start_v1.PNG', wait_time=0, conf=0.7, offset=(100, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/doaxvv/start_v1.PNG', wait_time=0, conf=0.7, offset=(100, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/doaxvv/start_v1.PNG', wait_time=0, conf=0.7, offset=(100, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/doaxvv/start_v2.PNG', wait_time=0, conf=0.7, offset=(100, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/doaxvv/start_v2.PNG', wait_time=0, conf=0.7, offset=(100, 0), return_loc=eval_mode)

        # GameAuto.serch_click_image2(img_path='./img/doaxvv/start_v4.PNG', wait_time=0, conf=0.7, offset=(100, 0), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/doaxvv/decide.PNG', wait_time=0, conf=0.7, offset=(0, 0), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/doaxvv/skip_v2.PNG', wait_time=0, conf=0.7, offset=(0, 0), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/doaxvv/start_v4.PNG', wait_time=0, conf=0.7, offset=(0, 0), return_loc=eval_mode)



        # GameAuto.serch_click_image2(img_path='./img/doaxvv/skip.PNG', wait_time=0, conf=0.7, offset=(0, -20), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/doaxvv/skip.PNG', wait_time=0, conf=0.7, offset=(0, -20), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/doaxvv/result.PNG', wait_time=0, conf=0.7, offset=(0, -10), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/doaxvv/event_Arank.PNG', wait_time=0, conf=0.7, offset=(100, 0), return_loc=eval_mode)
        time.sleep(5)






#以下、メインルーチン
if __name__ == "__main__":
       
    GameAuto = GameAutomation.GameAutomation()   
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

    YS = YoujyoSenki()
    YS.youjyo_senki_story_v2()

    # DOA_XVV(GameAuto)
    # for _ in range(5):
    #     print("sleep.....")
    #     time.sleep(1)
    # for _ in range(20):
    #     print("click")
    #     pyautogui.moveTo( 768,  628, duration=0)
    #     # pyautogui.click(1386, 820)
    print("=========================")

        



