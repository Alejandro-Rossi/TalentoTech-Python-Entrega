# Sistema de Gestión de Stock - Artículos de Computación

Aplicación de consola desarrollada en **Python** para la administración de inventario de artículos de computación, implementando un **CRUD** completo (*Crear, Leer, Actualizar y Eliminar*) con almacenamiento persistente mediante **SQLite3**.

---

## Características Principales

* **Persistencia de datos con SQLite3:** Creación automática de la base de datos `stock_computacion.db` y su tabla `productos` al iniciar el sistema.
* **Operaciones CRUD completas:**
  * **Crear (`INSERT`):** Registro de nuevos productos con marca, modelo, tipo y precio con decimales (`REAL`).
  * **Consultar todos (`SELECT`):** Visualización completa del inventario ordenado por su identificador único (`ID`).
  * **Buscar (`SELECT ... LIKE`):** Búsqueda flexible por coincidencias parciales en marca o modelo, insensible a mayúsculas y minúsculas.
  * **Actualizar (`UPDATE`):** Edición selectiva de cualquier campo de un producto mediante su `ID`, permitiendo presionar `ENTER` para conservar los valores actuales.
  * **Eliminar (`DELETE`):** Borrado seguro de productos verificando previamente la existencia del `ID`.
* **Validación de entradas y manejo de excepciones:** Control mediante bloques `try / except / finally` para evitar cierres inesperados por errores de tipeo (`ValueError`), fallos de base de datos (`sqlite3.Error`) o interrupciones de teclado (`KeyboardInterrupt`).
* **Arquitectura modular:** Código separado en capas de presentación, lógica de datos y utilidades de validación.

---

## Estructura del Proyecto

```text
proyecto_stock/
│
├── main.py                # Punto de entrada: menú principal e interfaz de consola
├── database.py            # Capa de datos: conexión SQLite3 y consultas SQL (CRUD)
├── validaciones.py        # Utilidades: validación de textos, enteros y precios decimales
├── stock_computacion.db   # Base de datos SQLite (generada automáticamente)
└── README.md              # Documentación del proyecto
```

---

## Modelo de Datos

El sistema utiliza una tabla llamada `productos` dentro de `stock_computacion.db` con la siguiente estructura:

| Columna | Tipo SQLite | Restricciones | Descripción |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PRIMARY KEY AUTOINCREMENT` | Identificador único del producto |
| `marca` | `TEXT` | `NOT NULL` | Fabricante o marca (ej. Kingston, Asus) |
| `modelo` | `TEXT` | `NOT NULL` | Modelo comercial, SKU o Part Number |
| `tipo` | `TEXT` | `NOT NULL` | Categoría (ej. Memoria RAM, Monitor, Teclado) |
| `precio` | `REAL` | `NOT NULL` | Precio unitario con decimales sin redondear |

---

## Requisitos e Instalación

* **Python 3.8 o superior** (no requiere instalación de librerías externas, ya que `sqlite3` y `math` forman parte de la biblioteca estándar de Python).

### Ejecución

1. Clonar o descargar los archivos en una misma carpeta (`main.py`, `database.py` y `validaciones.py`).
2. Abrir una terminal en el directorio del proyecto.
3. Ejecutar el archivo principal:

```bash
python main.py
```

*(En sistemas Linux o macOS puede requerirse `python3 main.py`).*

---

## Guía de Uso

Al iniciar el programa, se desplegará el menú interactivo:

```text
========================================
   Sistema de Stock - Computación
========================================
1. Agregar producto (Crear)
2. Mostrar productos (Consultar todos)
3. Buscar producto (Consultar específico)
4. Actualizar producto (Modificar)
5. Eliminar producto (Borrar)
6. Salir
========================================
```

* **Precios decimales:** Al cargar o modificar precios, el sistema acepta tanto punto (`.`) como coma (`,`) como separador decimal (por ejemplo: `45999.50` o `45999,50`) y los almacena con precisión decimal sin redondear.
* **Edición rápida:** En la opción **4 (Actualizar producto)**, si se deja un campo en blanco presionando `ENTER`, se mantiene el dato registrado anteriormente.

---

## Autor

* Proyecto desarrollado como **Trabajo Práctico - Talento Tech**.