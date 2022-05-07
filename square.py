class Square():

  def area(side):
    return side*side

figure = Square()
side_length = int(input("Ingresa la longitud del lado del cuadrado: "))
print(figure.area(side_length))
