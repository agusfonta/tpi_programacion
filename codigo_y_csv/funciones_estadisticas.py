# ============================================
# FUNCIONES DE ESTADÍSTICAS
# ============================================

def obtener_pais_mayor_poblacion(paises):
    """
    Recibe la lista de paises
    Retorna el pais con mayor poblacion 
    
    """
    pais_mayor =  max(paises, key=lambda p: p["poblacion"])
    return pais_mayor

def obtener_pais_menor_poblacion(paises):
    """
    Recibe la lista de paises
    Retorna el pais con menor poblacion 
    
    """
    pais_menor =  min(paises, key=lambda p: p["poblacion"])
    return pais_menor

def calcular_promedio_poblacion(paises):
    """
    Recibe la lista de paises
    Retorna el ppromedio de poblacion 
    
    """
    total = sum(p["poblacion"] for p in paises)
    promedio = total / len(paises)
    return promedio

def calcular_promedio_superficie(paises):
    """
    Recibe la lista de paises
    Retorna el ppromedio de superficie
    
    """
    total = sum(p["superficie"] for p in paises)
    superficie = total / len(paises)
    return superficie


def contar_paises_por_continente(paises):
    """
    Recibe la lista de paises y cuenta la cantidad de paises por continente
    Retorna una lista ordenada (asia, europa, oceania, africa, america) con las cantidades de paises de cada continente
    
    """
    asia = 0
    europa= 0
    oceania = 0
    africa = 0
    america = 0

    for p in paises:
        if p["continente"] == "Asia":
            asia += 1
        elif p["continente"] == "Europa":
            europa += 1
        elif p["continente"] == "Oceanía":
            oceania += 1
        elif p["continente"] == "África":
            africa += 1
        elif p["continente"] == "América":
            america += 1

        lista = [asia, europa, oceania, africa, america]
    
    return lista
