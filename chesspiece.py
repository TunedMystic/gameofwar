import abc


class ChessPiece(object):
  """
  A generic chess piece object.
  """
  
  __metaclass__ = abc.ABCMeta
  
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
