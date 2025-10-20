# ============================================
# FUNCIONES DE VALIDACIÓN
# ============================================

def validar_numero_entero(numero): # Arreglar que acepte , . y " "
    try:
        if (not(numero.isdigit())) or (int(numero) <= 0):
            raise ValueError("Debe ingresar un número entero válido positivo, sin decimales.")
    
        if '.' in numero or ',' in numero:
            raise ValueError("No se permiten puntos ni comas. Intenta de nuevo.\n")
        return True
    
    except ValueError as e:
        print("~"*50)
        print("  x Error: ", e )
        print("  - Escritura permitida -> 20000 ")
        print("~"*50)


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
    
    while True:
        if len(texto) == 0:
            texto = input(" x Campo vacio. Por favor ingrese una palabra: ")
            
        if not texto.isalpha():
            texto = input(" x Por favor ingrese una palabra: ")
            continue

        return texto


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

