import funciones_carga_datos
# ============================================
# FUNCIONES DE BÚSQUEDA
# ============================================

def buscar_por_nombre(lista_paises, dato, tipo): #OPCION 1 DEL MENU 
    coincidencias = []
    print(" ")
    print(f"· Paises que coinciden con '{dato}' ")
    print("-"*50)
    dato_normalizado = funciones_carga_datos.normalizar_texto(dato)
    for pais in lista_paises:
        if dato_normalizado.lower() in pais[tipo].lower():
            coincidencias.append(pais)
    if len(coincidencias)==0: print(f"- No hay paises encontrados con '{dato}'")
    for pais in coincidencias:
        for key, value in pais.items():
            print(f" {key.capitalize()} : {value}")
        print("-"*25)
    # Otra forma de escritura: coincidencias = [p for p in lista_paises if dato.lower() in p["nombre"].lower()]
#_______________________________________________________________________

def buscar_por_rango(min,max,paises,tipo):
    print(" ")
    print(f"· Paises con '{tipo}' entre '{min}' y '{max}' ")
    print("-"*50)
    min = int(min)
    max = int(max)
    paises_encontrados = []
    for pais in paises:
        if min <= pais[tipo] <= max:
            paises_encontrados.append(pais)
    if len(paises_encontrados)==0:
        print(f"- No se encontraron paises entre '{min}' y '{max}'.")
    else:
        for pais in paises_encontrados:
            print(f"· {pais["nombre"].capitalize()} : {pais[tipo]}")
    
