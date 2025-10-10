"""
Sistema de Gestión de Países
Tecnicatura Universitaria en Programación

"""

# ============================================
# IMPORTACIONES
# ============================================
import csv
import funciones as f

# ============================================
# FUNCIÓN PRINCIPAL
# ============================================

def main():
    """
    Función principal que ejecuta el programa.
    """
    # Cargar datos
    RUTA_ARCHIVO = "paises.csv"  # Nombre del archivo CSV
    paises = f.crear_lista_de_dicccionarios_de_paises(RUTA_ARCHIVO)
    
    if not paises:
        print("No se pudieron cargar los datos. El programa finalizará.")
        return
    
    print(f"Se cargaron {len(paises)} países correctamente.")
    
    # Bucle principal del programa
    while True:
        f.mostrar_menu_principal()
        opcion = f.validar_opcion_menu(0, 4)
        
        if opcion == 1:
            # Buscar país por nombre
            nombre = input("Ingrese el nombre del país a buscar: ").capitalize()
            validacion = f.validar_texto(nombre)

            if validacion:
                f.buscar_por_nombre(paises,nombre) 
            
        elif opcion == 2: # ARREGLAR FUNCION RANGO , que acepte , . " " y buscar que es el None que aparece en funciones de filtro
            f.menu_filtros(paises)

        elif opcion == 3:
            f.menu_ordenamiento(paises)

        elif opcion == 4:
            # Mostrar estadísticas
            f.mostrar_estadisticas(paises)
            
        elif opcion == 5:
            # Mostrar todos los países
            f.mostrar_paises(paises)
            
        elif opcion == 0:
            print("\n¡Gracias por usar el sistema! Hasta luego.")
            break


# ============================================
# PUNTO DE ENTRADA
# ============================================

if __name__ == "__main__":
    main()
