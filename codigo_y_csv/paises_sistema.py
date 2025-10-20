""" Sistema de Gestión de Países - TPI Programación """

# ============================================
# IMPORTACIONES
# ============================================

import funciones_busqueda 
import funciones_carga_datos
import funciones_menu
import funciones_validacion
import funciones_visualizacion

RUTA_ARCHIVO = "paises.csv"  # Nombre del archivo CSV

# ============================================
# PRINCIPAL
# ============================================

def main():
#____________________________ CARGAR DATOS _______________________________________# 

    paises = funciones_carga_datos.crear_lista_paises(RUTA_ARCHIVO)
    if not paises:
        print("No se pudieron cargar los datos. El programa finalizará.")
        return
    print(f"Se cargaron {len(paises)} países correctamente.")
    
#____________________________ FUNCION PRINCIPAL ___________________________________#

    while True:
        funciones_menu.menu_principal()
        opcion = funciones_validacion.validar_opcion_menu(0, 4)
            
        match opcion:
            case 1: #___________________ Op1. Buscar por pais ____________________
                    print(" ")
                    print("=" *50)
                    print(f" 1. BUSCAR PAIS POR NOMBRE")
                    print("=" *50)
                    nombre = input("· Ingrese el nombre del país a buscar: ").capitalize()
                    texto = funciones_validacion.validar_texto(nombre)
                    if texto:
                        funciones_busqueda.buscar_por_nombre(paises,texto,"nombre")

            case 2: #_________________ Op2. Buscar por filtros ___________________
                funciones_menu.menu_filtros(paises)

            case 3: #_________________ Op3. Ordenar ______________________________
                funciones_menu.menu_ordenamiento(paises)
            
            case 4: #_________________ Op4. Mostrar estadisticas _________________
                print("=" *50)
                print(f" 4. MOSTRAR ESTADISTICAS")
                print("=" *50)
                funciones_visualizacion.mostrar_estadisticas(paises)
            
            case 0: #_________________ Op0. Salir _______________________________
                print("=" *50)
                print(f" 0. SALIR")
                print("=" *50)
                print("\n¡Gracias por usar el sistema! Hasta luego.")
                break

            # case _ : Ya esta validado en las validaciones de la opcion 

# ============================================
# PUNTO DE ENTRADA
# ============================================

if __name__ == "__main__":
    main()
