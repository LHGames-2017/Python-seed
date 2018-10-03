from structs import Point


class Tile:
    def __init__(self, tileType, x, y):
        self.TileType = tileType
        self.Position = Point(x, y)
        pass


class ResourceTile(Tile):
    def __init__(self, tileType, x, y, amountLeft, density):
        Tile.__init__(self, tileType, x, y)
        self.AmountLeft = amountLeft
        self.Density = density


class TileContent():
    Empty, Wall, House, Lava, Resource, Shop, Player = range(7)
