import csv
import os


# --- FUNCIÓN DE UTILIDAD ---
# Función auxiliar para normalizar texto (elimina acentos para búsquedas).
def normalizar_texto(texto):
    # NOTA: Diccionario para mapear acentos y Ñ a caracteres simples.
    acentos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'ñ': 'n', 'Ñ': 'N'
    }
    # NOTA: Itera y reemplaza todos los caracteres acentuados.
    for acento, sin_acento in acentos.items():
        texto = texto.replace(acento, sin_acento)
    return texto

# --- MANEJO DE ARCHIVOS ---
def cargar_paises(nombre_archivo):
    paises = []
    ruta_completa = nombre_archivo
    
    # NOTA: Bloque para asegurar la ruta del archivo (lo busca junto al script si no lo encuentra).
    if not os.path.isabs(nombre_archivo): 
        if not os.path.exists(nombre_archivo): 
            ruta_script = os.path.dirname(os.path.abspath(__file__))
            ruta_completa = os.path.join(ruta_script, nombre_archivo)
    
    try:
        # NOTA: Abre el archivo en modo lectura ("r").
        with open(ruta_completa, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo) # NOTA: Usa los encabezados como claves de diccionario.
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]), # NOTA: Conversión a entero.
                        "superficie": int(fila["superficie"]), # NOTA: Conversión a entero.
                        "continente": fila["continente"].strip()
                    }
                    paises.append(pais)
                except (ValueError, KeyError):
                    continue # NOTA: Ignora filas con datos numéricos inválidos o columnas faltantes.
    except FileNotFoundError:
        print(f"Error: el archivo '{ruta_completa}' no existe.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    
    # NOTA: Devuelve la lista de países Y la ruta para usarla al guardar.
    return paises, ruta_completa


def guardar_paises(nombre_archivo, paises):
    """Guarda la lista de países en el archivo CSV."""
    try:
        # NOTA: Abre el archivo en modo escritura ("w", sobrescribe) y UTF-8.
        with open(nombre_archivo, "w", newline='', encoding="utf-8") as archivo:
            campos = ['nombre', 'poblacion', 'superficie', 'continente']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader() # NOTA: Escribe los encabezados.
            for p in paises:
                escritor.writerow(p) 
        return True
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
        return False

# --- FUNCIONES DE FILTRADO Y BÚSQUEDA ---
def buscar_pais(paises, nombre):
    """Devuelve países cuyo nombre coincida parcial o totalmente."""
    nombre_normalizado = normalizar_texto(nombre.strip().lower())
    resultado = []
    for p in paises:
        nombre_pais = normalizar_texto(p["nombre"].lower()) 
        if nombre_normalizado in nombre_pais: # NOTA: Búsqueda parcial y normalizada.
            resultado.append(p)
    return resultado


def filtrar_por_continente(paises, continente):
    """Filtra países por continente (sin importar acentos)."""
    continente_normalizado = normalizar_texto(continente.strip().lower())
    resultado = []
    for p in paises:
        cont_pais = normalizar_texto(p["continente"].lower()) 
        if cont_pais == continente_normalizado: # NOTA: Búsqueda exacta y normalizada (para América, África).
            resultado.append(p)
    return resultado


def filtrar_por_rango(paises, clave, minimo, maximo):
    """Filtra países según rango de población o superficie."""
    resultado = []
    for p in paises:
        if minimo <= p[clave] <= maximo: # NOTA: Comprueba si el valor está dentro del rango.
            resultado.append(p)
    return resultado

# --- FUNCIONES DE ORDENAMIENTO Y ESTADÍSTICAS ---
def ordenar_paises(paises, clave, descendente=False):
    """Ordena los países según la clave usando algoritmo burbuja."""
    lista = []
    for p in paises:
        lista.append(p) # NOTA: Crea una copia de la lista.
    
    n = len(lista)
    for i in range(n): 
        for j in range(0, n - i - 1): 
            if descendente:
                if lista[j][clave] < lista[j + 1][clave]: 
                    lista[j], lista[j + 1] = lista[j + 1], lista[j] # NOTA: Intercambio (SWAP).
            else:
                if lista[j][clave] > lista[j + 1][clave]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j] # NOTA: Intercambio (SWAP).
    return lista


