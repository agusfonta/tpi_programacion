# ============================================
# FUNCIONES DE ORDENAMIENTO
# ============================================

def ordenar_paises_por(paises, reverse, key):

    """ 
    Recibe
    - key = poblacion, superficie o nombre 
    - reverse = True o False
    - paises= lista de los paises

    Ordena paises por el valor de la key ingresado en el sentido ingresado del reverse 
    
    Retorna la lista de paises ordenados
    
    """
    ordenado = sorted(paises, key=lambda pais: pais[key], reverse=reverse)
    return ordenado


