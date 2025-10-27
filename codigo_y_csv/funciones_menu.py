# ============================================
# IMPORTACIONES
# ============================================
import funciones_pide_datos
import funciones_ordenamiento
import funciones_validacion
import funciones_visualizacion


# ============================================
# FUNCIONES DE MENÚS
# ============================================

def menu_principal():

    """Muestra el menu principal"""

    print("\n" + "="*50)
    print("    SISTEMA DE GESTIÓN DE PAÍSES")
    print("="*50)
    print(" 1. Buscar país por nombre")
    print(" 2. Filtrar países")
    print(" 3. Ordenar países")
    print(" 4. Mostrar estadísticas")
    print(" 5. Agregar pais nuevo")
    print(" 6. Editar pais existente")
    print(" 0. Salir")
    print("-"*50)


def menu_filtros(paises): 
    
    """Recibe la lista de paises y muestra el menu de la opcion 2 (filtros) del menu principal"""
    while True:
        print(" ")
        print("="*50)
        print("   2. FILTRAR PAISES ")
        print("="*50)
        print(" 1. Por continente")
        print(" 2. Por rango de población")
        print(" 3. Por rango de superficie")
        print(" 0. Volver al menú principal")
        print("-"*50)
        
        opcion = funciones_validacion.validar_opcion_menu(0, 3)

        match opcion: 
            case 1:
                funciones_pide_datos.ingresar_texto(paises,"continente")
    
            case 2:
                funciones_pide_datos.ingresar_rango(paises, "poblacion")

            case 3:
                funciones_pide_datos.ingresar_rango(paises, "superficie")
        
            case 0:
                break

            case _: 
                print("Ocurrio algo inesperado")


def menu_ordenamiento(paises): # MENU Opcion 3

    """Recibe la lista de paises y muestra el menu de la opcion 3 (ordenamiento) del menu principal"""
    while True:
        print(" ")
        print("="*50)
        print("   3. ORDENAR PAISES ")
        print("="*50)
        print(" 1. Por nombre (A-Z)")
        print(" 2. Por nombre (Z-A)")
        print(" 3. Por población (menor a mayor)")
        print(" 4. Por población (mayor a menor)")
        print(" 5. Por superficie (menor a mayor)")
        print(" 6. Por superficie (mayor a menor)")
        print(" 0. Volver al menú principal")
        print("-"*50)
        
        opcion = funciones_validacion.validar_opcion_menu(0, 6)
        
        match opcion:
            case 1:
                print(" ")
                print(f"1. Paises ordenados (A-Z) ")
                print("-"*50)
                paises_ordenados = funciones_ordenamiento.ordenar_paises_por(paises, False, "nombre")
                funciones_visualizacion.mostrar_ordenados(paises_ordenados,"nombre")

            case 2:
                print(" ")
                print("2. Paises ordenados (Z-A)")
                print("-"*50)
                paises_ordenados = funciones_ordenamiento.ordenar_paises_por(paises,True, "nombre")
                funciones_visualizacion.mostrar_ordenados(paises_ordenados,"nombre")

            case 3:
                print(" ")
                print("3. Paises ordenados por poblacion de menor a mayor")
                print("-"*50)
                paises_ordenados = funciones_ordenamiento.ordenar_paises_por(paises, False,"poblacion")
                funciones_visualizacion.mostrar_ordenados(paises_ordenados,"poblacion")

            case 4:
                print(" ")
                print("4. Paises ordenados por poblacion de mayor a menor")
                print("-"*50)
                paises_ordenados = funciones_ordenamiento.ordenar_paises_por(paises, True,"poblacion")
                funciones_visualizacion.mostrar_ordenados(paises_ordenados,"poblacion")

            case 5:
                print(" ")
                print("5. Paises ordenados por superficie de menor a mayor")
                print("-"*50)
                paises_ordenados = funciones_ordenamiento.ordenar_paises_por(paises, False,"superficie")
                funciones_visualizacion.mostrar_ordenados(paises_ordenados,"superficie")
            
            case 6:
                print(" ")
                print("6. Paises ordenados por superficie de mayor a menor")
                print("-"*50)
                paises_ordenados = funciones_ordenamiento.ordenar_paises_por(paises, True,"superficie")
                funciones_visualizacion.mostrar_ordenados(paises_ordenados,"superficie")

            case 0:
                break

            case _: 
                print("Ocurrio algo inesperado")




