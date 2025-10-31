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
    Retorna un diccionario con las cantidades de paises de cada continente
    
    """
    continentes = {"Asia": 0,"Europa": 0,"Oceania" : 0,"Africa" : 0,"America": 0,}

    for p in paises:
        if p["continente"] == "Asia":
            continentes["Asia"] += 1
            continue
        elif p["continente"] == "Europa":
            continentes["Europa"] += 1
            continue
        elif p["continente"] == "Oceania":
            continentes["Oceania"] += 1
            continue
        elif p["continente"] == "Africa":
            continentes["Africa"] += 1
            continue
        elif p["continente"] == "America":
            continentes["America"] += 1
            continue

    return continentes
