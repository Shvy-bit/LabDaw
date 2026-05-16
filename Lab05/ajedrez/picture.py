from ajedrez.colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
      vertical.append(value[::-1])
    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    horizontal = self.img[::-1]
    return Picture(horizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negative = []
    for linea in self.img:
      negative.append(''.join([self._invColor(color) for color in linea]))
    return Picture(negative)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento
        al lado derecho de la figura actual """
    joined = []
    for i in range(len(p.img)):
      if i < len(self.img):
        joined.append(self.img[i] + p.img[i])
      else:
        joined.append(p.img[i])
    return Picture(joined)

  def up(self, p):
    """ Devuelve una nueva figura poniendo la figura actual sobre la
        figura p """
    new = self.img
    for i in range(len(p.img)):
      new.append(p.img[i])
    return Picture(new)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    new = p.img
    for i in range(len(self.img)):
      new.append(self.img[i])
    return Picture(new)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    hRepeat = self
    for i in range(n - 1):
      hRepeat = hRepeat.join(self)
    #Solo retorna hRepeat dado que join devuelve una Picture de por si
    return hRepeat

  def verticalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual hacia abajo
        la cantidad de veces que indique el valor de n """
    vRepeat = self.img[:]
    for i in range(n - 1):
      for j in range(len(self.img)):
        vRepeat.append(self.img[j])
    return Picture(vRepeat)
  
  def square(self):
    """Devuelve una figura sobrepuesta en un cuadro"""
    new = []
    for linea in self.img:
      new.append(linea.replace(' ', '_'))
    return Picture(new)

  def squareN(self):
    new = []
    for linea in self.img:
      new.append(linea.replace(' ', '='))
    return Picture(new)
  
  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

