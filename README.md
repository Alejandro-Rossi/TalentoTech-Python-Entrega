# Sistema de Gestión de Stock — Artículos de Computación

Aplicación de consola desarrollada en **Python 3** con persistencia de datos en **SQLite3** para administrar el inventario de productos de computación mediante un sistema **CRUD** completo (Crear, Consultar, Actualizar y Eliminar).

---

## Características principales

* **Arquitectura modular en 3 capas:** Separación clara entre la interfaz de usuario (`main.py`), la lógica de acceso a datos (`database.py`) y las validaciones de entrada (`validaciones.py`).
* **Persistencia con SQLite3:** Almacenamiento local automático en el archivo `stock_computacion.db` mediante consultas SQL parametrizadas (`?`) para prevenir inyección SQL y asegurar la integridad de los datos.
* **Precisión decimal y formato local (`n.nnn,nn`):**
  * Almacena los precios como valores de punto flotante (`REAL`) en la base de datos sin redondeos.
  * Acepta entradas con separadores de miles y decimales tanto en formato argentino (`545.600,65`) como internacional (`545,600.65`) o sin separador de miles (`545600,65`).
  * Muestra todos los importes en consola formateados con punto para miles y coma para dos decimales (`$545.600,65`).
* **Edición parcial inteligente:** Al actualizar un producto existente, permite presionar `ENTER` sobre cualquier campo para conservar su valor actual sin necesidad de reescribir todo el registro.
* **Búsqueda flexible:** Consulta productos por coincidencia parcial en `marca` o `modelo` sin distinguir entre mayúsculas y minúsculas (`LIKE`).
* **Manejo robusto de errores:** Control de excepciones mediante bloques `try / except / finally` para errores de base de datos (`sqlite3.Error` con `rollback()` y cierre garantizado de conexión), conversiones numéricas (`ValueError`) e interrupciones de teclado (`KeyboardInterrupt`, `EOFError`).
* **Ejecución rápida en Windows:** Incluye un script batch (`iniciar_stock.bat`) configurado en UTF-8 para iniciar el sistema con doble clic.

---

## Estructura del proyecto

```text
proyecto_stock/
│
├── main.py                # Punto de entrada: menú principal, vistas e interacción por consola
├── database.py            # Capa de datos: conexión SQLite3, esquema de tabla y operaciones CRUD
├── validaciones.py        # Capa de utilidades: normalización, validación de entradas y formateo de precios
├── iniciar_stock.bat      # Script lanzador para Windows con soporte UTF-8
├── stock_computacion.db   # Base de datos SQLite (se crea automáticamente al iniciar)
└── README.md              # Documentación del proyecto
```

---

## Requisitos

* **Python 3.10 o superior** (utiliza únicamente módulos de la biblioteca estándar: `sqlite3` y `math`, por lo que no requiere instalar dependencias externas).

---

## Ejecución

### Opción 1: Desde el lanzador de Windows (recomendado)
Haz doble clic sobre el archivo **`iniciar_stock.bat`** dentro de la carpeta del proyecto. El script configura la consola en UTF-8 (para visualizar tildes y símbolos correctamente), detecta la instalación de Python disponible (`python` o `py`) y ejecuta `main.py`.

### Opción 2: Desde la terminal
1. Abre una terminal y ubícate en la carpeta del proyecto:
   ```bash
   cd ruta/a/proyecto_stock
   ```
2. Ejecuta el programa principal:
   ```bash
   python main.py
   ```

---

## Esquema de la base de datos

Al ejecutarse por primera vez, `database.inicializar_db()` crea automáticamente la tabla `productos` en `stock_computacion.db`:

| Columna | Tipo SQLite | Restricciones | Descripción |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PRIMARY KEY AUTOINCREMENT` | Identificador único autoincremental del producto |
| `marca` | `TEXT` | `NOT NULL` | Fabricante o marca (ej. `Kingston`, `Asus`, `Logitech`) |
| `modelo` | `TEXT` | `NOT NULL` | Modelo comercial, capacidad o SKU (ej. `FURY DDR5 32GB`) |
| `tipo` | `TEXT` | `NOT NULL` | Categoría del artículo (ej. `Memoria RAM`, `Monitor`) |
| `precio` | `REAL` | `NOT NULL` | Precio unitario en pesos con precisión decimal |

---

## Funcionalidades del menú

1. **Agregar producto (Crear):** Solicita marca, modelo, tipo y precio validando que no haya campos vacíos ni valores negativos.
2. **Mostrar productos (Consultar todos):** Lista el inventario completo con su `ID`, descripción, categoría y precio formateado (`$n.nnn,nn`).
3. **Buscar producto (Consultar específico):** Filtra registros por coincidencias parciales en marca o modelo.
4. **Actualizar producto (Modificar):** Permite seleccionar un producto por su `ID` y modificar todos o solo algunos de sus campos.
5. **Eliminar producto (Borrar):** Elimina permanentemente un registro de la base de datos previa verificación de existencia por `ID`.
6. **Salir:** Finaliza la ejecución del sistema de manera segura.

---

## Autor

* Proyecto desarrollado por Roberto Aljeandro Rossi como **Trabajo Práctico — Talento Tech**.
