# 🌍 Sistema de Gestión de Países

**Trabajo Práctico Integrador - Programación 1**  
Tecnicatura Universitaria en Programación

---

## 📋 Descripción

Sistema de gestión de información de países desarrollado en Python que permite realizar búsquedas, filtros, ordenamientos y generar estadísticas a partir de un dataset almacenado en formato CSV. El proyecto aplica conceptos fundamentales de programación como listas, diccionarios, funciones, estructuras condicionales y manejo de archivos.

---

## ✨ Características Principales

### 🔍 Búsqueda

- Búsqueda de países por nombre (coincidencia parcial)
- Resultados detallados con toda la información del país

### 🎯 Filtros

- **Por continente**: Filtra países según su ubicación geográfica
- **Por rango de población**: Encuentra países dentro de un rango poblacional específico
- **Por rango de superficie**: Filtra países por extensión territorial

### 📊 Ordenamiento

- Nombre (A-Z / Z-A)
- Población (menor a mayor / mayor a menor)
- Superficie (menor a mayor / mayor a menor)

### 📈 Estadísticas

- País con mayor población
- País con menor población
- Promedio de población mundial
- Promedio de superficie territorial
- Cantidad de países por continente

---

## 🗂️ Estructura del Proyecto

```
tpi_programacion/
│
├── paises.csv                      # Dataset con información de países
├── paises_sistema.py               # Programa principal
├── funciones_busqueda.py           # Funciones de búsqueda y filtrado
├── funciones_carga_datos.py        # Carga y validación del CSV
├── funciones_estadisticas.py       # Cálculos estadísticos
├── funciones_menu.py               # Menús del sistema
├── funciones_ordenamiento.py       # Funciones de ordenamiento
├── funciones_validacion.py         # Validaciones de entrada
└── funciones_visualizacion.py      # Presentación de resultados
```

---

## 🚀 Requisitos

- **Python 3.10+**
- **Módulos estándar de Python:**
  - `csv` (lectura de archivos)
  - `statistics` (cálculos estadísticos)

⚡ No requiere instalación de librerías externas.

---

## 💻 Instalación y Uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/sistema-gestion-paises.git
cd sistema-gestion-paises
```

### 2. Verificar el archivo CSV

Asegúrate de que `paises.csv` esté en el mismo directorio que `paises_sistema.py`.

### 3. Ejecutar el programa

```bash
python paises_sistema.py
```

---

## 📝 Formato del Dataset (CSV)

El archivo `paises.csv` debe seguir este formato:

```csv
nombre;poblacion;superficie;continente
China;1412000000;9596961;Asia
India;1408000000;3287263;Asia
Estados Unidos;331900000;9833517;América
```

### Campos:

| Campo        | Tipo    | Descripción                  |
| ------------ | ------- | ---------------------------- |
| `nombre`     | String  | Nombre del país              |
| `poblacion`  | Integer | Cantidad de habitantes       |
| `superficie` | Integer | Extensión territorial en km² |
| `continente` | String  | Continente al que pertenece  |

---

## 🎮 Ejemplos de Uso

### Búsqueda por nombre

```
Ingrese el nombre del país a buscar: China

=============================================
Búsqueda de países que coinciden con 'China'
=============================================
Nombre : China
Poblacion : 1412000000
Superficie : 9596961
Continente : Asia
```

### Filtro por continente

```
Ingrese el continente: Asia

- China
- India
- Indonesia
- Pakistán
```

### Filtro por rango de población

```
Ingrese el valor mínimo del rango: 100000000
Ingrese el valor máximo del rango: 500000000

- Países con poblacion entre 100000000 y 500000000
[Lista de países encontrados...]
```

### Estadísticas

```
====================================
       ESTADÍSTICAS GENERALES
====================================
  --- País con mayor población ---
Nombre : China
Poblacion : 1,412,000,000
Superficie : 9,596,961
Continente : Asia

  --- Promedio población ----
 => 622,458,833.5

  ---- Países por continente ----
- Cantidad de países de ASIA: 4
- Cantidad de países de EUROPA: 2
- Cantidad de países de AMERICA: 2
- Cantidad de países de AFRICA: 2
```

---

## 🏗️ Arquitectura y Diseño

### Modularización

El proyecto está diseñado siguiendo el principio de responsabilidad única, donde cada módulo tiene una función específica:

- **Separación de responsabilidades**: Cada archivo maneja un aspecto específico del sistema
- **Reutilización de código**: Las funciones son independientes y reutilizables
- **Mantenibilidad**: Facilita la detección y corrección de errores
- **Escalabilidad**: Permite agregar nuevas funcionalidades sin afectar el código existente

### Validaciones Implementadas

✅ Validación de números enteros positivos  
✅ Validación de rangos (mínimo < máximo)  
✅ Validación de texto (sin caracteres especiales)  
✅ Validación de opciones de menú  
✅ Manejo de errores en lectura de archivos  
✅ Detección de datos duplicados

---

## 🔧 Funcionalidades Técnicas

### Manejo de Archivos

- Lectura de CSV con encoding UTF-8
- Detección de errores de formato
- Conversión automática de tipos de datos
- Eliminación de espacios en blanco

### Estructuras de Datos

- **Listas**: Almacenamiento de países
- **Diccionarios**: Representación de cada país
- **Sets**: Control de duplicados
- **Tuplas**: Retorno múltiple de funciones

### Algoritmos

- Búsqueda secuencial con coincidencia parcial
- Ordenamiento con función `sorted()` y expresiones lambda
- Filtrado por múltiples criterios
- Cálculos estadísticos (max, min, promedio)

---

## ⚠️ Consideraciones Importantes

- **Encoding**: El CSV debe estar en UTF-8 para soportar caracteres especiales (tildes, ñ)
- **Delimitador**: Se utiliza punto y coma (`;`) como separador
- **Validación de datos**: Solo se cargan países con datos completos y válidos
- **Duplicados**: El sistema detecta y elimina automáticamente países duplicados

---

## 👥 Participantes

**Agustina Fontagnol** y **Gianella Peña**

---

## 📚 Informe, Video y Conceptos Aplicados

- **Link del informe**: https://colab.research.google.com/drive/16Ni9GnjZ9NN9UTEzmSm1cIw0udc5Ss8K
- **Link del video**: https://drive.google.com/drive/folders/1NOrZL0LWhjJX_-OYsqQXJ4U-3RPmzR1Z?usp=sharing
- **Listas y Diccionarios**: Almacenamiento y manipulación de datos estructurados
- **Funciones**: Modularización y reutilización de código
- **Condicionales**: Lógica de filtrado y validación
- **Bucles**: Iteración sobre colecciones de datos
- **Manejo de Archivos**: Lectura y procesamiento de CSV
- **Expresiones Lambda**: Ordenamiento personalizado
- **Match/Case**: Control de flujo moderno (Python 3.10+)

---

## 📖 Fuentes Bibliográficas

- [Python Documentation](https://docs.python.org)
- [CSV File Reading and Writing - Python Official Docs](https://docs.python.org/3/library/csv.html)
- [Real Python - Data Structures in Python](https://realpython.com)
- [GeeksforGeeks - Python Programming Examples](https://www.geeksforgeeks.org)
