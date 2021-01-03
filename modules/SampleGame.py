

from GameAutomation import GameAutomation

class SampleGame(GameAutomation):
    def __init__(self):
        super(SampleGame, self).__init__()
        self.function = "SampleGame"

    def sample(self):
        print(self.function)

if __name__ == "__main__":
    
    OBJ = SampleGame()
    OBJ.sample()