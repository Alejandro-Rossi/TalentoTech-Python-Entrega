import math

def pedir_texto_obligatorio(mensaje):
    """Solicita un texto asegurando que no quede vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("❌ Error. Este campo no puede quedar vacío.")

def pedir_entero(mensaje):
    """Solicita un número entero positivo validando con try-except."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("❌ Error. El número no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("❌ Error. Ingrese únicamente números enteros válidos.")

def pedir_flotante(mensaje):
    """Solicita un número decimal positivo sin redondear."""
    while True:
        entrada = input(mensaje).strip().replace(",", ".")
        try:
            valor = float(entrada)
            if math.isnan(valor) or math.isinf(valor) or valor < 0:
                print("❌ Error. Ingrese un precio válido y no negativo.")
                continue
            return valor
        except ValueError:
            print("❌ Error. Ingrese un número válido (ej. 15499.99).")

def pedir_entero_opcional(mensaje, valor_actual):
    """Permite mantener el valor actual con ENTER o ingresar un nuevo entero positivo."""
    while True:
        entrada = input(mensaje).strip()
        if entrada == "":
            return valor_actual
        try:
            valor = int(entrada)
            if valor < 0:
                print("❌ Error. El número no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("❌ Error. Ingrese únicamente números enteros válidos.")
