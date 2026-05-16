from ajedrez.interpreter import *
import ajedrez.chessPictures as piece
from ajedrez.colors import *

pieces = piece.king.join(piece.queen.negative())
draw(pieces)