from ajedrez.interpreter import *
from ajedrez.chessPictures import *

a1 = rock.squareN()
b1 = knight.square()
c1 = bishop.squareN()
d1 = queen.square()
e1 = king.squareN()
f1 = bishop.square()
g1 = knight.squareN()
h1 = rock.square()

fila1 = a1.join(
    b1.join(
        c1.join(
            d1.join(
                e1.join(
                    f1.join(
                        g1.join(
                            h1
                        )
                    )
                )
            )
        )
    )
)

fila2 = pawn.square().join(pawn.squareN()).horizontalRepeat(4)

fila4 = square.join(square.negative()).horizontalRepeat(4)
fila3_4 =fila4.up(fila4.negative())

fig1 = fila3_4.up(fila2.up(fila1))
fig2 = fig1.horizontalMirror().negative()

draw(fig2.up(fig1))