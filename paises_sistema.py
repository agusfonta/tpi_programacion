"""
Sistema de Gestión de Países
Tecnicatura Universitaria en Programación

"""

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
# FUNCIÓN PRINCIPAL
# ============================================

def main():
    """
    Función principal que ejecuta el programa.
    """
    # Cargar datos
    RUTA_ARCHIVO = "paises.csv"  # Nombre del archivo CSV
    paises = funciones_carga_datos.crear_lista_de_dicccionarios_de_paises(RUTA_ARCHIVO)
    
    if not paises:
        print("No se pudieron cargar los datos. El programa finalizará.")
        return
    
    print(f"Se cargaron {len(paises)} países correctamente.")
    
    # Bucle principal del programa
    while True:
        funciones_menu.menu_principal()
        opcion = funciones_validacion.validar_opcion_menu(0, 4)

        match opcion:
            case 1:
                # Buscar país por nombre
                nombre = input("Ingrese el nombre del país a buscar: ").capitalize()
                validacion = funciones_validacion.validar_texto(nombre)
                #TODO busqueda parcial 

                if validacion:
                    funciones_busqueda.buscar_por_nombre(paises,nombre) 
                
            case 2: #TODO buscar que es el None que aparece en funciones de filtro
                funciones_menu.menu_filtros(paises)

            case 3:
                funciones_menu.menu_ordenamiento(paises)

            case 4:
                # Mostrar estadísticas
                funciones_visualizacion.mostrar_estadisticas(paises)
                
            case 0:
                print("\n¡Gracias por usar el sistema! Hasta luego.")
                break

            # case _ : Ya esta validado en las validaciones de la opcion 

# ============================================
# PUNTO DE ENTRADA
# ============================================

if __name__ == "__main__":
    main()
