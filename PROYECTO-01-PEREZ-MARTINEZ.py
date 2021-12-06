from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
from collections import Counter

usuario = "Admin"
password = "EmTech"
print("\t\tBienvenido al sistema de reportes de LifeStore\n\n")
Validar_usuario = input("Usuario:")
Validar_contraseña = input("Contraseña:")

while Validar_usuario == "Admin" and Validar_contraseña == "EmTech":
  print("\n\nAccediendo a reportes...")
  print("\n\t\t\t\tMenu\n\n1- Reporte de Ventas\n\n2- Reseña de servicio\n\n3- Total de ingresos y ventas promedio\n")
  opcion = int(input("Seleccione una opción:"))
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
      score = prod[1],prod[2]
      #print(score)_Validar que se tomó la columna adecuada de la lista
      convertir_lista = str(score)
      mejores_rñs.append(score)
      ordenar = Counter(mejores_rñs)
    #print(ordenar)_Se ordenan los valores de mayor a menor con Counter
    cuantos = int(input('Indique el Top # de productos a  visualizar:\t'))
    print('\n')
    num = cuantos
    print(f"Los {cuantos} productos con las mejores reseñas (*****)   son:\n\n",ordenar.most_common(cuantos))

    #Peores Reseñas
    print('\n')
    print(f"Los {cuantos} productos con las peores reseñas (*)        son:\n\n",ordenar.most_common()[-num:])
    continue
  elif opcion == 3:
    print("Total de ingresos y ventas promedio")
    ventas = []
    cantidad_de_productos = len(lifestore_products)

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
    
    continue
  else: 
    print("Opción incorrecta, Intente nuevamente")
    continue
  #break
  break
else:
  
  print("\n\n\nUsuario incorrecto......Adiós!")
      
