MORNING = 0
NIGHT = 1

class Game(object):
    def __init__(self, code):
        self.code = code
        self.day = 0
        self.turn = MORNING

