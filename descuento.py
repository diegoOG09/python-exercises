categoria = input('Introduce la categoría:')

while categoria != 'cancelar':
  precio = float(input('Introduce el precio del producto:'))

  if categoria == 'productos horneados':
    print('Descuento de 30%. Por pagar:',precio - (precio*.30))
  elif categoria == 'productos lacteos':
    print('Descuento de 10%. Por pagar:',precio - (precio*.10))
  else:
    print('No hay descuento. Por pagar:',precio)

  categoria = input('Introduce la categoría:')
print('Compra cerrada')