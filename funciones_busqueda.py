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
# FUNCIONES DE BÚSQUEDA
# ============================================

def buscar_por_nombre(list_dict_paises, dato): #OPCION 1 DEL MENU 

    """ Ejemplo guia: 

    list_dict_paises = diccionario
    dato =  China
    filtro = nombre """

    for pais in list_dict_paises:
        if pais["nombre"] == dato:
            dic_pais_encontrado = pais
            break

    for caracteristica,dato in dic_pais_encontrado.items():
        print(caracteristica.capitalize() ,": ",dato)


def buscar_por_filtro(list_dict_paises, dato, filtro): #OPCION 2 DEL MENU 

    paises_encontrados = []

    for pais in list_dict_paises:
        if pais[filtro] == dato:
            paises_encontrados.append(pais["nombre"])
    print(paises_encontrados)


def buscar_por_rango(min,max,paises,tipo):
    print(f"- Paises con {tipo} entre {min} y {max}")
    min = int(min)
    max = int(max)
    existen = False
    for pais in paises:
        if min <= int(pais[tipo]) <= max:
            existen = True
            print(f"{pais["nombre"],pais[tipo]}")

    if not existen:
        print("No se encontraron paises entre esos rangos.")
