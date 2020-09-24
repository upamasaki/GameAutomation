
import sys
import pprint


sys.path.append("./modules")
pprint.pprint(sys.path)

import GameAutomation 
import time

count = 0

def uchu_main(GameAuto):
    while 1:
        print(">>>>>>>>> uchu >>>>>>")
        GameAuto.serch_click_image2('./img/uchu/start.png', 1, 0.8)
        GameAuto.serch_click_image2('./img/uchu/close.png', 1, 0.7)
        GameAuto.serch_click_image2('./img/uchu/close2.png', 1, 0.7)
        GameAuto.serch_click_image2('./img/uchu/close3.png', 1, 0.8)
        GameAuto.serch_click_image2('./img/uchu/retry.png', 1, 0.8)

        time.sleep(2)

#以下、メインルーチン
if __name__ == "__main__":
    
   

    GameAuto = GameAutomation.GameAutomation()   
    print("=========================")
    uchu_main(GameAuto)
    print("=========================")

        


