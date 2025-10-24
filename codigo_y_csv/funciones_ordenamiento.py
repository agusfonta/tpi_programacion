# ============================================
# FUNCIONES DE ORDENAMIENTO
# ============================================

def ordenar_paises_por(paises, reverse, key):
    ordenado = sorted(paises, key=lambda pais: pais[key], reverse=reverse)
    return ordenado


