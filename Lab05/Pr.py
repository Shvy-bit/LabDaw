from ajedrez.interpreter import *
from ajedrez.chessPictures import *
from ajedrez.colors import *

#from ajedrez.picture import *

pieces = king.negative().square().join(square)

draw(pieces)

#a = Picture(["aña ","ene ","oo "])
#u = Picture(["K"])
#b= Picture(["Array ","izi ","uu "])
#c = Picture(["ang ", "oztia ", "waza "])
#out = u.verticalRepeat(3)
#for i in range(len(out.img)):
#    print(out.img[i])
