# ============================================
# FUNCIONES DE ORDENAMIENTO
# ============================================

def ordenar_paises_por(paises, reverse, tipo):
    ordenado = sorted(paises, key=lambda pais: pais[tipo], reverse=reverse)
    for p in ordenado:
        print(f"· {p[tipo]}")
