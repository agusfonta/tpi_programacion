import csv

RUTA = "paises.csv"

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

texto = input("Ingresa: ")
validar_texto(texto)


