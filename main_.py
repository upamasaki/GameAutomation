
import sys
import pprint


sys.path.append("./modules")
pprint.pprint(sys.path)

import GameAutomation 

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

def kyoshin_seijo_event_humetsu(GameAuto):
    counter = 0
    item_get_count = 10
    start = time.time()
    elapsed_time = -1
    
    while 1:
        eval_mode = True
        
        ###############################################
        # オーダーの報酬一括受け取り
        #
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/order_flag2.PNG', wait_time=1, conf=0.8, offset=(20, 20), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/item_get_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/close3.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/ok6.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        
        ###############################################
        # 調査距離報酬
        #
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/distance_result_v1.PNG', wait_time=1, conf=0.8, offset=(20, 20), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/item_all_get.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/close_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        
        ###############################################
        # 戦闘
        #
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/battle5.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        if(GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/battle6.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)):
            elapsed_time = time.time() - start
            counter = counter + 1
            start = time.time()

        if(counter % item_get_count == 0):
            GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/retry_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        else:
            GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/come_back_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)

        print("counter : {}, elapsed_time : {:6.3f}".format(counter, elapsed_time))

        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/ok7.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)

        time.sleep(2)

def kyoshin_seijo_event_oujya(GameAuto):
    while 1:
        eval_mode = True
        
        # ###############################################
        # # オーダーの獲得
        # #
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/order_v3.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/order_v3.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/item_get_v3.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/ok8.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/close4.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)

        # ###############################################
        # # 通常の戦闘
        # #
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/battle7.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/battle8.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/ok7.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/come_back_v3.PNG', wait_time=3, conf=0.8, offset=(0, 0), return_loc=eval_mode)


        # ###############################################
        # # イベントアイテムの交換
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/event_item.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/oujya_soshina.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/item_plus.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/item_plus.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/item_plus.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/item_plus.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/item_plus.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/item_exchange.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/ok7.PNG', wait_time=2, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/item_get_close.PNG', wait_time=2, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        
        # ###############################################
        # # 探索グリフのセット
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/glyph_set.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/glyph_clear.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/glyph_recomm.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/glyph_back.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)

        # ###############################################
        # # 勝手に探索
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/battle7.PNG', wait_time=1, conf=0.8, offset=(-200, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/ok7.PNG', wait_time=2, conf=0.8, offset=(0, 0), return_loc=eval_mode)

        ###############################################
        # 託すを発動
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/takusu_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/takusu_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/takusu_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/takusu_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)



        time.sleep(1)

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

