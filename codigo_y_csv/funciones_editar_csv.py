
# ============================================
# IMPORTACIONES
# ============================================
import csv
import funciones_validacion
import funciones_carga_datos

RUTA_ARCHIVO = "paises.csv"

# ============================================
# FUNCIONES DE EDITAR CSV
# ============================================

# ------- DE AGREGAR--------
def añadir(paises):
    dic_agregar = {} 

    """Pide nombre del pais. Si el nombre del pais ya esta en el csv muesta mensaje de que ya ha sido agregado y corta la ejecucion. 
    S el nombre NO esta, pide los otros datos y agrega el diccionario completo al csv"""

    if not pedir_datos_nuevo_pais("nombre",paises, "agregar", dic_agregar): 
        # Si al pedir el nombre, este se encuentra en el csv no se ejecuta el if. 
        # Si el nombre no existe en el csv, se ejecuta el if y comienza a pedir los otros datos del pais. 
        pedir_datos_nuevo_pais("poblacion",paises, "agregar", dic_agregar)
        pedir_datos_nuevo_pais("superficie",paises, "agregar",  dic_agregar)
        pedir_datos_nuevo_pais("continente",paises, "agregar", dic_agregar)
        
        try: #Se abre el archivo para agregar -> "a"
            with open(RUTA_ARCHIVO, "a", newline="", encoding="utf-8") as archivo:
                campos = ["nombre", "poblacion", "superficie", "continente"]
                escritor = csv.DictWriter(archivo, fieldnames=campos, delimiter=";")
                escritor.writerow(dic_agregar)
            
            paises.append(dic_agregar) #Agregamos el diccionario del nuevo pais al csv
            print(" - País agregado exitosamente")
            return True
                
        except FileNotFoundError:
            print("~"*50)
            print("  x Error: Archivo no encontrado.")
            print("~"*50)
            return False

def pedir_datos_nuevo_pais(key, paises, metodo, dic=None):
    # --- Parametros ---
    # key => puede recibir nombre, poblacion, superficie o continente. Maneja con que tipo de dato estaremos trabajando
    # metodo => recibe o agregar o editar. Es depende la funcion para lo que lo necesites. 
    # dic => Recibe el diccionario del paisa editar. Por defecto es None ya que en el caso de agregar no lo necesitariamos. 

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

def validar_pais_existe(nombre, paises): #Recorre la lista de paises y valida. Si ya esta dentro de ella devuelve True
    for pais in paises:
        if nombre.lower() == pais["nombre"].lower():
            return True

# -------  DE EDITAR ----------

def ingresar_nuevos_valores(key, pais):
    """ Modifica el valor de la key ingresada del pais ingresado. 
    Si la key es poblacion o superficie valida numero y si es nombre o continente valida texto"""
    
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


def editar(paises):
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