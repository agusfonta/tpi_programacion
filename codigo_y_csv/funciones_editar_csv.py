import csv
import funciones_validacion

RUTA_ARCHIVO = "paises.csv"


def verificar_y_reparar_csv():
    """
    Verifica que el CSV tenga el header correcto.
    Si no lo tiene, lo agrega.
    """
    try:
        with open(RUTA_ARCHIVO, 'r', encoding='utf-8') as f:
            primera_linea = f.readline().strip()
            
        # Si no tiene el header correcto, lo agregamos
        if primera_linea != "nombre;poblacion;superficie;continente":
            with open(RUTA_ARCHIVO, 'r', encoding='utf-8') as f:
                contenido = f.read()
            
            with open(RUTA_ARCHIVO, 'w', encoding='utf-8') as f:
                f.write("nombre;poblacion;superficie;continente\n")
                if contenido and not contenido.startswith("nombre;poblacion"):
                    f.write(contenido)
                    
    except FileNotFoundError:
        # Crear el archivo si no existe
        with open(RUTA_ARCHIVO, 'w', encoding='utf-8') as f:
            f.write("nombre;poblacion;superficie;continente\n")

def añadir(paises):
    """
    Agrega un nuevo país al CSV y a la lista en memoria.
    Retorna True si se agregó correctamente, False si ya existe o hubo error.
    """
    nombre = input("· Ingresa el nombre del pais: ").strip().capitalize()
    nombre = funciones_validacion.validar_texto(nombre)
    
    # Verificar si el país ya existe
    for pais in paises:
        if nombre.lower() == pais["nombre"].lower():
            print("~"*50)
            print("  x Error: El país ya existe en el sistema.")
            print("~"*50)
            return False
    
    # Crear el diccionario para el nuevo país
    dic_agregar = {}
    dic_agregar["nombre"] = nombre
    
    # Solicitar población
    while True:
        poblacion = input("· Ingresa la poblacion del pais: ")
        if funciones_validacion.validar_numero_entero(poblacion):
            dic_agregar["poblacion"] = int(poblacion)
            break
    
    # Solicitar superficie
    while True:
        superficie = input("· Ingresa la superficie del pais: ")
        if funciones_validacion.validar_numero_entero(superficie):
            dic_agregar["superficie"] = int(superficie)
            break
    
    # Solicitar continente
    continente = input("· Ingresa el continente del pais: ").strip().capitalize()
    continente = funciones_validacion.validar_texto(continente)
    dic_agregar["continente"] = continente
    
    try:
        # Verificar que el CSV esté correcto antes de agregar
        verificar_y_reparar_csv()
        
        # Agregar al archivo CSV (modo append, sin escribir header)
        with open(RUTA_ARCHIVO, "a", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos, delimiter=";")
            escritor.writerow(dic_agregar)
        
        # Agregar a la lista en memoria
        paises.append(dic_agregar)
        
        print("~"*50)
        print(f"  ✓ País '{nombre}' agregado exitosamente.")
        print("~"*50)
        return True
                
    except FileNotFoundError:
        print("~"*50)
        print("  x Error: Archivo no encontrado.")
        print("~"*50)
        return False
    except Exception as e:
        print("~"*50)
        print(f"  x Error al agregar el país: {e}")
        print("~"*50)
        return False


def editar(paises):
    """
    Edita un país existente en el CSV y en la lista en memoria.
    """
    nombre_buscar = input("· Ingresa el nombre del país a editar: ").strip().capitalize()
    
    # Buscar el país en la lista
    pais_encontrado = None
    for pais in paises:
        if nombre_buscar.lower() == pais["nombre"].lower():
            pais_encontrado = pais
            break
    
    if not pais_encontrado:
        print("~"*50)
        print(f"  x Error: No se encontró el país '{nombre_buscar}'.")
        print("~"*50)
        return False
    
    # Mostrar datos actuales
    print("-"*50)
    print("  Datos actuales del país:")
    for key, value in pais_encontrado.items():
        print(f"  {key.capitalize()}: {value}")
    print("-"*50)
    
    # Solicitar nuevos datos
    print("\n· Ingresa los nuevos datos (presiona Enter para mantener el valor actual):\n")
    
    nuevo_nombre = input(f"  Nombre [{pais_encontrado['nombre']}]: ").strip().capitalize()
    if nuevo_nombre:
        nuevo_nombre = funciones_validacion.validar_texto(nuevo_nombre)
    else:
        nuevo_nombre = pais_encontrado['nombre']
    
    nueva_poblacion = input(f"  Población [{pais_encontrado['poblacion']}]: ").strip()
    if nueva_poblacion:
        while not funciones_validacion.validar_numero_entero(nueva_poblacion):
            nueva_poblacion = input(f"  Población [{pais_encontrado['poblacion']}]: ").strip()
        nueva_poblacion = int(nueva_poblacion)
    else:
        nueva_poblacion = pais_encontrado['poblacion']
    
    nueva_superficie = input(f"  Superficie [{pais_encontrado['superficie']}]: ").strip()
    if nueva_superficie:
        while not funciones_validacion.validar_numero_entero(nueva_superficie):
            nueva_superficie = input(f"  Superficie [{pais_encontrado['superficie']}]: ").strip()
        nueva_superficie = int(nueva_superficie)
    else:
        nueva_superficie = pais_encontrado['superficie']
    
    nuevo_continente = input(f"  Continente [{pais_encontrado['continente']}]: ").strip().capitalize()
    if nuevo_continente:
        nuevo_continente = funciones_validacion.validar_texto(nuevo_continente)
    else:
        nuevo_continente = pais_encontrado['continente']
    
    try:
        # Actualizar en la lista en memoria
        pais_encontrado['nombre'] = nuevo_nombre
        pais_encontrado['poblacion'] = nueva_poblacion
        pais_encontrado['superficie'] = nueva_superficie
        pais_encontrado['continente'] = nuevo_continente
        
        # Reescribir todo el archivo CSV con los datos actualizados
        with open(RUTA_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos, delimiter=";")
            escritor.writeheader()
            escritor.writerows(paises)
        
        print("~"*50)
        print(f"  ✓ País '{nuevo_nombre}' editado exitosamente.")
        print("~"*50)
        return True
        
    except Exception as e:
        print("~"*50)
        print(f"  x Error al editar el país: {e}")
        print("~"*50)
        return False