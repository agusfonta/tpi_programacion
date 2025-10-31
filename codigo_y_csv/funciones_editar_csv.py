# ============================================
# IMPORTACIONES
# ============================================
import csv
import funciones_validacion

RUTA_ARCHIVO = "paises.csv"

# ============================================
# FUNCIONES DE EDITAR CSV
# ============================================

# ------- DE AGREGAR--------
def añadir_pais(paises):
    """
    Recibe la lista de los diccionarios de los paises.

    La funcion añade un pais nuevo con todos los datos completos al CSV. 

    Pide nombre del pais. Si el nombre del pais ya esta en el csv muesta mensaje de que ya ha sido agregado y corta la ejecucion. 
    Si el nombre NO esta, pide los otros datos y agrega el diccionario completo del pais nuevo al csv.

    """
    dic_agregar = {} 

    booleano, nombre = pedir_datos_nuevo_pais("nombre", paises, "agregar")

    if booleano: 
        dic_agregar["nombre"] = nombre
        poblacion = pedir_datos_nuevo_pais("poblacion",paises, "agregar")
        dic_agregar["poblacion"] = poblacion 
        superficie = pedir_datos_nuevo_pais("superficie",paises, "agregar")
        dic_agregar["superficie"] = superficie
        continente = pedir_datos_nuevo_pais("continente",paises, "agregar")
        dic_agregar["continente"] = continente 
        
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
    # CAMBIO 1: Agregado return False cuando el país ya existe
    else:
        return False

def pedir_datos_nuevo_pais(key, paises, metodo):
    """ 
    Pide los datos del pais nuevo al usuario. Si lo usamos para agregar, crea el diccionario y si es para editar, edita el pais elegido. 

    key => puede recibir nombre, poblacion, superficie o continente. Maneja con que tipo de dato estaremos trabajando
    metodo => recibe o agregar o editar. Es depende la funcion para lo que lo necesites. 
    dic => Recibe el diccionario del pais en caso de querer editar. Por defecto es None ya que en el caso de agregar no lo necesitariamos.
    paises => lista de diccionario de paises  

    Si el metodo ingresado es agregar - suma un diccionario a la lista original y se actualiza el csv
    Si el metodo ingresado es editar - retorna el diccionario del pais con los datos editados

    """

    while True:
        dato = input(f"· Ingresa {key} del pais: ").strip()

        if key in ["poblacion", "superficie"]:
            if not funciones_validacion.validar_numero_entero(dato):
                continue  
            dato = int(dato) 
            break  

        if key in ["nombre","continente"]:
            if not funciones_validacion.validar_texto(dato):
                continue  
            dato = dato.capitalize()
            break

    if key == "nombre":
        if validar_pais_existe(dato, paises):
            if metodo == "agregar":
                print("- Pais existente")
                return False, dato
            elif metodo == "editar":
                for pais in paises:
                    if pais[key] == dato:
                        return True, pais
        else:
            if metodo == "agregar":
                return True, dato
            # CAMBIO: Agregado manejo cuando el país NO existe en modo editar
            elif metodo == "editar":
                return False, None  # Retorna False y None para indicar que no existe
    
    return dato

def validar_pais_existe(nombre, paises): 
    """
    Recibe el nombre del pais y la lista de diccionarios de paises
    Recorre la lista de paises y valida. Si ya esta dentro de ella devuelve True

    """
    for pais in paises:
        if nombre.lower() == pais["nombre"].lower():
            return True
        # CAMBIO 5: ELIMINADO else: return False
    # CAMBIO 6: Agregado return False FUERA del bucle
    return False

# -------  DE EDITAR ----------

def ingresar_nuevos_valores(key, pais):
    """ 
    Recibe:
    - key -> puede ser poblacion, superficie nombre o continente
    - pais -> nombre del pais a editar

    Modifica el valor de la key ingresada del pais ingresado. 
    Si la key es poblacion o superficie valida numero y si es nombre o continente valida texto
    
    """
    
    while True:
        dato = input(f"· [Dato anterior: {pais[key]}] Valor actualizado de {key.capitalize()}: ").strip()

        if key in ["poblacion", "superficie"]:
            if not funciones_validacion.validar_numero_entero(dato):
                continue  
            dato = int(dato)
            # CAMBIO 7: Agregada asignación del dato al diccionario
            pais[key] = dato
            break  

        if key in ["nombre","continente"]:
            if not funciones_validacion.validar_texto(dato):
                continue  
            dato = dato.capitalize()
            pais[key] = dato
            break


def editar_pais(paises):
    """
    Funcion principal para editar pais. Muestra datos viejos y actualizados del pais. 
    Sobre escribe el diccionario del pais con los datos nuevos en el csv 
    
    """

    # CAMBIO: Capturar el resultado de pedir_datos_nuevo_pais
    resultado = pedir_datos_nuevo_pais("nombre", paises, "editar")
    
    # CAMBIO: Verificar si resultado es una tupla válida
    if resultado is None or (isinstance(resultado, tuple) and not resultado[0]):
        print("~"*50)
        print("  x Error: País no existente")
        print("~"*50)
        return False
    
    booleano, dic_pais = resultado

    print("-"*50)
    print(f"· Datos actuales de {dic_pais['nombre'].capitalize()}")
    for key, value in dic_pais.items():
        print(f"  {key.capitalize()}: {value}")
    print("-"*50)
    print(" · Ingresa los nuevos datos:")

    if booleano: 
        ingresar_nuevos_valores("nombre", dic_pais)
        ingresar_nuevos_valores("poblacion", dic_pais)
        ingresar_nuevos_valores("superficie", dic_pais)
        ingresar_nuevos_valores("continente", dic_pais)

        print("-"*50)
        print(f"· Datos ACTUALIZADOS")
        for key, value in dic_pais.items():
            print(f"  {key.capitalize()}: {value}")
        print("-"*50)

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