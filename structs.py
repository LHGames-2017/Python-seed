class ActionTypes():
    DefaultAction, MoveAction, AttackAction, CollectAction,
        UpgradeAction, StealAction, PurchaseAction = range(7)

class UpgradeType():
    CarryingCapacity, AttackPower, Defence, MaximumHealth,
        CollectingSpeed = range(5)
class TileType():
    Tile, Wall, House, Lava, Resource, Shop = range(6)

class TileContent():
    Empty, Resource, House, Player, Wall, Lava, Shop = range(7)

class Point(object):

    # Constructor
    def __init__(self, X=0, Y=0):
        self.X = X
        sellf.Y = Y

    # Overloaded operators
    def __add__(self, point):
        return Point(self.X + point.X, self.Y + point.Y)

    def __sub__(self, point):
        return Point(self.X - point.X, self.Y - point.Y)

    def __str__(self):
        return "{{{0}, {1}}}".format(self.X, self.Y)

    # Distance between two Points
    def Distance(p1, p2):
        delta_x = p1.X - p2.X
        delta_y = p1.Y - p2.Y
        return math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2))

class GameInfo(object):

    def __init__(self, json_dict):
        self.__dict__ = json_dict
        self.HouseLocation = Point(json_dict["HouseLocation"])
        self.Map = Tile(json_dict["Map"])
        self.Players = dict()

class Tile(object):

    def __init__(self, content, x, y):
        self.Content = content
        self.X = x
        self.Y = y

class PlayerInfo(object):

    def __init__(self, health, position, houseLocation, carriedRessources,
                 carryingCapacity=1000):
        self.Health = health
        self.Position = position
        self.HouseLocation = houseLocation
        self.CarriedRessources = carriedRessources
        self.CarryingCapacity = carryingCapacity
