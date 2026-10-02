# Lista principal para almacenar el stock de computación
# Cada elemento es una sublista con: [marca, modelo, tipo, precio (en pesos argentinos)]
stock_computacion = []

# Ciclo principal para mantener el menú abierto

while True:
    print("\n========================================")
    print("   Sistema de Stock - Artículos de Computación")
    print("========================================")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("========================================")
    
    opcion = input("Seleccione una opción (1-5): ")
    
    # OPCIÓN 1: Agregar producto (4 elementos)

    if opcion == "1":
        print("\n--- Agregar Nuevo Producto ---")
        marca = input("Ingrese la marca (ej. Kingston, HyperX, Asus, etc): ")
        modelo = input("Ingrese el modelo (ej. Modelo comercial (FURY DDR5 32GB), SKU o PN): ")
        tipo = input("Ingrese el tipo de producto (ej. Memoria RAM, Teclado, Monitor, etc): ")
        
        # Se convierte directamente a entero (precio sin centavos)
        precio = int(input("Ingrese el precio en pesos (sin centavos): "))
        
        # Creamos la sublista con los 4 datos y la guardamos en la lista principal
        producto_nuevo = [marca, modelo, tipo, precio]
        stock_computacion.append(producto_nuevo)
        print(f"¡El producto '{marca} {modelo}' se agregó al stock con éxito!")

    # OPCIÓN 2: Mostrar productos

    elif opcion == "2":
        print("\n--- Stock Actual de Productos ---")
        if len(stock_computacion) == 0:
            print("No hay productos registrados en el stock actualmente.")
        else:
            for i in range(len(stock_computacion)):
                p = stock_computacion[i]
                # p[0]=marca, p[1]=modelo, p[2]=tipo, p[3]=precio
                print(f"{i + 1}. {p[0]} {p[1]} | Tipo: {p[2]} | Precio: ${p[3]}")

    # OPCIÓN 3: Buscar producto (Buscando por marca o modelo)

    elif opcion == "3":
        print("\n--- Buscar Producto en el Stock ---")
        if len(stock_computacion) == 0:
            print("El stock está vacío, no hay nada que buscar.")
        else:
            busqueda = input("Ingrese la marca o modelo a buscar: ")
            encontrado = False
            
            for p in stock_computacion:
                # Buscamos si coincide con la marca (p[0]) o con el modelo (p[1])
                if p[0] == busqueda or p[1] == busqueda:
                    print(f"✅ ¡Encontrado! -> Marca: {p[0]} | Modelo: {p[1]} | Tipo: {p[2]} | Precio: ${p[3]}")
                    encontrado = True
                    break
            
            if not encontrado:
                print("❌ No se encontró ningún artículo con esa marca o modelo.")

    # OPCIÓN 4: Eliminar producto

    elif opcion == "4":
        print("\n--- Eliminar Producto del Stock ---")
        if len(stock_computacion) == 0:
            print("No hay productos para eliminar.")
        else:
            # Mostramos la lista numerada para que el usuario elija
            for i in range(len(stock_computacion)):
                p = stock_computacion[i]
                print(f"{i + 1}. {p[0]} {p[1]} ({p[2]}) - ${p[3]}")
            
            eliminacion = int(input("Ingrese el número del producto que desea eliminar: "))
            
            # Validamos que el número esté dentro de los límites de la lista
            if eliminacion >= 1 and eliminacion <= len(stock_computacion):
                producto_eliminado = stock_computacion.pop(eliminacion - 1)
                print(f"🗑️ El artículo '{producto_eliminado[0]} {producto_eliminado[1]}' fue eliminado del stock.")
            else:
                print("❌ Número de producto inválido.")

    # OPCIÓN 5: Salir

    elif opcion == "5":
        print("\n¡Saliendo del sistema de stock de computación. Hasta luego!")
        break

    # Opción no válida

    else:
        print("❌ Opción no válida. Por favor, elija un número entre 1 y 5.")