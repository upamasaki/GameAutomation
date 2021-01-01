

from GameAutomation import GameAutomation
import time

class NaruKore(GameAutomation):
    def __init__(self):
        super(NaruKore, self).__init__()
        self.function = "NaruKore"


    def narukore_promotion_exam(self):
        #####################################
        # ここからナルコレの関数
        #
        # 昇級試験
        while 1:

            # ----------------------------------------------
            # バトルパート
            #
            self.serch_click_image3(img_path='./img/narukore/challenging.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/narukore/next.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/narukore/mission_start.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/narukore/message.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/narukore/auto_play.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/narukore/total_score.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/narukore/result_pt.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/narukore/pt_tortal.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/narukore/promotion.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/narukore/promotion_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/narukore/next_promotion.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/narukore/shinobi_rank.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            self.serch_click_image3(img_path='./img/narukore/ability.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            # self.serch_click_image3(img_path='./img/narukore/no.PNG', wait_time=2, conf=0.8, offset=(0, 0), return_loc=True)
            # self.serch_click_image3(img_path='./img/narukore/yes_v2.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

            # ----------------------------------------------
            # アイテムで回復
            #
            self.serch_click_image3(img_path='./img/narukore/recover_item.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)
            if(self.serch_click_image3(img_path='./img/narukore/stamina_recover.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)):
                self.serch_click_image3(img_path='./img/narukore/yes.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

            self.serch_click_image3(img_path='./img/narukore/close.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

            # ----------------------------------------------
            # 敗北時
            #
            if(self.serch_click_image3(img_path='./img/narukore/continue_v1.PNG', wait_time=1, conf=0.85, offset=(0, 0), return_loc=True)):
                self.serch_click_image3(img_path='./img/narukore/no_v2.PNG', wait_time=1, conf=0.85, offset=(0, 0), return_loc=True)

            if(self.serch_click_image3(img_path='./img/narukore/retired.PNG', wait_time=1, conf=0.85, offset=(0, 0), return_loc=True)):
                self.serch_click_image3(img_path='./img/narukore/yes_v4.PNG', wait_time=1, conf=0.8, offset=(0, 0), return_loc=True)

            print("sleep........")
            time.sleep(1)



if __name__ == "__main__":
    
    SBS = NaruKore()