def youjyo_senki(GameAuto):

    counter = 0
    item_get_count = 50
    start = time.time()
    syorui_count = 50
    elapsed_time = -1
    
    while 1:
        eval_mode = True
        
        ###############################################
        # 書類整理
        #        
        if(GameAuto.serch_click_image2(img_path='./img/youjyo/syorui_count.PNG', wait_time=0, conf=0.8, offset=(0, 0), return_loc=eval_mode)):
            GameAuto.serch_click_image2(img_path='./img/youjyo/syorui_v0.PNG', wait_time=0, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            GameAuto.serch_click_image2(img_path='./img/youjyo/syorui_v1.PNG', wait_time=0, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            GameAuto.serch_click_image2(img_path='./img/youjyo/syorui_v2.PNG', wait_time=0, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            GameAuto.serch_click_image2(img_path='./img/youjyo/syorui_v3.PNG', wait_time=0, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            GameAuto.serch_click_image2(img_path='./img/youjyo/syorui_v4.PNG', wait_time=0, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            GameAuto.serch_click_image2(img_path='./img/youjyo/syorui_v5.PNG', wait_time=0, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            GameAuto.serch_click_image2(img_path='./img/youjyo/syorui_v6.PNG', wait_time=0, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            GameAuto.serch_click_image2(img_path='./img/youjyo/syorui_close.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        else:
            GameAuto.serch_click_image2(img_path='./img/youjyo/syorui.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            GameAuto.serch_click_image2(img_path='./img/youjyo/syorui_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
    

            time.sleep(1)
        # raise
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/item_get_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/close3.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/ok6.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        
def youjyo_senki_multi(GameAuto):

    def _syorui_worker(img_path=None, count=10):

        while 1:
            for _ in range(count):
                GameAuto.serch_click_image3(img_path=img_path, wait_time=0, conf=0.8, offset=(0, 0), return_loc=True)


    counter = 0
    item_get_count = 50
    start = time.time()
    syorui_count = 50
    
    syorui_list = [ './img/youjyo/syorui_v0.PNG', 
                    './img/youjyo/syorui_v1.PNG', 
                    './img/youjyo/syorui_v2.PNG',
                    './img/youjyo/syorui_v3.PNG',
                    './img/youjyo/syorui_v4.PNG',
                    './img/youjyo/syorui_v6.PNG',
                    './img/youjyo/syorui_v7.PNG',
                    './img/youjyo/level_up.PNG',
                    './img/youjyo/syorui_close.PNG',
                    './img/youjyo/syorui.PNG',
                    './img/youjyo/syorui_ok.PNG',]

    # スレッドを 5 個つくる
    for i in range(len(syorui_list)):
        t = threading.Thread(target=_syorui_worker, kwargs={'img_path': syorui_list[i], 'count' : syorui_count})
        # t.setDaemon(True)
        t.start()
  
def youjyo_senki_battle(GameAuto):

    def _syorui_worker():
        
        while 1:

            # if(GameAuto.serch_image2(img_path='./img/youjyo/drop_info.PNG', wait_time=1, conf=0.8)):
            #     GameAuto.serch_click_image3(img_path='./img/youjyo/battle_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

            # if(GameAuto.serch_image2(img_path='./img/youjyo/battle_result.PNG', wait_time=1, conf=0.8) or 
            #     GameAuto.serch_image2(img_path='./img/youjyo/friend.PNG', wait_time=1, conf=0.8)):
            GameAuto.serch_click_image3(img_path='./img/youjyo/retry.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

            GameAuto.serch_click_image3(img_path='./img/youjyo/level_up.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

            print("sleep........")
            time.sleep(10)
    

    _syorui_worker()

def youjyo_senki_story(GameAuto):

    while 1:

        ##########################################
        # メニュー画面関係
        #
        # 進行中の章がなければnewのマークがある章を進める
        if(not GameAuto.serch_click_image3(img_path='./img/youjyo/story/stage_new_v3.PNG', wait_time=1, conf=0.7, offset=(10, 10), return_loc=True)):
            # new マークがない場合は下へスクロール
            GameAuto.serch_drag_image(img_path='./img/youjyo/story/stage_clear.PNG', wait_time=1, conf=0.8, offset=(0, -50))
        if(not GameAuto.serch_click_image3(img_path='./img/youjyo/story/stage_new_v2.PNG', wait_time=1, conf=0.7, offset=(10, 10), return_loc=True)):
            # new マークがない場合は下へスクロール
            GameAuto.serch_drag_image(img_path='./img/youjyo/story/stage_clear.PNG', wait_time=1, conf=0.8, offset=(0, -50))
        # 進行中の章があればその章を進める
        GameAuto.serch_click_image3(img_path='./img/youjyo/story/now_stage.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

        GameAuto.serch_click_image3(img_path='./img/youjyo/story/new_chapter.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        
        # チェックボックスのあるバトルパートを行う
        if(not GameAuto.serch_click_image3(img_path='./img/youjyo/story/battle_check3.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)):
            if(GameAuto.serch_click_image3(img_path='./img/youjyo/story/unopened.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)):
                # チェックボックスがない場合はストーリーを見る
                GameAuto.serch_click_image3(img_path='./img/youjyo/story/stage_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            else:
                # 未開放バトルパートがなくなったら戻る
                if(GameAuto.serch_click_image3(img_path='./img/youjyo/story/battle_info.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)):
                    GameAuto.serch_click_image3(img_path='./img/youjyo/story/stage_back.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

        # ストーリーはskipする
        GameAuto.serch_click_image3(img_path='./img/youjyo/story/skip.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

        GameAuto.serch_click_image3(img_path='./img/youjyo/story/stage_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        GameAuto.serch_click_image3(img_path='./img/youjyo/story/stage_go.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)


        ##########################################
        # バトル関係
        #
        GameAuto.serch_click_image3(img_path='./img/youjyo/miss_comp.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        GameAuto.serch_click_image3(img_path='./img/youjyo/next.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        GameAuto.serch_click_image3(img_path='./img/youjyo/item_get.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        if(GameAuto.serch_image2(img_path='./img/youjyo/retry.PNG', wait_time=1, conf=0.8)):
            GameAuto.serch_click_image3(img_path='./img/youjyo/battle_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            GameAuto.serch_click_image3(img_path='./img/youjyo/battle_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            GameAuto.serch_click_image3(img_path='./img/youjyo/battle_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            GameAuto.serch_click_image3(img_path='./img/youjyo/battle_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        

        print("sleep........")
        time.sleep(1)
    
def youjyo_senki_story_v2(GameAuto):

    while 1:

        ##########################################
        # メニュー画面関係
        #
        # 進行中の章がなければnewのマークがある章を進める
        if(not GameAuto.serch_click_image3(img_path='./img/youjyo/story/stage_new_v3.PNG', wait_time=1, conf=0.7, offset=(10, 10), return_loc=True)):
            # new マークがない場合は下へスクロール
            GameAuto.serch_drag_image(img_path='./img/youjyo/story/stage_clear.PNG', wait_time=1, conf=0.8, offset=(0, -50))
        if(not GameAuto.serch_click_image3(img_path='./img/youjyo/story/stage_new_v2.PNG', wait_time=1, conf=0.7, offset=(10, 10), return_loc=True)):
            # new マークがない場合は下へスクロール
            GameAuto.serch_drag_image(img_path='./img/youjyo/story/stage_clear.PNG', wait_time=1, conf=0.8, offset=(0, -50))
        # 進行中の章があればその章を進める
        GameAuto.serch_click_image3(img_path='./img/youjyo/story/now_stage.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

        GameAuto.serch_click_image3(img_path='./img/youjyo/story/new_chapter.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        
        # チェックボックスのあるバトルパートを行う
        if(not GameAuto.serch_click_image3(img_path='./img/youjyo/story/battle_check3.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)):
            if(GameAuto.serch_click_image3(img_path='./img/youjyo/story/unopened.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)):
                # チェックボックスがない場合はストーリーを見る
                GameAuto.serch_click_image3(img_path='./img/youjyo/story/stage_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            else:
                # 未開放バトルパートがなくなったら戻る
                if(GameAuto.serch_click_image3(img_path='./img/youjyo/story/battle_info.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)):
                    GameAuto.serch_click_image3(img_path='./img/youjyo/story/stage_back.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

        # ストーリーはskipする
        GameAuto.serch_click_image3(img_path='./img/youjyo/story/skip.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

        GameAuto.serch_click_image3(img_path='./img/youjyo/story/stage_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        GameAuto.serch_click_image3(img_path='./img/youjyo/story/stage_go.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)


        ##########################################
        # バトル関係
        #
        GameAuto.serch_click_image3(img_path='./img/youjyo/miss_comp.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        GameAuto.serch_click_image3(img_path='./img/youjyo/next.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        GameAuto.serch_click_image3(img_path='./img/youjyo/item_get.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        if(GameAuto.serch_image2(img_path='./img/youjyo/retry.PNG', wait_time=1, conf=0.8)):
            GameAuto.serch_click_image3(img_path='./img/youjyo/battle_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            GameAuto.serch_click_image3(img_path='./img/youjyo/battle_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            GameAuto.serch_click_image3(img_path='./img/youjyo/battle_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            GameAuto.serch_click_image3(img_path='./img/youjyo/battle_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        

        print("sleep........")
        time.sleep(1)
    

def narukore_Promotion_exam(GameAuto):
#####################################
# ここからナルコレの関数
#
# 昇級試験
    while 1:


        # ----------------------------------------------
        # バトルパート
        #
        GameAuto.serch_click_image3(img_path='./img/narukore/challenging.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        GameAuto.serch_click_image3(img_path='./img/narukore/next.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        GameAuto.serch_click_image3(img_path='./img/narukore/mission_start.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        GameAuto.serch_click_image3(img_path='./img/narukore/message.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        GameAuto.serch_click_image3(img_path='./img/narukore/auto_play.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        GameAuto.serch_click_image3(img_path='./img/narukore/total_score.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        GameAuto.serch_click_image3(img_path='./img/narukore/result_pt.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        GameAuto.serch_click_image3(img_path='./img/narukore/pt_tortal.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        GameAuto.serch_click_image3(img_path='./img/narukore/promotion.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        GameAuto.serch_click_image3(img_path='./img/narukore/promotion_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        GameAuto.serch_click_image3(img_path='./img/narukore/next_promotion.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        GameAuto.serch_click_image3(img_path='./img/narukore/shinobi_rank.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        GameAuto.serch_click_image3(img_path='./img/narukore/ability.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        # GameAuto.serch_click_image3(img_path='./img/narukore/no.PNG', wait_time=2, conf=0.8, offset=(0, 0), return_loc=True)
        # GameAuto.serch_click_image3(img_path='./img/narukore/yes_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

        # ----------------------------------------------
        # アイテムで回復
        #
        GameAuto.serch_click_image3(img_path='./img/narukore/recover_item.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
        if(GameAuto.serch_click_image3(img_path='./img/narukore/stamina_recover.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)):
            GameAuto.serch_click_image3(img_path='./img/narukore/yes.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

        GameAuto.serch_click_image3(img_path='./img/narukore/close.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

        # ----------------------------------------------
        # 敗北時
        #
        if(GameAuto.serch_click_image3(img_path='./img/narukore/continue_v1.PNG', wait_time=1, conf=0.85, offset=(0, 0), return_loc=True)):
            GameAuto.serch_click_image3(img_path='./img/narukore/no_v2.PNG', wait_time=1, conf=0.85, offset=(0, 0), return_loc=True)

        if(GameAuto.serch_click_image3(img_path='./img/narukore/retired.PNG', wait_time=1, conf=0.85, offset=(0, 0), return_loc=True)):
            GameAuto.serch_click_image3(img_path='./img/narukore/yes_v4.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

        print("sleep........")
        time.sleep(1)




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
    youjyo_senki_story(GameAuto)
    # DOA_XVV(GameAuto)
    # for _ in range(5):
    #     print("sleep.....")
    #     time.sleep(1)
    # for _ in range(20):
    #     print("click")
    #     pyautogui.moveTo( 768,  628, duration=0)
    #     # pyautogui.click(1386, 820)
    print("=========================")

        



