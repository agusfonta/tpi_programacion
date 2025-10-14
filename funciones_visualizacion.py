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
    if not paises:
        print("No hay datos para mostrar estadísticas.")
        return
    
    print("\n" + "="*50)
    print("ESTADÍSTICAS GENERALES")
    print("="*50)

    print("Pais con mayor poblacion: ")
    print(funciones_estadisticas.obtener_pais_mayor_poblacion(paises))
    
    print(" === Pais con menor poblacion === ")
    print(funciones_estadisticas.obtener_pais_menor_poblacion(paises))

    print(" === Promedio poblacion === ")
    print(funciones_estadisticas.calcular_promedio_poblacion(paises))

    print(" === Promedio superficie === ")
    print(funciones_estadisticas.calcular_promedio_superficie(paises))

    print(" === Cantidad de paises por continente === ")
    asia, europa, oceania, africa, america = funciones_estadisticas.contar_paises_por_continente(paises)
    print(f"=== Cantidad de paises de ASIA: {asia}")
    print(f"=== Cantidad de paises de EUROPA: {europa}")
    print(f"=== Cantidad de paises de OCEANIA: {oceania}")
    print(f"=== Cantidad de paises de AFRICA: {africa}")
    print(f"=== Cantidad de paises de AMERICA: {america}")
    
    print("="*50 + "\n")
