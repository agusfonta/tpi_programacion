

# ============================================
# IMPORTACIONES
# ============================================
import csv
RUTA_ARCHIVO = "paises.csv"

# # ============================================
# # FUNCIONES DE CARGA DE DATOS
# # ============================================


def crear_lista_de_dicccionarios_de_paises(RUTA):
    paises = []  # Lista de diccionarios de paises
    paises_sin_repetir = set()
    try:
        with open(RUTA, newline='', encoding="utf-8") as archivo:
            paises_csv = csv.DictReader(archivo, delimiter=";") #se arma la lisa de diccionarios
            for pais in paises_csv: #itera por cada pais(diccionarios)
                if len(pais) == 4:  #corrobora que tenga 4 valores
                    for clave in pais: #itera por cada valor del diccionario
                        if pais[clave]: #si tiene un valor es decir no es '' 
                            pais[clave] = pais[clave].strip()
                        else:
                            pais[clave] = "" #si no tiene valor no hace nada
                    nombre_pais = pais["nombre"]
                    if nombre_pais in paises_sin_repetir:
                        continue
                    paises_sin_repetir.add(nombre_pais)
                    
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