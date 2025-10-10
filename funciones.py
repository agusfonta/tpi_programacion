
# ============================================
# IMPORTACIONES
# ============================================
import csv
RUTA_ARCHIVO = "paises.csv"

# ============================================
# FUNCIONES DE CARGA DE DATOS
# ============================================

def crear_lista_de_dicccionarios_de_paises(RUTA):
    datos = []  # Lista de diccionarios de paises
    try:
        with open(RUTA, newline='', encoding="utf-8") as archivo:
            paises = csv.DictReader(archivo, delimiter=";")
            for fila in paises:
                fila['poblacion'] = fila['poblacion']
                fila['superficie'] = fila['superficie']
                datos.append(fila)
        
        return datos
    except FileNotFoundError:
        print(f"Error: El archivo '{RUTA}' no fue encontrado.")
        return []
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []


# ============================================
# FUNCIONES DE BÚSQUEDA
# ============================================

def buscar_por_nombre(list_dict_paises, dato): #OPCION 1 DEL MENU 

    """ Ejemplo guia: 

    list_dict_paises = diccionario
    dato =  China
    filtro = nombre """

    for pais in list_dict_paises:
        if pais["nombre"] == dato:
            dic_pais_encontrado = pais
            break

    for caracteristica,dato in dic_pais_encontrado.items():
        print(caracteristica.capitalize() ,": ",dato)


def buscar_por_filtro(list_dict_paises, dato, filtro): #OPCION 2 DEL MENU 

    paises_encontrados = []

    for pais in list_dict_paises:
        if pais[filtro] == dato:
            paises_encontrados.append(pais["nombre"])
    print(paises_encontrados)

# ============================================
# FUNCIONES DE FILTRADO
# ============================================

def filtrar_por_continente(paises, continente):
    """
    Filtra países por continente.
    
    Parámetros:
        paises (list): lista de diccionarios de países
        continente (str): nombre del continente
    
    Retorna:
        list: países del continente especificado
    """
    filtrados = []
    # TODO: Implementar filtro por continente
    return filtrados


def filtrar_por_rango_poblacion(paises, min_poblacion, max_poblacion):
    """
    Filtra países por rango de población.
    
    Parámetros:
        paises (list): lista de diccionarios de países
        min_poblacion (int): población mínima
        max_poblacion (int): población máxima
    
    Retorna:
        list: países dentro del rango de población
    """
    filtrados = []
    # TODO: Implementar filtro por población
    return filtrados


def filtrar_por_rango_superficie(paises, min_superficie, max_superficie):
    """
    Filtra países por rango de superficie.
    
    Parámetros:
        paises (list): lista de diccionarios de países
        min_superficie (int): superficie mínima en km²
        max_superficie (int): superficie máxima en km²
    
    Retorna:
        list: países dentro del rango de superficie
    """
    filtrados = []
    # TODO: Implementar filtro por superficie
    return filtrados


# ============================================
# FUNCIONES DE ORDENAMIENTO
# ============================================

def ordenar_por_nombre(paises, ascendente=True):
    """
    Ordena países alfabéticamente por nombre.
    
    Parámetros:
        paises (list): lista de diccionarios de países
        ascendente (bool): True para A-Z, False para Z-A
    
    Retorna:
        list: lista ordenada de países
    """
    # TODO: Implementar ordenamiento por nombre
    # Usar sorted() con key y reverse
    return paises


def ordenar_por_poblacion(paises, ascendente=True):
    """
    Ordena países por población.
    
    Parámetros:
        paises (list): lista de diccionarios de países
        ascendente (bool): True para menor a mayor, False para mayor a menor
    
    Retorna:
        list: lista ordenada de países
    """
    # TODO: Implementar ordenamiento por población
    return paises


def ordenar_por_superficie(paises, ascendente=True):
    """
    Ordena países por superficie.
    
    Parámetros:
        paises (list): lista de diccionarios de países
        ascendente (bool): True para menor a mayor, False para mayor a menor
    
    Retorna:
        list: lista ordenada de países
    """
    # TODO: Implementar ordenamiento por superficie
    return paises


# ============================================
# FUNCIONES DE ESTADÍSTICAS
# ============================================

def obtener_pais_mayor_poblacion(paises):
    """
    Encuentra el país con mayor población.
    
    Parámetros:
        paises (list): lista de diccionarios de países
    
    Retorna:
        dict: país con mayor población
    """
    # TODO: Implementar búsqueda del país con mayor población
    # Usar max() con key
    pass


def obtener_pais_menor_poblacion(paises):
    """
    Encuentra el país con menor población.
    
    Parámetros:
        paises (list): lista de diccionarios de países
    
    Retorna:
        dict: país con menor población
    """
    # TODO: Implementar búsqueda del país con menor población
    pass


def calcular_promedio_poblacion(paises):
    """
    Calcula el promedio de población de los países.
    
    Parámetros:
        paises (list): lista de diccionarios de países
    
    Retorna:
        float: promedio de población
    """
    # TODO: Implementar cálculo de promedio
    # Sumar todas las poblaciones y dividir por cantidad
    pass


def calcular_promedio_superficie(paises):
    """
    Calcula el promedio de superficie de los países.
    
    Parámetros:
        paises (list): lista de diccionarios de países
    
    Retorna:
        float: promedio de superficie
    """
    # TODO: Implementar cálculo de promedio
    pass


def contar_paises_por_continente(paises):
    """
    Cuenta la cantidad de países por continente.
    
    Parámetros:
        paises (list): lista de diccionarios de países
    
    Retorna:
        dict: diccionario con continente como clave y cantidad como valor
    """
    conteo = {}
    # TODO: Implementar conteo por continente
    # - Recorrer países
    # - Si el continente no existe en el diccionario, agregarlo con valor 1
    # - Si existe, incrementar el contador
    return conteo


# ============================================
# FUNCIONES DE VISUALIZACIÓN
# ============================================

def mostrar_paises(paises):
    """
    Muestra la lista de países en formato legible.
    
    Parámetros:
        paises (list): lista de diccionarios de países
    """
    if not paises:
        print("No hay países para mostrar.")
        return
    
    print("\n" + "="*80)
    print(f"{'NOMBRE':<30} {'POBLACIÓN':<15} {'SUPERFICIE':<15} {'CONTINENTE':<15}")
    print("="*80)
    
    for pais in paises:
        # TODO: Formatear y mostrar cada país
        pass
    
    print("="*80)
    print(f"Total: {len(paises)} países\n")


def mostrar_estadisticas(paises):
    """
    Muestra las estadísticas generales de los países.
    
    Parámetros:
        paises (list): lista de diccionarios de países
    """
    if not paises:
        print("No hay datos para mostrar estadísticas.")
        return
    
    print("\n" + "="*50)
    print("ESTADÍSTICAS GENERALES")
    print("="*50)
    
    # TODO: Llamar a las funciones de estadísticas y mostrar resultados
    # - País con mayor población
    # - País con menor población
    # - Promedio de población
    # - Promedio de superficie
    # - Cantidad de países por continente
    
    print("="*50 + "\n")


# ============================================
# FUNCIONES DE VALIDACIÓN
# ============================================

def validar_numero_entero(numero):
    try:
        if not (numero.isdigit()):
            raise ValueError
        return True
    
    except ValueError:
        print("Error: Debe ingresar un número entero válido, sin coma (,) ni punto (.).")


def validar_opcion_menu(min_opcion, max_opcion):
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if min_opcion <= opcion <= max_opcion:
                return opcion
            else:
                print(f"Error: Ingrese un número entre {min_opcion} y {max_opcion}")
        except ValueError:
            print("Error: Debe ingresar un número válido.")

def validar_texto(texto):
    try:
        if len(texto) == 0:
            raise ValueError("Campo vacio. Por favor ingrese una palabra")
        
        if not texto.isalpha():
            raise ValueError("Por favor ingrese una palabra")

        return True

    except ValueError as e:
        print("Error: ", e)
        return False

# ============================================
# FUNCIONES DE MENÚS
# ============================================

def mostrar_menu_principal():
    """
    Muestra el menú principal del sistema.
    """
    print("\n" + "="*20)
    print("SISTEMA DE GESTIÓN DE PAÍSES")
    print("="*20)
    print("1. Buscar país por nombre")
    print("2. Filtrar países")
    print("3. Ordenar países")
    print("4. Mostrar estadísticas")
    print("0. Salir")
    print("="*20)


def menu_filtros(paises):
    while True:
        print("\n--- FILTRAR PAÍSES ---")
        print("1. Por continente")
        print("2. Por rango de población")
        print("3. Por rango de superficie")
        print("0. Volver al menú principal")
        
        opcion = validar_opcion_menu(0, 3)
        

        if opcion == 1:
            continente = input("Ingrese el continente: ").capitalize()
            filtro = "continente"
            valido = validar_texto(continente)
            if valido:
                buscar_por_filtro(paises, continente, filtro)
            else:
                None


        elif opcion == 2:
            poblacion = input("Ingrese la poblacion: ")
            filtro = "poblacion"
            valido = validar_numero_entero(poblacion)
            if valido:
                buscar_por_filtro(paises, poblacion, filtro)
            else:
                None

        elif opcion == 3:
            superficie = input("Ingrese la superficie: ")
            filtro = "superficie"
            valido = validar_numero_entero(superficie)
            if valido:
                buscar_por_filtro(paises, superficie, filtro)
            else:
                None
    
        elif opcion == 0:
            break


def menu_ordenamiento(paises):
    """
    Submenú para ordenar países.
    
    Parámetros:
        paises (list): lista de diccionarios de países
    """
    while True:
        print("\n--- ORDENAR PAÍSES ---")
        print("1. Por nombre (A-Z)")
        print("2. Por población (menor a mayor)")
        print("3. Por superficie (menor a mayor)")
        print("4. Por superficie (mayor a menor)")
        print("0. Volver al menú principal")
        
        opcion = validar_opcion_menu(0, 4)
        
        if opcion == 1:
            """
            from operator import itemgetter

            personas = [
                {'nombre': 'Ana', 'edad': 23},
                {'nombre': 'Juan', 'edad': 30},
                {'nombre': 'Lucía', 'edad': 28}
            ]

            # Ordenar por la clave 'edad'
            personas.sort(key=itemgetter('edad'))
            print(personas)
            
            
            
            """

        elif opcion == 2:
            # TODO: Ordenar por nombre descendente
            pass
        elif opcion == 3:
            # TODO: Ordenar por población ascendente
            pass
        elif opcion == 4:
            # TODO: Ordenar por población descendente
            pass
        elif opcion == 5:
            # TODO: Ordenar por superficie ascendente
            pass
        elif opcion == 6:
            # TODO: Ordenar por superficie descendente
            pass
        elif opcion == 0:
            break

