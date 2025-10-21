
# ============================================
# IMPORTACIONES
# ============================================
import csv
import funciones_validacion
from funciones_carga_datos import normalizar_texto

RUTA_ARCHIVO = "paises.csv"

# ============================================
# FUNCIONES DE EDITAR CSV
# ============================================

# ------- DE AGREGAR--------
def añadir(paises):
    dic_agregar = {} 

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

def pedir_datos_nuevo_pais(tipo, paises, metodo, dic=None):
    
    while True:
        dato = input(f"· Ingresa {tipo} del pais: ").strip()

        if tipo in ["poblacion", "superficie"]:
            if not funciones_validacion.validar_numero_entero(dato):
                continue  
            dato = int(dato) 
            break  

        if tipo in ["nombre","continente"]:
            if not funciones_validacion.validar_texto(dato):
                continue  
            dato = dato.capitalize()
            break

    if tipo == "nombre":
        if validar_pais_existe(dato, paises):
            if metodo == "agregar":
                print("- Pais existente")
                return False
            if metodo == "editar":
                for pais in paises:
                    if pais[tipo] == dato:
                        return True, pais
                
    dic[tipo] = dato
            

def validar_pais_existe(nombre, paises):
    for pais in paises:
        if nombre.lower() == pais["nombre"].lower():
            return True

# -------  DE EDITAR ----------

def editar_pais(tipo, pais):
    
    while True:
        dato = input(f"· [Dato anterior: {pais[tipo]}] Valor actualizado de {tipo.capitalize()}: ").strip()


        if tipo in ["poblacion", "superficie"]:
            if not funciones_validacion.validar_numero_entero(dato):
                continue  
            dato = int(dato) 
            break  

        if tipo in ["nombre","continente"]:
            if not funciones_validacion.validar_texto(dato):
                continue  
            dato = dato.capitalize()
            pais[tipo] = dato
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
        editar_pais("nombre", dic_pais)
        editar_pais("poblacion", dic_pais)
        editar_pais("superficie", dic_pais)
        editar_pais("continente", dic_pais)

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