# ============================================
# IMPORTACIONES
# ============================================

import funciones_carga_datos

# ============================================
# FUNCIONES DE BÚSQUEDA
# ============================================

def buscar_por_nombre(lista_paises, dato, key): 
    """ 
    Busqueda parcial o total por nombre o continente (str)
    - key = "nombre" o "continente" segun lo enviado
    - Texto ingresado - Ejemplo de dato (dato = Asia) o (dato = Argentina)
    - Retorno lista de paises que coinciden con el nombre

    """

    coincidencias = []
    dato_normalizado = funciones_carga_datos.normalizar_texto(dato) 
    for pais in lista_paises: 
        if dato_normalizado.lower() in pais[key].lower():
            coincidencias.append(pais) 
    if len(coincidencias)==0: 
        return f"- No hay paises encontrados con '{dato}'" 
    else: 
        return coincidencias 

    # Otra forma de escritura: coincidencias = [p for p in lista_paises if dato.lower() in p["nombre"].lower()]
#_______________________________________________________________________

def buscar_por_rango(min,max,paises,key): 
    """ 
    Busqueda por rango de numeros (int) 
    - min = numero minimo del rango
    - max = numero maximo del rango
    - key = "superficie" o "poblacion" segun lo enviado
    - paises = lista de todos los paises del csv
    - Retorno lista de paises encontrados entre ese rango

    """

    min = int(min)
    max = int(max)
    paises_encontrados = []
    for pais in paises:
        if min <= pais[key] <= max:
            paises_encontrados.append(pais) 
    if len(paises_encontrados)==0:
        return f"- No se encontraron paises entre '{min}' y '{max}'."

    return paises_encontrados 


