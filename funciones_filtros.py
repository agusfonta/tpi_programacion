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
# FUNCIONES DE FILTRADO
# ============================================

def filtrar_por_continente(paises, continente):
    """
    Filtra países por continente.
    
    Parámetros:
        paises (list): lista de diccionarios de países
        continente (str): nombre del continente
    
    Retorna:
        list: países del continente especificado
    """
    filtrados = []
    # TODO: Implementar filtro por continente
    return filtrados


def filtrar_por_rango_poblacion(paises, min_poblacion, max_poblacion):
    """
    Filtra países por rango de población.
    
    Parámetros:
        paises (list): lista de diccionarios de países
        min_poblacion (int): población mínima
        max_poblacion (int): población máxima
    
    Retorna:
        list: países dentro del rango de población
    """
    filtrados = []
    # TODO: Implementar filtro por población
    return filtrados


def filtrar_por_rango_superficie(paises, min_superficie, max_superficie):
    """
    Filtra países por rango de superficie.
    
    Parámetros:
        paises (list): lista de diccionarios de países
        min_superficie (int): superficie mínima en km²
        max_superficie (int): superficie máxima en km²
    
    Retorna:
        list: países dentro del rango de superficie
    """
    filtrados = []
    # TODO: Implementar filtro por superficie
    return filtrados
