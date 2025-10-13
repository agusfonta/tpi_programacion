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
# FUNCIONES DE ORDENAMIENTO
# ============================================

def ordenar_paises_por(paises, reverse, tipo):
    ordenado = sorted(paises, key=lambda pais: pais[tipo], reverse=reverse)
    for p in ordenado:
        print(p[tipo])

def ordenar_por_poblacion(paises, ascendente=True):
    """
    Ordena países por población.
    
    Parámetros:
        paises (list): lista de diccionarios de países
        ascendente (bool): True para menor a mayor, False para mayor a menor
    
    Retorna:
        list: lista ordenada de países
        ordenado = sorted(personas, key=lambda pais: pais['nombre'])
    """
    # TODO: Implementar ordenamiento por población
    return paises


def ordenar_por_superficie(paises, ascendente=True):
    """
    Ordena países por superficie.
    
    Parámetros:
        paises (list): lista de diccionarios de países
        ascendente (bool): True para menor a mayor, False para mayor a menor
    
    Retorna:
        list: lista ordenada de países
    """
    # TODO: Implementar ordenamiento por superficie
    return paises