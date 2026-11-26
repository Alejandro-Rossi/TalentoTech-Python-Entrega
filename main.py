import database as db
from validaciones import (
    pedir_entero,
    pedir_flotante,
    pedir_entero_opcional,
    pedir_texto_obligatorio,
)


def vista_crear():
    print("\n--- Agregar Nuevo Producto ---")
    marca = pedir_texto_obligatorio("Marca (ej. Kingston, Asus): ")
    modelo = pedir_texto_obligatorio("Modelo (ej. FURY DDR5 32GB): ")
    tipo = pedir_texto_obligatorio("Tipo (ej. Memoria RAM, Monitor): ")
    precio = pedir_entero("Precio en pesos (con o sin decimales): ")

    if db.insertar_producto(marca, modelo, tipo, precio):
        print(f"✅ ¡El producto '{marca} {modelo}' se guardó con éxito!")


def vista_mostrar():
    print("\n--- Stock Actual de Productos ---")
    productos = db.obtener_todos()
    if not productos:
        print("No hay productos registrados actualmente.")
        return False

    for p in productos:
        print(f"ID: {p[0]} | {p[1]} {p[2]} | Tipo: {p[3]} | Precio: ${p[4]}")
    return True


def vista_buscar():
    print("\n--- Buscar Producto ---")
    termino = pedir_texto_obligatorio("Ingrese marca o modelo a buscar: ")
    resultados = db.buscar_productos(termino)

    if not resultados:
        print("❌ No se encontraron coincidencias.")
    else:
        for p in resultados:
            print(f"✅ ID: {p[0]} -> {p[1]} {p[2]} | Tipo: {p[3]} | Precio: ${p[4]}")


def vista_actualizar():
    print("\n--- Actualizar Producto ---")
    if not vista_mostrar():
        return

    id_producto = pedir_entero("\nIngrese el ID del producto a actualizar: ")
    producto = db.obtener_por_id(id_producto)

    if not producto:
        print("❌ No existe ningún producto con ese ID.")
        return

    print(f"\nEditando ID {producto[0]}: {producto[1]} {producto[2]} (${producto[4]})")
    print("(Presione ENTER sin escribir nada para mantener el valor actual)")

    marca = input(f"Nueva marca [{producto[1]}]: ").strip() or producto[1]
    modelo = input(f"Nuevo modelo [{producto[2]}]: ").strip() or producto[2]
    tipo = input(f"Nuevo tipo [{producto[3]}]: ").strip() or producto[3]
    precio = pedir_entero_opcional(f"Nuevo precio [{producto[4]}]: ", producto[4])

    if db.actualizar_producto(id_producto, marca, modelo, tipo, precio):
        print(f"✅ ¡Producto ID {id_producto} actualizado correctamente!")


def vista_eliminar():
    print("\n--- Eliminar Producto ---")
    if not vista_mostrar():
        return

    id_producto = pedir_entero("\nIngrese el ID del producto a eliminar: ")
    producto = db.obtener_por_id(id_producto)

    if not producto:
        print("❌ No existe ningún producto con ese ID.")
        return

    if db.eliminar_producto(id_producto):
        print(f"🗑️ El artículo '{producto[1]} {producto[2]}' fue eliminado.")


def menu_principal():
    db.inicializar_db()

    while True:
        try:
            print("\n========================================")
            print("   Sistema de Stock - Computación")
            print("========================================")
            print("1. Agregar producto")
            print("2. Mostrar productos(Todos)")
            print("3. Buscar producto(Específico)")
            print("4. Actualizar producto")
            print("5. Eliminar producto")
            print("6. Salir")
            print("========================================")

            opcion = input("Seleccione una opción (1-6): ").strip()

            if opcion == "1":
                vista_crear()
            elif opcion == "2":
                vista_mostrar()
            elif opcion == "3":
                vista_buscar()
            elif opcion == "4":
                vista_actualizar()
            elif opcion == "5":
                vista_eliminar()
            elif opcion == "6":
                print("\n¡Saliendo del sistema. Hasta luego!")
                break
            else:
                print("❌ Opción no válida. Elija un número entre 1 y 6.")

        except (KeyboardInterrupt, EOFError):
            print("\n\n⚠️ Interrupción detectada. Cerrando de forma segura...")
            break


if __name__ == "__main__":
    menu_principal()