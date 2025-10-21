

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
    errores = []  # Lista para almacenar los errores
    linea_numero = 1  # Contador de líneas (empieza en 1, el header es línea 1)
    
    try:
        with open(RUTA, newline='', encoding="utf-8") as archivo:
            paises_csv = csv.DictReader(archivo, delimiter=";")
            
            for pais in paises_csv:
                linea_numero += 1
                errores_pais = []
                
                # Verificar que tenga exactamente 4 columnas
                if len(pais) != 4:
                    errores.append(f"Línea {linea_numero}: Número incorrecto de columnas ({len(pais)} en lugar de 4)")
                    continue
                
                # Limpiar espacios en blanco
                for clave in pais:
                    pais[clave] = pais[clave].strip()
                    if not pais[clave]: 
                        pais[clave] = ""
                
                # Verificar campos obligatorios
                if not pais.get("nombre"):
                    errores_pais.append("falta el nombre")
                
                if not pais.get("continente"):
                    errores_pais.append("falta la continente")
                
                # Verificar población
                if not pais.get("poblacion"):
                    errores_pais.append("falta la población")
                elif not pais['poblacion'].isnumeric():
                    errores_pais.append(f"población inválida ('{pais['poblacion']}')")
                
                # Verificar superficie
                if not pais.get("superficie"):
                    errores_pais.append("falta la superficie")
                elif not pais['superficie'].isnumeric():
                    errores_pais.append(f"superficie inválida ('{pais['superficie']}')")
                
                # Si hay errores en este país, registrarlos y continuar
                if errores_pais:
                    nombre_mostrar = pais.get("nombre", "[Sin nombre]")
                    errores.append(f"Línea {linea_numero} ({nombre_mostrar}): {', '.join(errores_pais)}")
                    continue
                
                # Normalizar texto
                nombre_pais = normalizar_texto(pais["nombre"])
                
                # Verificar duplicados
                if nombre_pais in paises_sin_repetir:
                    errores.append(f"Línea {linea_numero} ({pais['nombre']}): país duplicado")
                    continue
                
                paises_sin_repetir.add(nombre_pais)
                
                # Normalizar y convertir datos
                pais["nombre"] = nombre_pais
                pais['poblacion'] = int(pais['poblacion'])
                pais['superficie'] = int(pais['superficie'])
                pais["continente"] = normalizar_texto(pais["continente"])
                
                paises.append(pais)
        
        # Mostrar reporte de errores si los hay
        if errores:
            print("\n" + "="*70)
            print(" ⚠ REPORTE DE ERRORES EN LA CARGA DE DATOS")
            print("="*70)
            for error in errores:
                print(f" • {error}")
            print("="*70)
            print(f" Total de países cargados correctamente: {len(paises)}")
            print(f" Total de registros con errores: {len(errores)}")
            print("="*70 + "\n")
        else:
            print(f"\n✓ Todos los países ({len(paises)}) se cargaron correctamente.\n")
        
        return paises
        
    except FileNotFoundError:
        print("="*70)
        print(f" x ERROR CRÍTICO: El archivo '{RUTA}' no fue encontrado.")
        print(f" Verifica que el archivo exista en la ruta correcta.")
        print("="*70)
        exit(1)
    except Exception as e:
        print("="*70)
        print(f" x ERROR CRÍTICO: {type(e)._name_}")
        print(f" {str(e)}")
        print("="*70)
        exit(1)