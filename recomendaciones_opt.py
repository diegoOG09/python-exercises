category = input('Categoria de producto:')
wish = input('Deseo:')

if category == 'productos lacteos':
    if wish == 'granja':
        print('EcoFarm')
    else:
        print('Mi villa')

if category == 'pan':
    if wish == 'grano integral':
        print('Panaderia el Tio Nick')
    else:
        print('Fabrica de pan # 21')
