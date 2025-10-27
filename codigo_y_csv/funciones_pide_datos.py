# ============================================
# IMPORTACIONES
# ============================================

import funciones_validacion
import funciones_busqueda
import funciones_visualizacion

# ============================================
# FUNCIONES PIDEN DATOS
# ============================================

def ingresar_rango(paises, key):
    """
    Pide al usuario que ingrese el rango de numeros

    key = poblacion o superficie
    paises = lista de paises
    
    """
    while True:
        rango_min = input("· Ingrese el valor minimo del rango: ")
        if not funciones_validacion.validar_numero_entero(rango_min):
            continue
        rango_min=int(rango_min)

        while True:
            rango_max = input("· Ingrese el valor maximo del rango: ")
            if not funciones_validacion.validar_numero_entero(rango_max):
                continue
            rango_max  = int(rango_max)
            if not funciones_validacion.validar_rango(rango_min, rango_max):
                continue
            break
        
        print(" ")
        print(f"· Paises con '{key}' entre '{rango_min}' y '{rango_max}' ")
        print("-"*50)

        paises_encontrados = funciones_busqueda.buscar_por_rango(rango_min, rango_max, paises, key)

        if type(paises_encontrados) == list:
            funciones_visualizacion.mostrar_lista_al_usuario(paises_encontrados)
        else:
            print(paises_encontrados)

        break 

def ingresar_texto(paises, key):

    """
    Pide al usuario que ingrese un texto

    key = nombre o continente
    paises = lista de paises
    
    """
    while True:
        dato_ingresado= input(f"· Ingrese el {key}: ").strip()
        if not funciones_validacion.validar_texto(dato_ingresado):
            continue
        dato_ingresado = dato_ingresado.capitalize()

        print(" ")
        print(f"· Paises que coinciden con '{dato_ingresado}' ")
        print("-"*50)

        paises_encontrados = funciones_busqueda.buscar_por_nombre(paises, dato_ingresado, key)

        if type(paises_encontrados) == list:
            funciones_visualizacion.mostrar_lista_al_usuario(paises_encontrados)
        else:
            print(paises_encontrados)