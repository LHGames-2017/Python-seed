import math


class ActionTypes():
    DefaultAction, MoveAction, MeleeAttackAction, CollectAction, UpgradeAction, StealAction, PurchaseAction, HealAction = \
        range(8)


class UpgradeType():
    CarryingCapacity, AttackPower, Defence, MaximumHealth, CollectingSpeed = range(
        5)


class TileType():
    Tile, Wall, House, Lava, Resource, Shop = range(6)


class PurchasableItem():
    Sword, Shield, Backpack, Pickaxe, HealthPotion = range(5)


class Point(object):

    # Constructor
    def __init__(self, X=0, Y=0):
        self.X = X
        self.Y = Y

    # Overloaded operators
    def __add__(self, point):
        return Point(self.X + point.X, self.Y + point.Y)

    def __sub__(self, point):
        return Point(self.X - point.X, self.Y - point.Y)

    def __str__(self):
        return "{{{0}, {1}}}".format(self.X, self.Y)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.X == other.X and self.Y == other.Y
        return NotImplemented

    # Distance between two Points
    @staticmethod
    def Distance(p1, p2):
        delta_x = p1.X - p2.X
        delta_y = p1.Y - p2.Y
        return math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2))


class GameInfo(object):

    def __init__(self, json_dict):
        self.__dict__ = json_dict
        self.HouseLocation = Point(json_dict["HouseLocation"])
        self.Map = None
        self.OtherPlayers = dict()


class ActionContent(object):

    def __init__(self, action_name, content):
        self.ActionName = action_name
        self.Content = str(content)
