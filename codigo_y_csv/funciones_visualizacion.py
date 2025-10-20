# ============================================
# IMPORTACIONES
# ============================================
import funciones_estadisticas

# ============================================
# FUNCIONES DE VISUALIZACIÓN
# ============================================

def mostrar_estadisticas(paises):
    if not paises:
        print("- No hay datos para mostrar estadísticas.")
        return
# _________________________________________________________________________

    print(f" 1. Pais con mayor poblacion ")
    print("-"*50)
    pais_mayor = funciones_estadisticas.obtener_pais_mayor_poblacion(paises)
    for key,value in pais_mayor.items():
        print(f" {key.capitalize()} : {value}")
    print(" ")
# __________________________________________________________________________

    print("-"*50)
    print(f" 2. Pais con menor poblacion ")
    print("-"*50)
    pais_menor = funciones_estadisticas.obtener_pais_menor_poblacion(paises)
    for key,value in pais_menor.items():
        print(f" {key.capitalize()} : {value}")
    print(" ")
# ___________________________________________________________________________
    print("-"*50)
    print(f" 3. Promedio de poblacion ")
    print("-"*50)
    print(f" => {funciones_estadisticas.calcular_promedio_poblacion(paises):,}")
    print(" ")
# ___________________________________________________________________________

    print("-"*50)
    print(f"4. Promedio de superficie")
    print("-"*50)
    print(f" => {funciones_estadisticas.calcular_promedio_superficie(paises):,}")
    print(" ")
# ____________________________________________________________________________

    print("-"*50)
    print(f" 5. Paises por continente ")
    print("-"*50)
    asia, europa, oceania, africa, america = funciones_estadisticas.contar_paises_por_continente(paises)
    print(f"- Cantidad de paises de ASIA: {asia}")
    print(f"- Cantidad de paises de EUROPA: {europa}")
    print(f"- Cantidad de paises de OCEANIA: {oceania}")
    print(f"- Cantidad de paises de AFRICA: {africa}")
    print(f"- Cantidad de paises de AMERICA: {america}")
    print("-"*50)
