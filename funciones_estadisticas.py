# ============================================
# IMPORTACIONES
# ============================================
from statistics import median
RUTA_ARCHIVO = "paises.csv"
# ============================================
# FUNCIONES DE ESTADÍSTICAS
# ============================================

def obtener_pais_mayor_poblacion(paises):
    pais_mayor =  max(paises, key=lambda p: p["poblacion"])
    return pais_mayor

def obtener_pais_menor_poblacion(paises):
    pais_menor =  min(paises, key=lambda p: p["poblacion"])
    return pais_menor

def calcular_promedio_poblacion(paises):
    total = sum(p["poblacion"] for p in paises)
    promedio = total / len(paises)
    return promedio

def calcular_promedio_superficie(paises):
    total = sum(p["superficie"] for p in paises)
    superficie = total / len(paises)
    return superficie


def contar_paises_por_continente(paises):
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
    
    return asia, europa, oceania, africa, america
