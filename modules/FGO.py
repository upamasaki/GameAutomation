

from GameAutomation import GameAutomation
import time

class FGO(GameAutomation):
    def __init__(self):
        super(FGO, self).__init__()
        self.function = "FGO"

    def sample(self):
        print(self.function)


    def story(self):
        #####################################
        # FGOの関数
        #
        # story
        while 1:

            # ----------------------------------------------
            # story choice
            #
            if(self.serch_image2(img_path='./img/fgo/story/tokuiten.PNG', wait_time=1, conf=0.7)):    
                self.serch_click_image3(img_path='./img/fgo/story/next_stage_v1.PNG', wait_time=1, conf=0.7, offset=(0, 70), return_loc=True)
                self.serch_click_image3(img_path='./img/fgo/story/next_stage_v2.PNG', wait_time=1, conf=0.7, offset=(0, 70), return_loc=True)
            self.serch_click_image3(img_path='./img/fgo/story/new_stage_v1.PNG', wait_time=1, conf=0.7, offset=(0, 50), return_loc=True)

            # ----------------------------------------------
            # battle preparation
            #
            # self.serch_click_image3(img_path='./img/fgo/battle/advantageous.PNG', wait_time=1, conf=0.7, offset=(0, 50), return_loc=True)
            if(not self.serch_click_image3(img_path='./img/fgo/battle/suport.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=True)):
                self.serch_click_image3(img_path='./img/fgo/battle/suport_list.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            
            self.serch_click_image3(img_path='./img/fgo/battle/quest_start.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

            # ----------------------------------------------
            # story 
            #
            self.serch_click_image3(img_path='./img/fgo/story/skip.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            if(self.serch_image2(img_path='./img/fgo/story/event_skip_sentence.PNG', wait_time=1, conf=0.9)):
                self.serch_click_image3(img_path='./img/fgo/story/yes.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

            # ----------------------------------------------
            # battle preparation
            #
            self.serch_click_image3(img_path='./img/fgo/battle/atack.PNG', wait_time=3, conf=0.7, offset=(0, 0), return_loc=True)
            if(self.serch_image2(img_path='./img/fgo/battle/back.PNG', wait_time=1, conf=0.9)):
                
                self.serch_click_image3(img_path='./img/fgo/battle/hougu.PNG', wait_time=2, conf=0.95, offset=(0, 0), return_loc=True)
                # buster
                for _ in range(6):
                    self.serch_click_image3(img_path='./img/fgo/battle/buster.PNG', wait_time=2, conf=0.8, offset=(0, 0), return_loc=True)
                # arts
                for _ in range(6):
                    self.serch_click_image3(img_path='./img/fgo/battle/arts.PNG', wait_time=2, conf=0.8, offset=(0, 0), return_loc=True)
                # quick
                for _ in range(6):
                    self.serch_click_image3(img_path='./img/fgo/battle/quick.PNG', wait_time=2, conf=0.8, offset=(0, 0), return_loc=True)

            # ----------------------------------------------
            # battle result
            #
            self.serch_click_image3(img_path='./img/fgo/battle/result.PNG', wait_time=1, conf=0.7, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/fgo/battle/next.PNG', wait_time=1, conf=0.7, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/fgo/battle/stage_result.PNG', wait_time=1, conf=0.7, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/fgo/battle/display_touch.PNG', wait_time=1, conf=0.7, offset=(0, 0), return_loc=True)

            self.serch_click_image3(img_path='./img/fgo/battle/friend_end.PNG', wait_time=1, conf=0.7, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/fgo/battle/withdrawal.PNG', wait_time=1, conf=0.7, offset=(0, 0), return_loc=True)
            if(self.serch_image2(img_path='./img/fgo/battle/withdrawal_sentence.PNG', wait_time=1, conf=0.9)):
                self.serch_click_image3(img_path='./img/fgo/battle/decide.PNG', wait_time=1, conf=0.7, offset=(0, 0), return_loc=True)
            
            self.serch_click_image3(img_path='./img/fgo/battle/close.PNG', wait_time=1, conf=0.7, offset=(0, 0), return_loc=True)
            

            time.sleep(1)

            
    def level_up_item(self):
        #####################################
        # FGOの関数
        #
        # story
        while 1:

            # ----------------------------------------------
            # story choice
            #
            # if(self.serch_image2(img_path='./img/fgo/story/tokuiten.PNG', wait_time=1, conf=0.7)):    
            #     self.serch_click_image3(img_path='./img/fgo/story/next_stage_v1.PNG', wait_time=1, conf=0.7, offset=(0, 70), return_loc=True)
            #     self.serch_click_image3(img_path='./img/fgo/story/next_stage_v2.PNG', wait_time=1, conf=0.7, offset=(0, 70), return_loc=True)
            self.serch_click_image3(img_path='./img/fgo/battle/ap15.PNG', wait_time=1, conf=0.7, offset=(0, 50), return_loc=True)

            
            # ----------------------------------------------
            # battle preparation
            #
            # self.serch_click_image3(img_path='./img/fgo/battle/advantageous.PNG', wait_time=1, conf=0.7, offset=(0, 50), return_loc=True)
            if(not self.serch_click_image3(img_path='./img/fgo/battle/suport.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=True)):
                self.serch_click_image3(img_path='./img/fgo/battle/suport_list.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            
            self.serch_click_image3(img_path='./img/fgo/battle/quest_start.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

            # ----------------------------------------------
            # story 
            #
            self.serch_click_image3(img_path='./img/fgo/story/skip.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            if(self.serch_image2(img_path='./img/fgo/story/event_skip_sentence.PNG', wait_time=1, conf=0.9)):
                self.serch_click_image3(img_path='./img/fgo/story/yes.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)


            # ----------------------------------------------
            # battle preparation
            #
            self.serch_click_image3(img_path='./img/fgo/battle/atack.PNG', wait_time=3, conf=0.7, offset=(0, 0), return_loc=True)
            if(self.serch_image2(img_path='./img/fgo/battle/back.PNG', wait_time=1, conf=0.9)):
                
                self.serch_click_image3(img_path='./img/fgo/battle/hougu.PNG', wait_time=2, conf=0.95, offset=(0, 0), return_loc=True)
                # buster
                for _ in range(6):
                    self.serch_click_image3(img_path='./img/fgo/battle/buster.PNG', wait_time=2, conf=0.8, offset=(0, 0), return_loc=True)
                # arts
                for _ in range(6):
                    self.serch_click_image3(img_path='./img/fgo/battle/arts.PNG', wait_time=2, conf=0.8, offset=(0, 0), return_loc=True)
                # quick
                for _ in range(6):
                    self.serch_click_image3(img_path='./img/fgo/battle/quick.PNG', wait_time=2, conf=0.8, offset=(0, 0), return_loc=True)

            self.serch_click_image3(img_path='./img/fgo/battle/result.PNG', wait_time=1, conf=0.7, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/fgo/battle/next.PNG', wait_time=1, conf=0.7, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/fgo/battle/stage_result.PNG', wait_time=1, conf=0.7, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/fgo/battle/display_touch.PNG', wait_time=1, conf=0.7, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/fgo/battle/friend_end.PNG', wait_time=1, conf=0.7, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/fgo/battle/withdrawal.PNG', wait_time=1, conf=0.7, offset=(0, 0), return_loc=True)
            if(self.serch_image2(img_path='./img/fgo/battle/withdrawal_sentence.PNG', wait_time=1, conf=0.9)):
                self.serch_click_image3(img_path='./img/fgo/battle/decide.PNG', wait_time=1, conf=0.7, offset=(0, 0), return_loc=True)
            
            self.serch_click_image3(img_path='./img/fgo/battle/close.PNG', wait_time=1, conf=0.7, offset=(0, 0), return_loc=True)
            


            time.sleep(1)
            # self.serch_click_image3(img_path='./img/narukore/next.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            # self.serch_click_image3(img_path='./img/narukore/mission_start.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            # self.serch_click_image3(img_path='./img/narukore/message.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            # self.serch_click_image3(img_path='./img/narukore/auto_play.PNG', wait_time=1, conf=0.9, offset=(0, 0), return_loc=True)