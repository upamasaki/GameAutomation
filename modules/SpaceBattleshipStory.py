

from GameAutomation import GameAutomation
import time

class SpaceBattleshipStory(GameAutomation):
    def __init__(self):
        super(SpaceBattleshipStory, self).__init__()
        self.function = "SpaceBattleshipStory"

    def uchu_main(self):
        while 1:
            print(">>>>>>>>> uchu >>>>>>")
            self.serch_click_image2('./img/uchu/start.png', 1, 0.8)
            # self.serch_click_image2('./img/uchu/close.png', 1, 0.7)
            # self.serch_click_image2('./img/uchu/close2.png', 1, 0.7)
            self.serch_click_image2('./img/uchu/close3.png', 1, 0.8)
            self.serch_click_image2('./img/uchu/close4.png', 1, 0.8)
            self.serch_click_image2('./img/uchu/close5.png', 1, 0.8)
            self.serch_click_image2('./img/uchu/close6.png', 1, 0.8)
            self.serch_click_image2('./img/uchu/close7.png', 1, 0.8)
            self.serch_click_image2('./img/uchu/close8.png', 1, 0.8)
            self.serch_click_image2('./img/uchu/close9.png', 1, 0.8)
            self.serch_click_image2('./img/uchu/close10.png', 1, 0.8)
            self.serch_click_image2('./img/uchu/close11.png', 1, 0.8)
            self.serch_click_image2('./img/uchu/retry.png', 1, 0.8)
            time.sleep(2)


if __name__ == "__main__":
    
    SBS = SpaceBattleshipStory()
    SBS.sample()