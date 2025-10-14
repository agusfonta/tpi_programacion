# ============================================
# IMPORTACIONES
# ============================================
import csv
import funciones_busqueda 
import funciones_carga_datos
import funciones_estadisticas
import funciones_filtros
import funciones_menu
import funciones_ordenamiento
import funciones_validacion
import funciones_visualizacion
RUTA_ARCHIVO = "paises.csv"

# ============================================
# FUNCIONES DE VALIDACIÓN
# ============================================

def validar_numero_entero(numero): # Arreglar que acepte , . y " "
    try:
        if (not(numero.isdigit())) and (int(numero) <= 0):
            raise ValueError("Debe ingresar un número entero válido positivo, sin decimales.")
    
        if '.' in numero or ',' in numero:
            raise ValueError("No se permiten puntos ni comas. Intenta de nuevo.\n")
        return True
    
    except ValueError as e:
        print("Error: ", e )
        print("Escritura permitida -> 20000 ")


def validar_opcion_menu(min_opcion, max_opcion):
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if min_opcion <= opcion <= max_opcion:
                return opcion
            else:
                print(f"Error: Ingrese un número entre {min_opcion} y {max_opcion}")
        except ValueError:
            print("Error: Debe ingresar un número válido.")

def validar_texto(texto):
    try:
        if len(texto) == 0:
            raise ValueError("Campo vacio. Por favor ingrese una palabra")
        
        if not texto.isalpha():
            raise ValueError("Por favor ingrese una palabra")

        return True

    except ValueError as e:
        print("Error: ", e)
        return False


def validar_rango():
    while True:
        rango_min = input("Ingrese el valor minimo del rango: ")
        if not validar_numero_entero(rango_min):
            continue
        rango_min  = int(rango_min)
        while True:
            rango_max = input("Ingrese el valor maximo del rango: ")

            if not validar_numero_entero(rango_max):
                continue
            rango_max  = int(rango_max)
            if not rango_max > rango_min:
                print(f"El numero ingresado debe ser mayor al minimo ingresado -> {rango_min}")
            else:
                break

        return True, rango_min, rango_max