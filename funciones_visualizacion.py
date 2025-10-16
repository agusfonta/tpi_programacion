# ============================================
# IMPORTACIONES
# ============================================
import funciones_estadisticas

# ============================================
# FUNCIONES DE VISUALIZACIÓN
# ============================================

def mostrar_estadisticas(paises):
    if not paises:
        print("No hay datos para mostrar estadísticas.")
        return
    
    print("\n" + "="*36)
    print(" "*7 + "ESTADÍSTICAS GENERALES" + " "*7)
    print("="*36)
# =======================================================================
    print("  --- Pais con mayor poblacion ---   ")
    pais_mayor = funciones_estadisticas.obtener_pais_mayor_poblacion(paises)
    for key,value in pais_mayor.items():
        print(f"{key.capitalize()} : {value}")
    print(" ")
# =======================================================================
    print("  --- Pais con menor poblacion ---   ")
    pais_menor = funciones_estadisticas.obtener_pais_menor_poblacion(paises)
    for key,value in pais_menor.items():
        print(f"{key.capitalize()} : {value}")
    print(" ")
# =======================================================================
    print("  ---- Promedio poblacion ----   ")
    print(f" => {funciones_estadisticas.calcular_promedio_poblacion(paises):,}")
    print(" ")
# =======================================================================
    print("  ---- Promedio superficie ----   ")
    print(f" => {funciones_estadisticas.calcular_promedio_superficie(paises):,}")
    print(" ")
# =======================================================================
    print("  ---- Paises por continente ----  ")
    asia, europa, oceania, africa, america = funciones_estadisticas.contar_paises_por_continente(paises)
    print(f"- Cantidad de paises de ASIA: {asia}")
    print(f"- Cantidad de paises de EUROPA: {europa}")
    print(f"- Cantidad de paises de OCEANIA: {oceania}")
    print(f"- Cantidad de paises de AFRICA: {africa}")
    print(f"- Cantidad de paises de AMERICA: {america}")
    print("="*20 + "\n")
