

# ============================================
# IMPORTACIONES
# ============================================
import csv
import unicodedata
RUTA_ARCHIVO = "paises.csv"  # Nombre del archivo CSV

# # ============================================
# # FUNCIONES DE CARGA DE DATOS
# # ============================================

import csv
import unicodedata

def normalizar_texto(texto):
    """Elimina las tildes de un texto"""
    return unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8')

def crear_lista_paises(RUTA):
    paises = []  # Lista de diccionarios de paises
    paises_sin_repetir = set()
    try:
        with open(RUTA, newline='', encoding="utf-8") as archivo:
            paises_csv = csv.DictReader(archivo, delimiter=";") #se arma la lisa de diccionarios
            for pais in paises_csv: #itera por cada pais(diccionarios)
                if len(pais) == 4:  #corrobora que tenga 4 valores
                    for clave in pais: #itera por cada valor del diccionario
                        pais[clave] = pais[clave].strip()
                        if not pais[clave]: 
                            pais[clave] = "" #si no tiene valor no hace nada
                    
                    # Normalizar el nombre del país (sin tildes)
                    nombre_pais = normalizar_texto(pais["nombre"])
                    if nombre_pais in paises_sin_repetir:
                        continue
                    paises_sin_repetir.add(nombre_pais)
                    
                    # Normalizar todos los campos de texto
                    pais["nombre"] = normalizar_texto(pais["nombre"])
                    if "capital" in pais:
                        pais["capital"] = normalizar_texto(pais["capital"])
                    
                    if pais['poblacion'].isnumeric() and pais['superficie'].isnumeric():
                        pais['poblacion'] = int(pais['poblacion'])
                        pais['superficie'] = int(pais['superficie'])
                        paises.append(pais)
        return paises
    except FileNotFoundError:
        print(f"Error: El archivo '{RUTA}' no fue encontrado.")
        return []
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []