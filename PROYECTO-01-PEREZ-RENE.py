from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
from collections import Counter

usuario = "Admin"
password = "EmTech"
print("\t\tBienvenido al sistema de reportes de LifeStore\n\n")
Validar_usuario = input("Usuario:")
Validar_contraseña = input("Contraseña:")
#Se valida usuario y contraseña mediante While en el que debem ser verdaderas dos condiciones para poder continuar
while Validar_usuario == "Admin" and Validar_contraseña == "EmTech":
  print("\n\nAccediendo a reportes...")
  print("\n\t\t\t\tMenu\n\n1- Reporte de Ventas\n\n2- Reseña de servicio\n\n3- Total de ingresos y ventas promedio\n")
  opcion = int(input("Seleccione una opción:"))#Menu principal
  if opcion == 1:
    print("\nReporte de Ventas")
    #Ventas
    Mayores_ventas = []
    for productos in lifestore_sales:
      if productos[-1] == 0:#No se toman en cuenta las devoluciones
        id_producto = productos[1]
      #print(id_producto)_Validar que se tomó la columna adecuada de la lista
      conver = str(id_producto)
      Mayores_ventas.append(id_producto)
    ordenar = Counter(Mayores_ventas)
    #print(ordenar)_Se ordenan los valores de mayor a menor con Counter
    cuantos = int(input('\nIndique el Top # de productos a visualizar:\t'))
    print(f"Los {cuantos} productos con mayores ventas son: \n",ordenar.most_common(cuantos))
    #Búsquedas
    Mayores_busquedas = []
    for products in lifestore_searches:
      id_ = products[1]
      #print(id_)_Validar que se tomó la columna adecuada de la lista
      conver = str(id_)
      Mayores_busquedas.append(id_)
    orden = Counter(Mayores_busquedas)
    #print(orden)_Se ordenan los valores de mayor a menor con Counter
    Cuantos = int(input('\n\n\nIndique el Top # de productos a visualizar:\t'))
    print(f"Los {Cuantos} productos con mayores búsquedas son: \n",orden.most_common(Cuantos))
    continue
    
  elif opcion == 2:
    print("Reseña de servicio")
    #Reseñas
    mejores_rñs = []

    for prod in lifestore_sales:
      score = prod[1],prod[2]#accedemos a una parte especidfica de la lista
      #print(score)_Validar que se tomó la columna adecuada de la lista
      convertir_lista = str(score)
      mejores_rñs.append(score)#Se transforma y se guarda
      ordenar = Counter(mejores_rñs)
    #print(ordenar)_Se ordenan los valores de mayor a menor con Counter
    cuantos = int(input('Indique el Top # de productos a  visualizar:\t'))
    print('\n')
    num = cuantos
    print(f"Los {cuantos} productos con las mejores reseñas (*****)   son:\n\n",ordenar.most_common(cuantos))

    #Peores Reseñas
    print('\n')
    print(f"Los {cuantos} productos con las peores reseñas (*)        son:\n\n",ordenar.most_common()[-num:])#obtenemos los ultimos datos de la lista ordenanda
    continue
  elif opcion == 3:
    print("Total de ingresos y ventas promedio")
    ventas = []
    cantidad_de_productos = len(lifestore_products)
#guardamos en una lista con dos espacios el total de articulos y las veces que se repiten
    for id in range(cantidad_de_productos):
      verdadero_id = id + 1
      renglon = [verdadero_id, 0]
      ventas.append(renglon)

    for venta in lifestore_sales:
      id_producto = venta[1]
      ventas[id_producto - 1][1] = ventas[id_producto - 1][1] + 1
    print('\n\n')
    print("Cantidad de Ventas por Id")
    print(ventas)
    print("\n\n")


    costo = []
    for productes in lifestore_products:
      id_prices = productes[0],productes[2]
      costo.append(id_prices)
    print("Costo de los productos")
    print(costo)
    print('\n\n')
  #categoras mediante menu con sentencia if-elif-else
    print("\n\t\t\t\t\t\tMenú por categorías\n\n1- Procesadores\n\n2- Tarjetas de video\n\n3- Tarjetas madre\n\n4- Discos duros\n\n5- Memorias USB\n\n6-Pantallas\n\n7- Bocinas\n\n8- Audífonos")
    opt = int(input("\n\nSeleccione una opción:"))

    if opt == 1:
      print("\n\t\t\t\tProcesadores:\n")
      cat = []
      for prod in lifestore_products:#obtenemos la parte de interes de la lista
        category = prod[3]
      if category == "procesadores":
        cat.append(prod)
      for produ in cat:
        print(produ)#ID del producto , Nombre del mismo

      ventas = []
      cantidad_de_productos = len(lifestore_products)
#se guarda para el conteo de totales
      for id in range(cantidad_de_productos):
        verdadero_id = id + 1
        renglon = [verdadero_id, 0]
        ventas.append(renglon)

      for venta in lifestore_sales:
        id_producto = venta[1]
        ventas[id_producto - 1][1] = ventas[id_producto - 1][1] + 1
      print('\n\n')
      print("Menores Ventas")
      print(ventas[0:9])  
      print("\nMenores Búsquedas")
      busquedas = []
      cantidad = len(lifestore_products)

      for id in range(cantidad):
        verdadero_id = id + 1
        renglon = [verdadero_id, 0]
        busquedas.append(renglon)

      for busqueda in lifestore_searches:
        id_producto = busqueda[1]
        busquedas[id_producto - 1][1] = busquedas[id_producto - 1][1] + 1
      print(busquedas[0:9])
    elif opt == 2:
      print("\n\t\t\t\tTarjetas de video:\n")
      cat = []
      for prod in lifestore_products:
        category = prod[3]
        if category == "tarjetas de video":
          cat.append(prod)
      for produ in cat:
        print(produ)#ID del producto , Nombre del mismo
        prod_ventas = []
      cantidad_de_productos = len(lifestore_products)

      for id in range(cantidad_de_productos):
        verdadero_id = id + 1
        renglon = [verdadero_id, 0]
        prod_ventas.append(renglon)

      for venta in lifestore_sales:
        id_producto = venta[1]
        prod_ventas[id_producto - 1][1] = prod_ventas[id_producto - 1][1] + 1
      print('\n\n')
      print("Menores Ventas")
      print(prod_ventas[9:28])
      print("\nMenores Búsquedas")
      busquedas = []
      cantidad = len(lifestore_products)

      for id in range(cantidad):
        verdadero_id = id + 1
        renglon = [verdadero_id, 0]
        busquedas.append(renglon)

      for busqueda in lifestore_searches:
        id_producto = busqueda[1]
        busquedas[id_producto - 1][1] = busquedas[id_producto - 1][1] + 1
      print(busquedas[9:28])
    elif opt == 3:
      print("\n\t\t\t\tTarjetas madre:\n")
      cat = []
      for prod in lifestore_products:
        category = prod[3]
        if category == "tarjetas madre":
          cat.append(prod)
      for produ in cat:
        print(produ)#ID del producto , Nombre del mismo
        prod_ventas = []
      cantidad_de_productos = len(lifestore_products)

      for id in range(cantidad_de_productos):
        verdadero_id = id + 1
        renglon = [verdadero_id, 0]
        prod_ventas.append(renglon)

      for venta in lifestore_sales:
        id_producto = venta[1]
        prod_ventas[id_producto - 1][1] = prod_ventas[id_producto - 1][1] + 1
      print('\n\n')
      print("Menores Ventas")
      print(prod_ventas[28:46])
      print("\nMenores Búsquedas")
      busquedas = []
      cantidad = len(lifestore_products)

      for id in range(cantidad):
        verdadero_id = id + 1
        renglon = [verdadero_id, 0]
        busquedas.append(renglon)

      for busqueda in lifestore_searches:
        id_producto = busqueda[1]
        busquedas[id_producto - 1][1] = busquedas[id_producto - 1][1] + 1
      print(busquedas[28:46])
    elif opt == 4:
      print("\n\t\t\t\tDiscos duros:\n")
      cat = []
      for prod in lifestore_products:
        category = prod[3]
        if category == "discos duros":
          cat.append(prod)
      for produ in cat:
        print(produ)#ID del producto , Nombre del mismo
        prod_ventas = []
      cantidad_de_productos = len(lifestore_products)

      for id in range(cantidad_de_productos):
        verdadero_id = id + 1
        renglon = [verdadero_id, 0]
        prod_ventas.append(renglon)

      for venta in lifestore_sales:
        id_producto = venta[1]
        prod_ventas[id_producto - 1][1] = prod_ventas[id_producto - 1][1] + 1
      print('\n\n')
      print("Menores Ventas")
      print(prod_ventas[46:59])
      print("\nMenores Búsquedas")
      busquedas = []
      cantidad = len(lifestore_products)

      for id in range(cantidad):
        verdadero_id = id + 1
        renglon = [verdadero_id, 0]
        busquedas.append(renglon)

      for busqueda in lifestore_searches:
        id_producto = busqueda[1]
        busquedas[id_producto - 1][1] = busquedas[id_producto - 1][1] + 1
      print(busquedas[46:59])

    elif opt == 5:
      print("\n\t\t\t\tMemorias USB:\n")
      cat = []
      for prod in lifestore_products:
        category = prod[3]
        if category == "memorias usb":
          cat.append(prod)
      for produ in cat:
        print(produ)#ID del producto , Nombre del mismo
        prod_ventas = []
        cantidad_de_productos = len(lifestore_products)

      for id in range(cantidad_de_productos):
        verdadero_id = id + 1
        renglon = [verdadero_id, 0]
        prod_ventas.append(renglon)

      for venta in lifestore_sales:
        id_producto = venta[1]
        prod_ventas[id_producto - 1][1] = prod_ventas[id_producto - 1][1] + 1
      print('\n\n')
      print("Menores Ventas")
      print(prod_ventas[59:61])
      print("\nMenores Búsquedas")
      busquedas = []
      cantidad = len(lifestore_products)

      for id in range(cantidad):
        verdadero_id = id + 1
        renglon = [verdadero_id, 0]
        busquedas.append(renglon)

      for busqueda in lifestore_searches:
        id_producto = busqueda[1]
        busquedas[id_producto - 1][1] = busquedas[id_producto - 1][1] + 1
      print(busquedas[59:61])

    elif opt == 6:
      print("\n\t\t\t\tPantallas:\n")
      cat = []
      for prod in lifestore_products:
        category = prod[3]
        if category == "pantallas":
          cat.append(prod)
      for produ in cat:
        print(produ)#ID del producto , Nombre del mismo
        prod_ventas = []
      cantidad_de_productos = len(lifestore_products)

      for id in range(cantidad_de_productos):
        verdadero_id = id + 1
        renglon = [verdadero_id, 0]
        prod_ventas.append(renglon)

      for venta in lifestore_sales:
        id_producto = venta[1]
        prod_ventas[id_producto - 1][1] = prod_ventas[id_producto - 1][1] + 1
      print('\n\n')
      print("Menores Ventas")
      print(prod_ventas[61:73])
      print("\nMenores Búsquedas")
      busquedas = []
      cantidad = len(lifestore_products)

      for id in range(cantidad):
        verdadero_id = id + 1
        renglon = [verdadero_id, 0]
        busquedas.append(renglon)

      for busqueda in lifestore_searches:
        id_producto = busqueda[1]
        busquedas[id_producto - 1][1] = busquedas[id_producto - 1][1] + 1
      print(busquedas[61:73])
    elif opt == 7:
      print("\n\t\t\t\tBocinas:\n")#Que truenen
      cat = []
      for prod in lifestore_products:
        category = prod[3]
        if category == "bocinas":
          cat.append(prod)
      for produ in cat:
        print(produ)#ID del producto , Nombre del mismo
        prod_ventas = []
      cantidad_de_productos = len(lifestore_products)

      for id in range(cantidad_de_productos):
        verdadero_id = id + 1
        renglon = [verdadero_id, 0]
        prod_ventas.append(renglon)

      for venta in lifestore_sales:
        id_producto = venta[1]
        prod_ventas[id_producto - 1][1] = prod_ventas[id_producto - 1][1] + 1
      print('\n\n')
      print("Menores Ventas")
      print(prod_ventas[73:83])
      print("\nMenores Búsquedas")
      busquedas = []
      cantidad = len(lifestore_products)

      for id in range(cantidad):
        verdadero_id = id + 1
        renglon = [verdadero_id, 0]
        busquedas.append(renglon)

      for busqueda in lifestore_searches:
        id_producto = busqueda[1]
        busquedas[id_producto - 1][1] = busquedas[id_producto - 1][1] + 1
      print(busquedas[73:83])
    elif opt == 8:
      print("\n\t\t\t\tAudifonos:\n")
      cat = []
      for prod in lifestore_products:
        category = prod[3]
        if category == "audifonos":
          cat.append(prod)
      for produ in cat:
        print(produ)#ID del producto , Nombre del mismo
        prod_ventas = []
      cantidad_de_productos = len(lifestore_products)

      for id in range(cantidad_de_productos):
        verdadero_id = id + 1
        renglon = [verdadero_id, 0]
        prod_ventas.append(renglon)

      for venta in lifestore_sales:
        id_producto = venta[1]
        prod_ventas[id_producto - 1][1] = prod_ventas[id_producto - 1][1] + 1
      print('\n\n')
      print("Menores Ventas")
      print(prod_ventas[83:96])
      print("\nMenores Búsquedas")
      busquedas = []
      cantidad = len(lifestore_products)

      for id in range(cantidad):
        verdadero_id = id + 1
        renglon = [verdadero_id, 0]
        busquedas.append(renglon)

      for busqueda in lifestore_searches:
        id_producto = busqueda[1]
        busquedas[id_producto - 1][1] = busquedas[id_producto - 1][1] + 1
      print(busquedas[83:96])#mediante slicing se obtiene la parte de interes de la lista
    else:
      print("\nOpción Incorrecta") 
    continue
  else: 
    print("Opción incorrecta, Intente nuevamente")
  continue
else:
  print("\n\n\nUsuario incorrecto......Adiós!")
      