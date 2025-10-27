
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
    dic_agregar = {} 

    """
    Recibe la lista de los diccionarios de los paises.

    La funcion añade un pais nuevo con todos los datos completos al CSV. 

    Pide nombre del pais. Si el nombre del pais ya esta en el csv muesta mensaje de que ya ha sido agregado y corta la ejecucion. 
    Si el nombre NO esta, pide los otros datos y agrega el diccionario completo del pais nuevo al csv.

    """

    if not pedir_datos_nuevo_pais("nombre",paises, "agregar", dic_agregar): 
        pedir_datos_nuevo_pais("poblacion",paises, "agregar", dic_agregar)
        pedir_datos_nuevo_pais("superficie",paises, "agregar",  dic_agregar)
        pedir_datos_nuevo_pais("continente",paises, "agregar", dic_agregar)
        
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

def pedir_datos_nuevo_pais(key, paises, metodo, dic=None):
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
                return False
            if metodo == "editar":
                for pais in paises:
                    if pais[key] == dato:
                        return True, pais
                
    dic[key] = dato

def validar_pais_existe(nombre, paises): 
    """
    Recibe el nombre del pais y la lista de diccionarios de paises
    Recorre la lista de paises y valida. Si ya esta dentro de ella devuelve True

    """
    for pais in paises:
        if nombre.lower() == pais["nombre"].lower():
            return True

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

    booleano, dic_pais = pedir_datos_nuevo_pais("nombre", paises, "editar")

    print("-"*50)
    print(f"· Datos actuales de {dic_pais["nombre"].capitalize()}")
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
        print(f"· Datos ACTUALIZADOS de {dic_pais["nombre"].capitalize()}")
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