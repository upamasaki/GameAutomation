
import sys
import pprint


sys.path.append("./modules")
pprint.pprint(sys.path)

import GameAutomation 
import time

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
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/order_flag2.PNG', wait_time=1, conf=0.9, offset=(20, 20), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/item_get_v2.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/close3.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/ok6.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=eval_mode)
        


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
        GameAuto.serch_click_image2('./img/uchu/close11.png', 1, 0.9)
        GameAuto.serch_click_image2('./img/uchu/retry.png', 1, 0.8)
        time.sleep(2)

def sample2(GameAuto):
    while 1:
        GameAuto.press('e')
        time.sleep(1)

def final_gear(GameAuto):
    while 1:
        GameAuto.serch_click_image2('./img/final_gear/event_norm.PNG', 1, 0.9)
        GameAuto.serch_click_image2('./img/final_gear/start.PNG', 1, 0.9)

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
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/order_flag2.PNG', wait_time=1, conf=0.9, offset=(20, 20), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/item_get_v2.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/close3.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/ok6.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=eval_mode)
        
        ###############################################
        # 調査距離報酬
        #
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/distance_result_v1.PNG', wait_time=1, conf=0.9, offset=(20, 20), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/item_all_get.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/close_v2.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=eval_mode)
        
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

        GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/ok7.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=eval_mode)

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
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/ok7.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=eval_mode)
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
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/ok7.PNG', wait_time=2, conf=0.9, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/item_get_close.PNG', wait_time=2, conf=0.9, offset=(0, 0), return_loc=eval_mode)
        
        # ###############################################
        # # 探索グリフのセット
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/glyph_set.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/glyph_clear.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/glyph_recomm.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/glyph_back.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=eval_mode)

        # ###############################################
        # # 勝手に探索
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/battle7.PNG', wait_time=1, conf=0.8, offset=(-200, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/ok7.PNG', wait_time=2, conf=0.9, offset=(0, 0), return_loc=eval_mode)

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
        GameAuto.serch_click_image2(img_path='./img/doaxvv/start_v1.PNG', wait_time=0, conf=0.7, offset=(100, 0), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/doaxvv/start_v1.PNG', wait_time=0, conf=0.7, offset=(100, 0), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/doaxvv/start_v1.PNG', wait_time=0, conf=0.7, offset=(100, 0), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/doaxvv/start_v2.PNG', wait_time=0, conf=0.7, offset=(100, 0), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/doaxvv/start_v2.PNG', wait_time=0, conf=0.7, offset=(100, 0), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/doaxvv/skip.PNG', wait_time=0, conf=0.7, offset=(0, -20), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/doaxvv/skip.PNG', wait_time=0, conf=0.7, offset=(0, -20), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/doaxvv/result.PNG', wait_time=0, conf=0.7, offset=(0, -10), return_loc=eval_mode)
        GameAuto.serch_click_image2(img_path='./img/doaxvv/event_Arank.PNG', wait_time=0, conf=0.7, offset=(100, 0), return_loc=eval_mode)
        time.sleep(2)



def youjyo_senki(GameAuto):
    counter = 0
    item_get_count = 10
    start = time.time()
    elapsed_time = -1
    
    while 1:
        eval_mode = True
        
        ###############################################
        # 書類整理
        #        
        if(GameAuto.serch_click_image2(img_path='./img/youjyo/syorui_count.PNG', wait_time=0, conf=0.9, offset=(0, 0), return_loc=eval_mode)):
            GameAuto.serch_click_image2(img_path='./img/youjyo/syorui_v0.PNG', wait_time=0, conf=0.9, offset=(0, 0), return_loc=eval_mode)
            GameAuto.serch_click_image2(img_path='./img/youjyo/syorui_v1.PNG', wait_time=0, conf=0.9, offset=(0, 0), return_loc=eval_mode)
            GameAuto.serch_click_image2(img_path='./img/youjyo/syorui_v2.PNG', wait_time=0, conf=0.9, offset=(0, 0), return_loc=eval_mode)
            GameAuto.serch_click_image2(img_path='./img/youjyo/syorui_v3.PNG', wait_time=0, conf=0.9, offset=(0, 0), return_loc=eval_mode)
            GameAuto.serch_click_image2(img_path='./img/youjyo/syorui_v4.PNG', wait_time=0, conf=0.9, offset=(0, 0), return_loc=eval_mode)
            GameAuto.serch_click_image2(img_path='./img/youjyo/syorui_v5.PNG', wait_time=0, conf=0.9, offset=(0, 0), return_loc=eval_mode)
            GameAuto.serch_click_image2(img_path='./img/youjyo/syorui_v6.PNG', wait_time=0, conf=0.9, offset=(0, 0), return_loc=eval_mode)
            GameAuto.serch_click_image2(img_path='./img/youjyo/syorui_close.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=eval_mode)
        else:
            GameAuto.serch_click_image2(img_path='./img/youjyo/syorui.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=eval_mode)
            GameAuto.serch_click_image2(img_path='./img/youjyo/syorui_ok.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=eval_mode)
    

            time.sleep(1)
        # raise
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/item_get_v2.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/close3.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=eval_mode)
        # GameAuto.serch_click_image2(img_path='./img/kyoshintoseijyo/ok6.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=eval_mode)
        





#以下、メインルーチン
if __name__ == "__main__":
       
    GameAuto = GameAutomation.GameAutomation()   
    print("=========================")
    # uchu_main(GameAuto)
    # sample2(GameAuto)
    # final_gear(GameAuto)
    # kyoshin_seijo_event_humetsu(GameAuto)
    # kyoshin_seijo_event_oujya(GameAuto)
    youjyo_senki(GameAuto)
    # DOA_XVV(GameAuto)
    print("=========================")

        



