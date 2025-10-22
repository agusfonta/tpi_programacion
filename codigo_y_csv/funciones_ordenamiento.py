# ============================================
# FUNCIONES DE ORDENAMIENTO
# ============================================

def ordenar_paises_por(paises, reverse, tipo):
    ordenado = sorted(paises, key=lambda pais: pais[tipo], reverse=reverse)

    if tipo in ["nombre", "continente"]:
        for p in ordenado:
            print(f"· {p[tipo]}")

    if tipo in ["poblacion", "superficie"]:
        for p in ordenado:
            print(f"· {p["nombre"]}: {p[tipo]}")
