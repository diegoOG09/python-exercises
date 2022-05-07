category = input('Categoria de producto:')
wish = input('Deseo:')

if category == 'productos lacteos' and wish == 'granja':
    print('EcoFarm')

if category == 'productos lacteos' and wish != 'granja':
    print('Mi villa')

if category == 'pan' and wish == 'grano integral':
    print('Panaderia el Tio Nick')

if category == 'pan' and wish != 'grano integral':
    print('Fabrica de pan # 21')

