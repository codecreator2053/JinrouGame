
class Role(object):
    def __init__(self):
        self.is_human = True
        
    def act_at_night(self):
        pass

class Citizen(Role):
    def __init__(self):
        super(Citizen, self).__init__()

