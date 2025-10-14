

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
# FUNCIONES DE CARGA DE DATOS
# ============================================

def crear_lista_de_dicccionarios_de_paises(RUTA):
    dato = []  # Lista de diccionarios de paises
    paises_sin_repetir=set()
    try:
        with open(RUTA, newline='', encoding="utf-8") as archivo:
            paises = csv.DictReader(archivo, delimiter=";")
            for fila in paises:
                nombre_pais=fila["nombre"]
                if nombre_pais in paises_sin_repetir:
                    continue
                paises_sin_repetir.add(nombre_pais)
                fila['poblacion'] = int(fila['poblacion'])
                fila['superficie'] = int(fila['superficie'])
                dato.append(fila)
        return dato
    except FileNotFoundError:
        print(f"Error: El archivo '{RUTA}' no fue encontrado.")
        return []
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []

# # ============================================
# # FUNCIONES DE CARGA DE DATOS
# # ============================================

# def crear_lista_de_dicccionarios_de_paises(RUTA):
#     datos = []  # Lista de diccionarios de paises
#     try:
#         with open(RUTA, newline='', encoding="utf-8") as archivo:
#             paises = csv.DictReader(archivo, delimiter=";")
#             for fila in paises:
#                 fila['poblacion'] = fila['poblacion']
#                 fila['superficie'] = fila['superficie']
#                 datos.append(fila)
        
#         return datos
#     except FileNotFoundError:
#         print(f"Error: El archivo '{RUTA}' no fue encontrado.")
#         return []
#     except Exception as e:
#         print(f"Error al cargar el archivo: {e}")
#         return []
