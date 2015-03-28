import abc


class ChessPiece(object):
  """
  A generic chess piece object.
  """
  
  __metaclass__ = abc.ABCMeta
  name = "Base Piece"
  
  # (x, y)
  current_position = None
  
  def __init__(self, position=()):
    self.current_position = position
  
  @abc.abstractmethod
  def is_valid(self, row, col):
    """
    Receive a new position and determine if it is
    a valid move for this chess piece.
    """
    pass


class Pawn(object):
  name = "Pawn"
  
  def is_valid(self, row, col):
    if self.current_position[0] == (row, col):
      return False
    if row < self.current_position[0]:
      return True
    else:
      return False


class RookMixin(object):
  
  def is_valid(self, row, col):
    if self.current_position == (row, col):
      return False
    if self.current_position[0] == row or self.current_position[1] == col:
      return True
    else:
      return False


class Rook(RookMixin, ChessPiece):
  name = "Rook"


class Knight(ChessPiece):
  name = "Knight"
  
  def is_valid(self, row, col):
    if self.current_position == (row, col):
      return False
    if (self.current_position[0] + 2) == row or (self.current_position[0] - 2) == row:
      if (self.current_position[1] + 1) == col or (self.current_position[1] - 1) == col:
        return True
    if (self.current_position[1] + 2) == col or (self.current_position[1] - 2) == col:
      if (self.current_position[0] + 1) == row or (self.current_position[0] - 1) == row:
        return True
    else:
      return False