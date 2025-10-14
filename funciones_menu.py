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
# FUNCIONES DE MENÚS
# ============================================

def menu_principal():
    """
    Muestra el menú principal del sistema.
    """
    print("\n" + "="*20)
    print("SISTEMA DE GESTIÓN DE PAÍSES")
    print("="*20)
    print("1. Buscar país por nombre")
    print("2. Filtrar países")
    print("3. Ordenar países")
    print("4. Mostrar estadísticas")
    print("0. Salir")
    print("="*20)


def menu_filtros(paises):
    while True:
        print("\n--- FILTRAR PAÍSES ---")
        print("1. Por continente")
        print("2. Por rango de población")
        print("3. Por rango de superficie")
        print("0. Volver al menú principal")
        
        opcion = funciones_validacion.validar_opcion_menu(0, 3)


        if opcion == 1:
            continente = input("Ingrese el continente: ").capitalize()
            filtro = "continente"
            valido = funciones_validacion.validar_texto(continente)
            if valido:
                funciones_busqueda.buscar_por_filtro(paises, continente, filtro)


        elif opcion == 2:
            valido,min,max = funciones_validacion.validar_rango()
            tipo = "poblacion"
            if valido:
                print(funciones_busqueda.buscar_por_rango(min, max, paises,tipo))

        elif opcion == 3:
            valido,min,max = funciones_validacion.validar_rango()
            tipo = "superficie"
            if valido:
                print(funciones_busqueda.buscar_por_rango(min, max, paises,tipo))
    
        elif opcion == 0:
            break


def menu_ordenamiento(paises):
    """
    Submenú para ordenar países.
    
    Parámetros:
        paises (list): lista de diccionarios de países
    """
    while True:
        print("\n--- ORDENAR PAÍSES ---")
        print("1. Por nombre (A-Z)")
        print("2. Por nombre (Z-A)")
        print("3. Por población (menor a mayor)")
        print("4. Por población (mayor a menor)")
        print("5. Por superficie (menor a mayor)")
        print("6. Por superficie (mayor a menor)")
        print("0. Volver al menú principal")
        
        opcion = funciones_validacion.validar_opcion_menu(0, 6)
        
        if opcion == 1:
            print("1. Paises ordenados (A-Z)")
            funciones_ordenamiento.ordenar_paises_por(paises, False, "nombre")
        
        elif opcion == 2:
            print("2. Paises ordenados (Z-A)")
            funciones_ordenamiento.ordenar_paises_por(paises,True, "nombre")

        elif opcion == 3:
            print("3. Paises ordenados por poblacion de menor a mayor")
            funciones_ordenamiento.ordenar_paises_por(paises, False,"poblacion")

        elif opcion == 4:
            print("4. Paises ordenados por poblacion de mayor a menor")
            funciones_ordenamiento.ordenar_paises_por(paises, True,"poblacion")
        elif opcion == 5:
            print("5. Paises ordenados por superficie de menor a mayor")
            funciones_ordenamiento.ordenar_paises_por(paises, False,"superficie")
        elif opcion == 6:
            print("6. Paises ordenados por superficie de menor a mayor")
            funciones_ordenamiento.ordenar_paises_por(paises, True,"superficie")

        elif opcion == 0:
            break






