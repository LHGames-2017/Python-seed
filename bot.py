from aiHelper import *
from structs import *


class Bot:
    def __init__(self):
        pass

    def before_turn(self, playerInfo):
        self.PlayerInfo = playerInfo

    def execute_turn(self, map, otherPlayers):
        return create_move_action(Point(1, 0))

    def after_turn(self):
        pass
