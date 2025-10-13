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
# FUNCIONES DE VISUALIZACIÓN
# ============================================

def mostrar_paises(paises):
    """
    Muestra la lista de países en formato legible.
    
    Parámetros:
        paises (list): lista de diccionarios de países
    """
    if not paises:
        print("No hay países para mostrar.")
        return
    
    print("\n" + "="*80)
    print(f"{'NOMBRE':<30} {'POBLACIÓN':<15} {'SUPERFICIE':<15} {'CONTINENTE':<15}")
    print("="*80)
    
    for pais in paises:
        # TODO: Formatear y mostrar cada país
        pass
    
    print("="*80)
    print(f"Total: {len(paises)} países\n")


def mostrar_estadisticas(paises):
    """
    Muestra las estadísticas generales de los países.
    
    Parámetros:
        paises (list): lista de diccionarios de países
    """
    if not paises:
        print("No hay datos para mostrar estadísticas.")
        return
    
    print("\n" + "="*50)
    print("ESTADÍSTICAS GENERALES")
    print("="*50)
    
    # TODO: Llamar a las funciones de estadísticas y mostrar resultados
    # - País con mayor población
    # - País con menor población
    # - Promedio de población
    # - Promedio de superficie
    # - Cantidad de países por continente
    
    print("="*50 + "\n")