def encontrar_mayor_poblacion(paises):
    """Encuentra el país con mayor población manualmente."""
    if len(paises) == 0:
        return None
    mayor = paises[0]
    for p in paises: 
        if p["poblacion"] > mayor["poblacion"]:
            mayor = p
    return mayor


def encontrar_menor_poblacion(paises):
    """Encuentra el país con menor población manualmente."""
    if len(paises) == 0:
        return None
    menor = paises[0]
    for p in paises: 
        if p["poblacion"] < menor["poblacion"]:
            menor = p
    return menor


def calcular_promedio_poblacion(paises):
    """Calcula el promedio de población manualmente."""
    if len(paises) == 0:
        return 0
    total = 0
    for p in paises:
        total += p["poblacion"] 
    return total / len(paises) # NOTA: Suma total dividida por la cantidad de países.


def calcular_promedio_superficie(paises):
    """Calcula el promedio de superficie manualmente."""
    if len(paises) == 0:
        return 0
    total = 0
    for p in paises:
        total += p["superficie"]
    return total / len(paises)


def contar_por_continente(paises):
    """Cuenta cuántos países hay por continente manualmente."""
    continentes = {}
    for p in paises:
        cont = p["continente"]
        if cont in continentes:
            continentes[cont] += 1 # NOTA: Incrementa el contador si ya existe.
        else:
            continentes[cont] = 1 # NOTA: Inicializa el contador en 1 si es nuevo.
    return continentes


def estadisticas(paises):
    """Calcula estadísticas generales del conjunto de países."""
    if len(paises) == 0:
        return None

    max_pob = encontrar_mayor_poblacion(paises)
    min_pob = encontrar_menor_poblacion(paises)
    prom_pob = calcular_promedio_poblacion(paises)
    prom_sup = calcular_promedio_superficie(paises)
    continentes = contar_por_continente(paises)

    # NOTA: Devuelve un diccionario con todos los resultados de las funciones de estadística.
    return { 
        "mayor_poblacion": max_pob,
        "menor_poblacion": min_pob,
        "promedio_poblacion": prom_pob,
        "promedio_superficie": prom_sup,
        "cantidad_por_continente": continentes
    }

# --- FUNCIÓN DE AGREGAR PAÍS ---
def existe_pais(paises, nombre):
    """Verifica si un país ya existe en la lista."""
    nombre_normalizado = normalizar_texto(nombre.strip().lower()) 
    for p in paises:
        nombre_pais = normalizar_texto(p["nombre"].lower())
        if nombre_normalizado == nombre_pais: # NOTA: Compara si los nombres normalizados son iguales.
            return True
    return False


def agregar_pais(paises, nombre_archivo):
    """Agrega un nuevo país manualmente con validaciones."""
    print("\n=== AGREGAR NUEVO PAÍS ===")
    
    nombre = input("Nombre del país: ").strip()
    if len(nombre) == 0:
        print("Error: el nombre no puede estar vacío.")
        return False
    
    if existe_pais(paises, nombre): # NOTA: Verifica duplicados.
        print(f"Error: el país '{nombre}' ya existe en la lista.")
        return False
    
    continente = input("Continente: ").strip()
    if len(continente) == 0:
        print("Error: el continente no puede estar vacío.")
        return False
    
    try:
        poblacion = int(input("Población: "))
        if poblacion < 0:
            print("Error: la población no puede ser negativa.")
            return False
    except ValueError:
        print("Error: debe ingresar un número válido para la población.")
        return False
    
    try:
        superficie = int(input("Superficie (km²): "))
        if superficie < 0:
            print("Error: la superficie no puede ser negativa.")
            return False
    except ValueError:
        print("Error: debe ingresar un número válido para la superficie.")
        return False
    
    nuevo_pais = { 
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    
    paises.append(nuevo_pais)
    
    if guardar_paises(nombre_archivo, paises): # NOTA: Intenta guardar en el CSV.
        print(f"\n¡País '{nombre}' agregado exitosamente!")
        return True
    else:
        paises.pop() # NOTA: Si falla el guardado, revierte la adición de la lista en memoria.
        print("Error: no se pudo guardar el país.")
        return False