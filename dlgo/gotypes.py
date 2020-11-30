import enum
from collection import namedtuple

#Set your player to Player = Player.<color> then you can call Player.other to get the other color
class Player(enum.Enum):
  black = 1
  white = 2

  @property
  def other(self):
    return Player.black if self == Player.white else Player.white #Returns the value of the other player

#A namedtuple storing a point. Call neighbors to check for neighbors
class Point( namedtuple('Point', 'row col')):
    def neighbors(self):
        return [ 
            Point(self.row - 1, self.col),
            Point(self.row + 1, self.col),
            Point(self.row, self.col - 1),
            Point(self.row, self.col + 1)
        ]