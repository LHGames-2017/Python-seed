from structs import Point
from tile import *


class GameMap:
    def __init__(self, serializedMap, xMin, yMin):
        self.xMin = xMin
        self.yMin = yMin
        self.deserializeMap(serializedMap)
        self.initMapSize()

    def getTileAt(self, position):
        if (position.x < self.xMin or position.x >= self.xMax or
                position.y < self.yMin or position.y >= self.yMax):
            return TileContent.Empty

        x = position.x - self.xMin
        y = position.y - self.yMin
        return self.tiles[x][y].TileType

    def initMapSize(self):
        if not self.tiles:
            self.xMax = self.xMin + len(self.tiles)
            self.yMax = self.yMin + len(self.tiles[0])
            self._visibleDistance = (self.xMax - self.xMin - 1) / 2

    def deserializeMap(self, serializedMap):
        serializedMap = serializedMap[1:-2]
        rows = serializedMap.split('[')
        column = rows[1].split('{')
        self.tiles = []
        for i in range(len(rows) - 1):
            self.tiles.append([])
            column = rows[i + 1].split('{')
            for j in range(len(column) - 1):
                tileType = TileContent.Empty
                if not column[j + 1][0] == '}':
                    infos = column[j + 1].split('}')
                    if len(infos) > 1:
                        infos = infos[0].split(',')
                    tileType = int(infos[0])
                    if tileType == TileContent.Resource:
                        amountLeft = int(infos[1])
                        density = int(infos[2])
                        self.tiles[i].append(ResourceTile(
                            tileType, i, j,
                            amountLeft, density
                        ))

                if tileType != TileContent.Resource:
                    self.tiles[i].append(
                        Tile(tileType, i + self.xMin, j + self.yMin))
