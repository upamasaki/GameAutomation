

from GameAutomation import GameAutomation
import threading
import time

class KyoshinSeijo(GameAutomation):
    def __init__(self):
        super(KyoshinSeijo, self).__init__()
        self.function = "KyoshinSeijo"


    def kyoshin_seijo_event_humetsu(self):
        counter = 0
        item_get_count = 10
        start = time.time()
        elapsed_time = -1
        
        while 1:
            eval_mode = True
            
            ###############################################
            # オーダーの報酬一括受け取り
            #
            self.serch_click_image2(img_path='./img/kyoshintoseijyo/order_flag2.PNG', wait_time=1, conf=0.8, offset=(20, 20), return_loc=eval_mode)
            self.serch_click_image2(img_path='./img/kyoshintoseijyo/item_get_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            self.serch_click_image2(img_path='./img/kyoshintoseijyo/close3.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            self.serch_click_image2(img_path='./img/kyoshintoseijyo/ok6.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            
            ###############################################
            # 調査距離報酬
            #
            self.serch_click_image2(img_path='./img/kyoshintoseijyo/distance_result_v1.PNG', wait_time=1, conf=0.8, offset=(20, 20), return_loc=eval_mode)
            self.serch_click_image2(img_path='./img/kyoshintoseijyo/item_all_get.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            self.serch_click_image2(img_path='./img/kyoshintoseijyo/close_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            
            ###############################################
            # 戦闘
            #
            self.serch_click_image2(img_path='./img/kyoshintoseijyo/battle5.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            if(self.serch_click_image2(img_path='./img/kyoshintoseijyo/battle6.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)):
                elapsed_time = time.time() - start
                counter = counter + 1
                start = time.time()

            if(counter % item_get_count == 0):
                self.serch_click_image2(img_path='./img/kyoshintoseijyo/retry_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            else:
                self.serch_click_image2(img_path='./img/kyoshintoseijyo/come_back_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)

            print("counter : {}, elapsed_time : {:6.3f}".format(counter, elapsed_time))

            self.serch_click_image2(img_path='./img/kyoshintoseijyo/ok7.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)

            time.sleep(2)

    def kyoshin_seijo_event_oujya(self):
        while 1:
            eval_mode = True
            
            # ###############################################
            # # オーダーの獲得
            # #
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/order_v3.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/order_v3.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/item_get_v3.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/ok8.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/close4.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)

            # ###############################################
            # # 通常の戦闘
            # #
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/battle7.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/battle8.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/ok7.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/come_back_v3.PNG', wait_time=3, conf=0.8, offset=(0, 0), return_loc=eval_mode)


            # ###############################################
            # # イベントアイテムの交換
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/event_item.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/oujya_soshina.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/item_plus.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/item_plus.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/item_plus.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/item_plus.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/item_plus.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/item_exchange.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/ok7.PNG', wait_time=2, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/item_get_close.PNG', wait_time=2, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            
            # ###############################################
            # # 探索グリフのセット
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/glyph_set.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/glyph_clear.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/glyph_recomm.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/glyph_back.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)

            # ###############################################
            # # 勝手に探索
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/battle7.PNG', wait_time=1, conf=0.8, offset=(-200, 0), return_loc=eval_mode)
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/ok7.PNG', wait_time=2, conf=0.8, offset=(0, 0), return_loc=eval_mode)

            ###############################################
            # 託すを発動
            self.serch_click_image2(img_path='./img/kyoshintoseijyo/takusu_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            self.serch_click_image2(img_path='./img/kyoshintoseijyo/takusu_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            self.serch_click_image2(img_path='./img/kyoshintoseijyo/takusu_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            self.serch_click_image2(img_path='./img/kyoshintoseijyo/takusu_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)



            time.sleep(1)

