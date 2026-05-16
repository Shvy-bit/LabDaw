from ajedrez.interpreter import *
from ajedrez.chessPictures import *

fig1 = square.join(square.negative())
fig2 = fig1.horizontalRepeat(4)
fig3 = fig2.up(fig2.negative())
fig4 = fig3.verticalRepeat(2)

draw(fig4)