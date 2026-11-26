import math


def pedir_texto_obligatorio(mensaje):
    """Solicita un texto asegurando que no quede vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("❌ Error. Este campo no puede quedar vacío.")


def pedir_entero(mensaje):
    """Solicita un número entero positivo validando con try-except (para IDs)."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("❌ Error. El número no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("❌ Error. Ingrese únicamente números enteros válidos.")


def _normalizar_numero(entrada):
    """Convierte formatos con separador de miles y decimales (ej. 545.600,65) a float."""
    limpio = entrada.strip().replace("$", "").replace(" ", "")

    if "," in limpio and "." in limpio:
        # El último separador que aparece define cuál es el decimal
        if limpio.rfind(",") > limpio.rfind("."):
            # Formato argentino/europeo: 545.600,65 -> quitar puntos de miles y cambiar coma por punto
            limpio = limpio.replace(".", "").replace(",", ".")
        else:
            # Formato estadounidense: 545,600.65 -> quitar comas de miles
            limpio = limpio.replace(",", "")
    elif "," in limpio:
        # Solo hay coma: si hay más de una coma son miles (545,600,000), si hay una sola es decimal (545600,65)
        if limpio.count(",") > 1:
            limpio = limpio.replace(",", "")
        else:
            limpio = limpio.replace(",", ".")
    elif "." in limpio:
        # Si hay más de un punto son miles (1.545.600)
        if limpio.count(".") > 1:
            limpio = limpio.replace(".", "")

    return float(limpio)


def pedir_flotante(mensaje):
    """Solicita un precio decimal positivo aceptando separadores de miles y decimales."""
    while True:
        entrada = input(mensaje)
        try:
            valor = _normalizar_numero(entrada)
            if math.isnan(valor) or math.isinf(valor) or valor < 0:
                print("❌ Error. Ingrese un precio válido y no negativo.")
                continue
            return valor
        except ValueError:
            print("❌ Error. Ingrese un precio válido (ej. 545.600,65 o 545600.65).")


def pedir_flotante_opcional(mensaje, valor_actual):
    """Permite mantener el precio actual con ENTER o ingresar un nuevo decimal."""
    while True:
        entrada = input(mensaje)
        if entrada.strip() == "":
            return valor_actual
        try:
            valor = _normalizar_numero(entrada)
            if math.isnan(valor) or math.isinf(valor) or valor < 0:
                print("❌ Error. Ingrese un precio válido y no negativo.")
                continue
            return valor
        except ValueError:
            print("❌ Error. Ingrese un precio válido (ej. 545.600,65 o 545600.65).")
