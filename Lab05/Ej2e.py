from ajedrez.interpreter import *
from ajedrez.chessPictures import *

fig1 = square.negative().join(square)
fig2 = fig1.horizontalRepeat(4)
draw(fig2)