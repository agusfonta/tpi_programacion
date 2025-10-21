# ============================================
# FUNCIONES DE VALIDACIÓN
# ============================================

def validar_numero_entero(numero):
    try:
        if len(numero) == 0:
            raise ValueError("Campo vacío. Debe ingresar un número.")
        
        if '.' in numero or ',' in numero or ' ' in numero:
            raise ValueError("No se permiten puntos, comas ni espacios.")
        
        if not numero.isdigit():
            raise ValueError("Debe ingresar solo dígitos numéricos.")
        # Validar que sea mayor a 0
        if int(numero) <= 0:
            raise ValueError("El número debe ser mayor a 0.")
        return True
    except ValueError as e:
        print("~"*70)
        print(f"  x Error: {e}")
        print("  - Escritura permitida -> 20000")
        print("~"*70)
        return False


def validar_opcion_menu(min_opcion, max_opcion):
    while True:
        try:
            opcion = int(input("· Seleccione una opción: "))

            if min_opcion <= opcion <= max_opcion:
                return opcion
            else:
                print("~"*50)
                print(f"  x Error: Ingrese un número entre {min_opcion} y {max_opcion}")
                print("~"*50)
        except ValueError:
            print("~"*50)
            print("  x Error: Debe ingresar un número válido.")
            print("~"*50)

def validar_texto(texto):
    try:
        if len(texto) == 0:
            raise ValueError(" x Campo vacío. Debe ingresar un texto.")
        if not texto.isalpha():
            raise ValueError(" x Solo se permiten letras.")
        return True
    except ValueError as e:
        print("~"*70)
        print(f"  x Error: {e}")
        print("~"*70)
        return False


def validar_rango():
    while True:
        rango_min = input("· Ingrese el valor minimo del rango: ")
        if not validar_numero_entero(rango_min):
            continue
        rango_min  = int(rango_min)
        while True:
            rango_max = input("· Ingrese el valor maximo del rango: ")

            if not validar_numero_entero(rango_max):
                continue
            rango_max  = int(rango_max)
            if not rango_max > rango_min:
                print("~"*50)
                print(f"  x El numero ingresado debe ser mayor al minimo ingresado -> {rango_min}")
                print("~"*50)
            else:
                break

        return True, rango_min, rango_max