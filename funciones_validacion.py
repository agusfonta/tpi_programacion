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
        # numero.strip(",")
        # numero.strip(".")
        # numero.strip(" ")

        if not (numero.isdigit()):
            raise ValueError
        return True

    except ValueError:
        print("Error: Debe ingresar un número entero válido, sin coma (,) ni punto (.).")




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
    rango_min = input("Ingrese el valor minimo del rango: ")
    rango_max = input("Ingrese el valor maximo del rango: ")

    while rango_max <= rango_min:
        rango_max = input("Por favor ingrese un valor mayor al minimo: ")

    if validar_numero_entero(rango_max) and validar_numero_entero(rango_min):
        return True, rango_min, rango_max
