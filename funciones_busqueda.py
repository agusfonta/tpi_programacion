# ============================================
# IMPORTACIONES
# ============================================
RUTA_ARCHIVO = "paises.csv"
# ============================================
# FUNCIONES DE BÚSQUEDA
# ============================================

def buscar_por_nombre(list_dict_paises, dato): #OPCION 1 DEL MENU 

    coincidencias = []

    print("=" *45)
    print(f"Busqueda de paises que coinciden con '{dato}'")
    print("=" *45)

    for pais in list_dict_paises:
        if dato.lower() in pais["nombre"].lower():
            coincidencias.append(pais)


    for pais in coincidencias:
        for key, value in pais.items():
            print(key.capitalize(),": ",value)
            
        print("-----------------------")


def buscar_por_filtro(list_dict_paises, dato, filtro): #OPCION 2 DEL MENU 

    paises_encontrados = []

    for pais in list_dict_paises:
        if pais[filtro] == dato:
            paises_encontrados.append(pais["nombre"])
    print(paises_encontrados)

def buscar_por_rango(min,max,paises,tipo):

    print(f"- Paises con {tipo} entre {min} y {max}")
    min = int(min)
    max = int(max)
    paises_encontrados = []
    for pais in paises:
        if min <= pais[tipo] <= max:
            paises_encontrados.append(pais)
    if len(paises_encontrados)==0:
        print("No se encontraron paises entre esos rangos.")
    return paises_encontrados