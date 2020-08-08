import random

from user import User

MORNING = 0
NIGHT = 1

class Game(object):
    """Game object

    Has property and methods to control game.
    """

    def __init__(self, code):
        self.code = code
        self.day = 0
        self.turn = MORNING
        self.users = {}
        self.roles = []
        self.num_werewolf = 0

    def add_user(self, username):
        """Add user to users property

        Args:
            username (str): username
        """

        user = User(username)
        self.users[username] = user

    def generate_role(self, num_members):
        """Generate roles

        Generate roles according to the number of users

        Args:
            num_members: number of users
        """

        pass

    def allocate_role_to_users(self):
        """Allocate roles to users

        Allocate roles to users. This method has to be done after add_user and generate_role.
        """

        shuffled_roles = random.sample(self.roles, len(self.roles))

        for u, r in zip(self.users.values(), self.roles):
            u.role = r
            self.num_werewolf += int(not r.is_human)

    def check_finish(self):
        """Check is_finish

        Check the game is finished. This method has to be called in the morning and after voting.
        """

        num_alive_human = 0
        for u in self.users.values():
            num_alive_human += int(u.is_alive and u.role.is_human)

        return num_alive_human <= self.num_werewolf

    def kill_selected_user(self, username):
        """Kill selected user

        Kill selected user. User selected must be alive. If the user is already killed, raise assertion error.
        """
        assert username in self.users, "Not found user %s" % username
        assert self.users[username].is_alive, "User %s is already killed." % username

        self.users[username].is_alive = False



