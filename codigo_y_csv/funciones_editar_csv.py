
# ============================================
# IMPORTACIONES
# ============================================
import csv
import funciones_validacion
from funciones_carga_datos import normalizar_texto

RUTA_ARCHIVO = "paises.csv"


# TODO ARREGLAR ERRORES DE VALIDACION EN FUNCION AÑADIR Y ELIMINAR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ============================================
# FUNCIONES DE CARGA DE DATOS
# ============================================

def añadir(paises):
    nombre = input("· Ingresa el nombre del pais: ")
    nombre = funciones_validacion.validar_texto(nombre)
    nombre = normalizar_texto(nombre)

    for pais in paises:
        if nombre.lower() == pais["nombre"].lower():
            print("- Pais existente")
            return False

    dic_agregar = {} 
    dic_agregar["nombre"] = nombre

    poblacion = input("· Ingresa la poblacion del pais: ")

    while not poblacion or not funciones_validacion.validar_numero_entero(poblacion): 
        poblacion = input(f"  Ingrese nuevamente la población: ")
    dic_agregar["poblacion"] = int(poblacion)

    superficie = input("· Ingresa la superficie del pais: ")
    
    while not superficie or not funciones_validacion.validar_numero_entero(superficie):  
        superficie = input(f"  Ingrese nuevamente la superficie: ")
    dic_agregar["superficie"] = int(superficie)

    continente = input("· Ingresa el continente del pais: ")
    
    while not continente or not funciones_validacion.validar_texto(continente):
        continente = input(f"  Ingrese nuevamente el continente: ")
    dic_agregar["continente"] = normalizar_texto(continente)

    try:
        with open(RUTA_ARCHIVO, "a", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos, delimiter=";")
            escritor.writerow(dic_agregar)
        
        paises.append(dic_agregar) 
        print(" - País agregado exitosamente")
        return True
            
    except FileNotFoundError:
        print("~"*50)
        print("  x Error: Archivo no encontrado.")
        print("~"*50)
        return False

def editar(paises):
    nombre_buscar = input("· Ingresa el nombre del país a editar: ")
    nombre_buscar = funciones_validacion.validar_texto(nombre_buscar)
    nombre_buscar = normalizar_texto(nombre_buscar)
    
    pais_encontrado = None
    for pais in paises:
        if nombre_buscar.lower() == pais["nombre"].lower():
            pais_encontrado = pais
            break
    
    if not pais_encontrado:
        print("- País no encontrado")
        return False
    
    print("-"*50)
    print(f"· Datos actuales de {pais_encontrado["nombre"].capitalize()}")
    for key, value in pais_encontrado.items():
        print(f"  {key.capitalize()}: {value}")
    print("-"*50)
    print(" · Ingresa los nuevos datos:")
    
    nuevo_nombre = input(f"  Nombre [{pais_encontrado['nombre']}]: ")
    if nuevo_nombre:
        nuevo_nombre = funciones_validacion.validar_texto(nuevo_nombre)
        pais_encontrado['nombre'] = normalizar_texto(nuevo_nombre)
    
    nueva_poblacion = input(f"  Población [{pais_encontrado['poblacion']}]: ")
    if nueva_poblacion:
        while not nueva_poblacion or not funciones_validacion.validar_numero_entero(nueva_poblacion):  # AGREGADO while
            nueva_poblacion = input(f"  Población: ")
        pais_encontrado['poblacion'] = int(nueva_poblacion)
    
    nueva_superficie = input(f"  Superficie [{pais_encontrado['superficie']}]: ")
    if nueva_superficie:
        while not nueva_superficie or not funciones_validacion.validar_numero_entero(nueva_superficie):  # AGREGADO while
            nueva_superficie = input(f"  Superficie: ")
        pais_encontrado['superficie'] = int(nueva_superficie)
    
    nuevo_continente = input(f"  Continente [{pais_encontrado['continente']}]: ")
    if nuevo_continente:
        while not nuevo_continente or not funciones_validacion.validar_texto(nuevo_continente):
            nuevo_continente = input(f"  Continente: ")
        pais_encontrado['continente'] = normalizar_texto(nuevo_continente)
    
    try:
        with open(RUTA_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos, delimiter=";")
            escritor.writeheader()
            escritor.writerows(paises)
        
        print(" - País editado exitosamente")
        return True
        
    except FileNotFoundError:
        print("~"*50)
        print("  x Error: Archivo no encontrado.")
        print("~"*50)
        return False