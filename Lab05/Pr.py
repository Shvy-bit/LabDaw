from ajedrez.interpreter import *
import ajedrez.chessPictures as piece
from ajedrez.colors import *

#from ajedrez.picture import *

pieces = piece.king.up(piece.queen.negative())
draw(pieces)

#a = Picture(["aña","ene","oo"])
#b= Picture(["kyara","izi","uu"])
#c = a.up(b)
#for i in range(len(c.img)):
#    print(c.img[i])