# ============================================
# IMPORTACIONES
# ============================================
import funciones_estadisticas
import funciones_visualizacion
# ============================================
# FUNCIONES DE VISUALIZACIÓN
# ============================================

def mostrar_lista_al_usuario(lista_paises):
    """ Muestra la lista completa de paises al usuario"""
    for pais in lista_paises:
        for key, value in pais.items():
            print(f" {key.capitalize()} : {value}")
        print("-"*25)

def mostrar_ordenados(lista_ordenados, key):
    """
    Recibe una lista ordenada y la muestra segun la key 
    
    """
    if key in ["nombre", "continente"]:
        for p in lista_ordenados:
            print(f"· {p[key]}")

    if key in ["poblacion", "superficie"]:
        for p in lista_ordenados:
            print(f"· {p["nombre"]}: {p[key]}")

def mostrar_continentes(lista):
    """
    Recibe una lista de cantidad de paises por continentes y la muestra
    
    """

    continentes = ["Asia", "Europa", "Oceania", "Africa", "America"]
    
    for i in range(len(lista)):
        print(f"- Cantidad de paises de {continentes[i].upper}: {lista[i]}")
        print("-"*50)


def mostrar_estadisticas(paises):
    """
    Muestra las estadisticas de los paises recibidos 
    
    """
    print(f" 1. Pais con mayor poblacion ")
    print("-"*50)
    pais_mayor = funciones_estadisticas.obtener_pais_mayor_poblacion(paises)
    print(f" {pais_mayor["nombre"]}")
    print(" ")

    print("-"*50)
    print(f" 2. Pais con menor poblacion ")
    print("-"*50)
    pais_menor = funciones_estadisticas.obtener_pais_menor_poblacion(paises)
    print(f" {pais_menor["nombre"]}")
    print(" ")

    print("-"*50)
    print(f" 3. Promedio de poblacion ")
    print("-"*50)
    promedio_poblacion = funciones_estadisticas.calcular_promedio_poblacion(paises)
    print(f"=> {promedio_poblacion}")

    print("-"*50)
    print(f" 4. Promedio de superficie ")
    print("-"*50)
    promedio_superficie = funciones_estadisticas.calcular_promedio_superficie(paises)
    print(f"=> {promedio_superficie}")

    print("-"*50)
    print(f" 5. Paises por continente ")
    print("-"*50)
    paises_por_continente = funciones_estadisticas.contar_paises_por_continente(paises)
    funciones_visualizacion.mostrar_continentes(paises_por_continente)
