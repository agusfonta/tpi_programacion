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
# FUNCIONES DE ESTADÍSTICAS
# ============================================

def obtener_pais_mayor_poblacion(paises):
    """
    Encuentra el país con mayor población.
    
    Parámetros:
        paises (list): lista de diccionarios de países
    
    Retorna:
        dict: país con mayor población
    """
    # TODO: Implementar búsqueda del país con mayor población
    # Usar max() con key
    pass


def obtener_pais_menor_poblacion(paises):
    """
    Encuentra el país con menor población.
    
    Parámetros:
        paises (list): lista de diccionarios de países
    
    Retorna:
        dict: país con menor población
    """
    # TODO: Implementar búsqueda del país con menor población
    pass


def calcular_promedio_poblacion(paises):
    """
    Calcula el promedio de población de los países.
    
    Parámetros:
        paises (list): lista de diccionarios de países
    
    Retorna:
        float: promedio de población
    """
    # TODO: Implementar cálculo de promedio
    # Sumar todas las poblaciones y dividir por cantidad
    pass


def calcular_promedio_superficie(paises):
    """
    Calcula el promedio de superficie de los países.
    
    Parámetros:
        paises (list): lista de diccionarios de países
    
    Retorna:
        float: promedio de superficie
    """
    # TODO: Implementar cálculo de promedio
    pass


def contar_paises_por_continente(paises):
    """
    Cuenta la cantidad de países por continente.
    
    Parámetros:
        paises (list): lista de diccionarios de países
    
    Retorna:
        dict: diccionario con continente como clave y cantidad como valor
    """
    conteo = {}
    # TODO: Implementar conteo por continente
    # - Recorrer países
    # - Si el continente no existe en el diccionario, agregarlo con valor 1
    # - Si existe, incrementar el contador
    return conteo
