from Orm import ORM

dialectoSQLITE = 'sqlite:///'
orm = ORM('InventarioTabla', dialectoSQLITE)
i = 2
while i > 0:
    x= int(input('Elije una opcion: 1 - agregar 2 - eliminar 3 - buscar 4 - actualizar '))
    if x == 1:
        nombre = str(input('nombre del item - '))
        precio = int(input('precio del item - '))
        orm.addItem(nombre, precio)

    if x == 2:
        nombre = str(input('nombre del item - '))
        orm.editarItem(nombre)

    if x == 3:
        nombre = str(input('nombre del item - '))
        orm.borrarItem(nombre)

    if x == 4:
        nombre = str(input('nombre del item - '))
        precio = int(input('precio del item - '))
        orm.editarItem(nombre, precio)

    print('listo')
    isActive = int(input('precina 1 para salir '))

    if isActive == 1:
        i = isActive

