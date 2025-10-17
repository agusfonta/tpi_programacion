
# ============================================
# FUNCIONES DE BÚSQUEDA
# ============================================
#_______________________________________________________________________

def buscar_por_nombre(lista_paises, dato): #OPCION 1 DEL MENU 
    coincidencias = []
    print(f"\n· PAISES QUE COINCIDEN CON '{dato}' ")
    print("-"*39)
    for pais in lista_paises:
        if dato.lower() in pais["nombre"].lower():
            coincidencias.append(pais)
    if len(coincidencias)==0: print("- No hay paises encontrados con esas caracteristicas")
    for pais in coincidencias:
        for key, value in pais.items():
            print(f" {key.capitalize()} : {value}")
        print("-"*25)
    # Otra forma de escritura: coincidencias = [p for p in lista_paises if dato.lower() in p["nombre"].lower()]
#_______________________________________________________________________

def buscar_por_filtro(lista_paises, dato, filtro): #OPCION 2 DEL MENU 
    paises_encontrados = []
    for pais in lista_paises:
        if pais[filtro] == dato:
            paises_encontrados.append(pais["nombre"])
    for nombre in paises_encontrados: print(f"• {nombre}")
    if len(paises_encontrados)==0: print("- No hay paises encontrados con esas caracteristicas")
#_______________________________________________________________________

def buscar_por_rango(min,max,paises,tipo):
    print(f"- Paises con {tipo} entre {min} y {max}")
    min = int(min)
    max = int(max)
    paises_encontrados = []
    for pais in paises:
        if min <= pais[tipo] <= max:
            paises_encontrados.append(pais)
    if len(paises_encontrados)==0:
        print("- No se encontraron paises entre esos rangos.")
    return paises_encontrados