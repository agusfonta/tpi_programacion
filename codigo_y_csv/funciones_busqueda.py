import funciones_carga_datos
# ============================================
# FUNCIONES DE BÚSQUEDA
# ============================================

def buscar_por_nombre(lista_paises, dato, key): # Busqueda parcial o total por nombre o continente (str)
    # key = "nombre" o "continente" segun lo enviado
    # Texto ingresado - Ejemplo de dato (dato = Asia) o (dato = Argentina)
    coincidencias = []
    dato_normalizado = funciones_carga_datos.normalizar_texto(dato) # Normalizamos el dato, queda sin tildes
    for pais in lista_paises: # Recorremos la lista de diccionarios
        if dato_normalizado.lower() in pais[key].lower():
            coincidencias.append(pais) #Si el dato coincide parcial o totalmente se agrega a la lista de coincidencias
    if len(coincidencias)==0: 
        return f"- No hay paises encontrados con '{dato}'" #Si no encuentra ningun pais
    else: 
        return coincidencias #Retorna lista de paises que coincidieron

    # Otra forma de escritura: coincidencias = [p for p in lista_paises if dato.lower() in p["nombre"].lower()]
#_______________________________________________________________________

def buscar_por_rango(min,max,paises,key): # Busqueda por superficie o poblacion (int)
    # key = "superficie" o "poblacion" segun lo enviado
    min = int(min)
    max = int(max)
    paises_encontrados = []
    for pais in paises:
        if min <= pais[key] <= max:
            paises_encontrados.append(pais) #Agregar a la lista paises encontrados entre el rango 
    if len(paises_encontrados)==0:
        return f"- No se encontraron paises entre '{min}' y '{max}'."

    return paises_encontrados #Retorna lista de paises encontrados entre ese rango


