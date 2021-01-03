

from GameAutomation import GameAutomation
import threading
import time

class YoujyoSenki(GameAutomation):
    def __init__(self):
        super(YoujyoSenki, self).__init__()
        self.function = "YoujyoSenki"

    def youjyo_senki(self):

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
            if(self.serch_click_image2(img_path='./img/youjyo/syorui_count.PNG', wait_time=0, conf=0.8, offset=(0, 0), return_loc=eval_mode)):
                self.serch_click_image2(img_path='./img/youjyo/syorui_v0.PNG', wait_time=0, conf=0.8, offset=(0, 0), return_loc=eval_mode)
                self.serch_click_image2(img_path='./img/youjyo/syorui_v1.PNG', wait_time=0, conf=0.8, offset=(0, 0), return_loc=eval_mode)
                self.serch_click_image2(img_path='./img/youjyo/syorui_v2.PNG', wait_time=0, conf=0.8, offset=(0, 0), return_loc=eval_mode)
                self.serch_click_image2(img_path='./img/youjyo/syorui_v3.PNG', wait_time=0, conf=0.8, offset=(0, 0), return_loc=eval_mode)
                self.serch_click_image2(img_path='./img/youjyo/syorui_v4.PNG', wait_time=0, conf=0.8, offset=(0, 0), return_loc=eval_mode)
                self.serch_click_image2(img_path='./img/youjyo/syorui_v5.PNG', wait_time=0, conf=0.8, offset=(0, 0), return_loc=eval_mode)
                self.serch_click_image2(img_path='./img/youjyo/syorui_v6.PNG', wait_time=0, conf=0.8, offset=(0, 0), return_loc=eval_mode)
                self.serch_click_image2(img_path='./img/youjyo/syorui_close.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            else:
                self.serch_click_image2(img_path='./img/youjyo/syorui.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
                self.serch_click_image2(img_path='./img/youjyo/syorui_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
        

                time.sleep(1)
            # raise
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/item_get_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/close3.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            # self.serch_click_image2(img_path='./img/kyoshintoseijyo/ok6.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=eval_mode)
            



    def youjyo_senki_multi(self):

        def _syorui_worker(img_path=None, count=10):

            while 1:
                for _ in range(count):
                    self.serch_click_image3(img_path=img_path, wait_time=0, conf=0.8, offset=(0, 0), return_loc=True)


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
    

    def youjyo_senki_battle(self):

        def _syorui_worker():
            
            while 1:

                # if(self.serch_image2(img_path='./img/youjyo/drop_info.PNG', wait_time=1, conf=0.8)):
                #     self.serch_click_image3(img_path='./img/youjyo/battle_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

                # if(self.serch_image2(img_path='./img/youjyo/battle_result.PNG', wait_time=1, conf=0.8) or 
                #     self.serch_image2(img_path='./img/youjyo/friend.PNG', wait_time=1, conf=0.8)):
                self.serch_click_image3(img_path='./img/youjyo/retry.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

                self.serch_click_image3(img_path='./img/youjyo/level_up.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

                print("sleep........")
                time.sleep(10)
        

        _syorui_worker()

    def youjyo_senki_story(self):

        while 1:

            ##########################################
            # メニュー画面関係
            #
            # 進行中の章がなければnewのマークがある章を進める
            if(not self.serch_click_image3(img_path='./img/youjyo/story/stage_new_v3.PNG', wait_time=1, conf=0.7, offset=(10, 10), return_loc=True)):
                # new マークがない場合は下へスクロール
                self.serch_drag_image(img_path='./img/youjyo/story/stage_clear.PNG', wait_time=1, conf=0.8, offset=(0, -50))
            if(not self.serch_click_image3(img_path='./img/youjyo/story/stage_new_v2.PNG', wait_time=1, conf=0.7, offset=(10, 10), return_loc=True)):
                # new マークがない場合は下へスクロール
                self.serch_drag_image(img_path='./img/youjyo/story/stage_clear.PNG', wait_time=1, conf=0.8, offset=(0, -50))
            # 進行中の章があればその章を進める
            self.serch_click_image3(img_path='./img/youjyo/story/now_stage.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

            self.serch_click_image3(img_path='./img/youjyo/story/new_chapter.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            
            # チェックボックスのあるバトルパートを行う
            if(not self.serch_click_image3(img_path='./img/youjyo/story/battle_check3.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)):
                if(self.serch_click_image3(img_path='./img/youjyo/story/unopened.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)):
                    # チェックボックスがない場合はストーリーを見る
                    self.serch_click_image3(img_path='./img/youjyo/story/stage_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
                else:
                    # 未開放バトルパートがなくなったら戻る
                    if(self.serch_click_image3(img_path='./img/youjyo/story/battle_info.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)):
                        self.serch_click_image3(img_path='./img/youjyo/story/stage_back.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

            # ストーリーはskipする
            self.serch_click_image3(img_path='./img/youjyo/story/skip.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

            self.serch_click_image3(img_path='./img/youjyo/story/stage_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/youjyo/story/stage_go.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)


            ##########################################
            # バトル関係
            #
            self.serch_click_image3(img_path='./img/youjyo/miss_comp.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/youjyo/next.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/youjyo/item_get.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            if(self.serch_image2(img_path='./img/youjyo/retry.PNG', wait_time=1, conf=0.8)):
                self.serch_click_image3(img_path='./img/youjyo/battle_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
                self.serch_click_image3(img_path='./img/youjyo/battle_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
                self.serch_click_image3(img_path='./img/youjyo/battle_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
                self.serch_click_image3(img_path='./img/youjyo/battle_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            

            print("sleep........")
            time.sleep(1)
        
    def youjyo_senki_story_v2(self):

        while 1:

            ##########################################
            # メニュー画面関係
            #
            # ---------------------------------------
            # 章の選択
            # ---------------------------------------
            #
            if(self.serch_image2(img_path='./img/youjyo/story/scenario_selection.PNG', wait_time=1, conf=0.8)):
                # 下へスクロール   
                self.serch_drag_image(img_path='./img/youjyo/story/stage_clear.PNG', wait_time=1, conf=0.8, offset=(0, -100))
                self.serch_drag_image(img_path='./img/youjyo/story/stage_comp.PNG', wait_time=1, conf=0.8, offset=(0, -100))

                if(not self.serch_click_image3(img_path='./img/youjyo/story/now_stage_v2.PNG', wait_time=1, conf=0.9, offset=(10, 10), return_loc=True)):
                    #
                    # 進行中の章があればその章を進める
                    self.serch_click_image3(img_path='./img/youjyo/story/now_stage.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=True)
                    #
                    # 進行中の章がなければnewのマークがある章を進める
                    self.serch_click_image3(img_path='./img/youjyo/story/stage_new_v3.PNG', wait_time=1, conf=0.7, offset=(10, 10), return_loc=True)
                    self.serch_click_image3(img_path='./img/youjyo/story/stage_new_v2.PNG', wait_time=1, conf=0.7, offset=(10, 10), return_loc=True)


            self.serch_click_image3(img_path='./img/youjyo/story/new_chapter.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            #
            # ---------------------------------------
            # バトルパートの選択
            # ---------------------------------------
            #
            # 未開放が画面内に無い場合はスクロール
            if(not self.serch_image2(img_path='./img/youjyo/story/unopened.PNG', wait_time=1, conf=0.8)):
                self.serch_drag_image(img_path='./img/youjyo/story/battle_name.PNG', wait_time=1, conf=0.8, offset=(0, -100))
            #
            # チェックボックスのあるバトルパートを行う
            if(not self.serch_click_image3(img_path='./img/youjyo/story/battle_check3.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)):
                if(self.serch_click_image3(img_path='./img/youjyo/story/unopened.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)):
                    # チェックボックスがない場合はストーリーを見る
                    self.serch_click_image3(img_path='./img/youjyo/story/stage_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
                else:
                    # 未開放バトルパートがなくなったら戻る
                    if(self.serch_click_image3(img_path='./img/youjyo/story/battle_info.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)):
                        self.serch_click_image3(img_path='./img/youjyo/story/stage_back.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

            # ストーリーはskipする
            self.serch_click_image3(img_path='./img/youjyo/story/skip.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

            self.serch_click_image3(img_path='./img/youjyo/story/stage_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/youjyo/story/stage_go.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)


            ##########################################
            # バトル関係
            #
            self.serch_click_image3(img_path='./img/youjyo/miss_comp.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/youjyo/next.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/youjyo/item_get.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            if(self.serch_image2(img_path='./img/youjyo/retry.PNG', wait_time=1, conf=0.8)):
                self.serch_click_image3(img_path='./img/youjyo/battle_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
                self.serch_click_image3(img_path='./img/youjyo/battle_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
                self.serch_click_image3(img_path='./img/youjyo/battle_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
                self.serch_click_image3(img_path='./img/youjyo/battle_ok.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            

            print("sleep........")
            time.sleep(1)
        





if __name__ == "__main__":
    
    SBS = YoujyoSenki()
    SBS.sample()