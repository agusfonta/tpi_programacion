

# ============================================
# IMPORTACIONES
# ============================================
import csv
import unicodedata
RUTA_ARCHIVO = "paises.csv"  

# ============================================
# FUNCIONES DE CARGA DE DATOS
# ============================================

def normalizar_texto(texto):
    """Elimina las tildes de un texto"""
    return unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8')

def crear_lista_paises(RUTA):
    paises = []
    paises_sin_repetir = set()
    try:
        with open(RUTA, newline='', encoding="utf-8") as archivo:
            paises_csv = csv.DictReader(archivo, delimiter=";")
            for pais in paises_csv:
                if len(pais) == 4:
                    for clave in pais:
                        pais[clave] = pais[clave].strip()
                        if not pais[clave]: 
                            pais[clave] = ""
                    
                    nombre_pais = normalizar_texto(pais["nombre"])
                    if nombre_pais in paises_sin_repetir:
                        continue
                    paises_sin_repetir.add(nombre_pais)
                    
                    pais["nombre"] = normalizar_texto(pais["nombre"])
                    if "capital" in pais:
                        pais["capital"] = normalizar_texto(pais["capital"])
                    
                    if pais['poblacion'].isnumeric() and pais['superficie'].isnumeric():
                        pais['poblacion'] = int(pais['poblacion'])
                        pais['superficie'] = int(pais['superficie'])
                        paises.append(pais)
        return paises
        
    except FileNotFoundError:
        print("="*70)
        print(f" x ERROR CRÍTICO: El archivo '{RUTA}' no fue encontrado.")
        print(f" Verifica que el archivo exista en la ruta correcta.")
        print("="*70)
        exit(1)