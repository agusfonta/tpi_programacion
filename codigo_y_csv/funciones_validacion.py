# ============================================
# FUNCIONES DE VALIDACIÓN
# ============================================

def validar_numero_entero(numero):
    """
    Recibe un numero y valida que sea correcto. Retorna True o False
    
    """
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
        print("  - Escritura permitida -> 2000")
        print("~"*70)
        return False


def validar_opcion_menu(min_opcion, max_opcion):

    """
    Recibe un numero y valida que sea entre las opciones del menu. Retorna la opcion
    
    """
    while True:
        try:
            opcion = int(input("· Seleccione una opción: "))

            if min_opcion <= opcion <= max_opcion:
                return opcion
            else:
                print("~"*50)
                print(f"  x Error: Ingrese un número \n entre {min_opcion} y {max_opcion}")
                print("~"*50)
        except ValueError:
            print("~"*50)
            print("  x Error: Debe ingresar un número válido.")
            print("~"*50)

def validar_texto(texto):
    """
    Recibe un texto y valida que sea correcto. Retorna True o False
    
    """
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


def validar_rango(min, max):
    """
    Recibe dos numeros. Valida que ambos sean numeros y que el minimo sea mas chico que el maximo
    
    """
    if not max > min:
        print("~"*50)
        print(f"  x El numero ingresado debe ser mayor al \n minimo ingresado -> {min}")
        print("~"*50)
        return False

    return True