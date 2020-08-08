
class Role(object):
    def __init__(self):
        self.is_human = True
        
    def act_at_night(self):
        pass

class Citizen(Role):
    def __init__(self):
        super(Citizen, self).__init__()

    def act_at_night(self):
        return None


class Prophet(Role):
    def __init__(self):
        super(Prophet, self).__init__()

    def act_at_night(self):
        pass


class Werewolf(Role):
    def __init(self):
        super(Werewolf, self).__init__()


