from ajedrez.interpreter import *
from ajedrez.chessPictures import *

fig1 = knight.join(knight.negative())
fig2 = fig1.negative()
draw(fig1.up(fig2))