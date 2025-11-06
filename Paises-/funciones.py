import csv # NOTA: Módulo para leer y escribir archivos CSV (Comma Separated Values).
import os # NOTA: Módulo para interactuar con el sistema operativo (rutas de archivos).

# --- FUNCIÓN DE UTILIDAD ---
# Función auxiliar para normalizar texto (elimina acentos, facilita búsquedas)
def normalizar_texto(texto):
    # NOTA: Diccionario con acentos y sus equivalentes sin acento, incluyendo la Ñ.
    acentos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'ñ': 'n', 'Ñ': 'N'
    }
    # NOTA: Itera sobre el diccionario para reemplazar cada acento encontrado.
    for acento, sin_acento in acentos.items():
        texto = texto.replace(acento, sin_acento)
    return texto

# --- MANEJO DE ARCHIVOS ---
def cargar_paises(nombre_archivo):
    paises = []
    ruta_completa = nombre_archivo # NOTA: Guarda la ruta completa para devolverla y usarla al guardar.
    
    # NOTA: Bloque para hacer la ruta del archivo robusta (busca el archivo junto al script).
    if not os.path.isabs(nombre_archivo): # Verifica si la ruta es absoluta
        if not os.path.exists(nombre_archivo): # Si no existe en la ubicación actual
            ruta_script = os.path.dirname(os.path.abspath(__file__)) # Obtiene la ruta del script
            ruta_completa = os.path.join(ruta_script, nombre_archivo) # Junta la ruta del script con el nombre
    
    try:
        # NOTA: Abre el archivo en modo lectura ("r") con codificación UTF-8 para leer tildes.
        with open(ruta_completa, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo) # NOTA: Lee el CSV usando los encabezados como claves (Diccionario).
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(), # NOTA: .strip() elimina espacios al inicio/final.
                        "poblacion": int(fila["poblacion"]), # NOTA: Convierte la población a número entero.
                        "superficie": int(fila["superficie"]), # NOTA: Convierte la superficie a número entero.
                        "continente": fila["continente"].strip()
                    }
                    paises.append(pais)
                except (ValueError, KeyError):
                    continue # NOTA: Si una fila falla (datos no son números o faltan columnas), la ignora.
    except FileNotFoundError:
        print(f"Error: el archivo '{ruta_completa}' no existe.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    
    # NOTA: Devuelve la lista de países Y la ruta completa para usarla al guardar (evita crear archivos duplicados).
    return paises, ruta_completa


def guardar_paises(nombre_archivo, paises):
    """Guarda la lista de países en el archivo CSV."""
    try:
        # NOTA: Abre el archivo en modo escritura ("w", sobrescribe) sin saltos de línea extra.
        with open(nombre_archivo, "w", newline='', encoding="utf-8") as archivo:
            campos = ['nombre', 'poblacion', 'superficie', 'continente']
            escritor = csv.DictWriter(archivo, fieldnames=campos) # NOTA: Define qué columnas escribir.
            escritor.writeheader() # NOTA: Escribe la primera fila con los nombres de las columnas.
            for p in paises:
                escritor.writerow(p) # NOTA: Escribe cada diccionario (país) como una fila.
        return True
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
        return False

# --- FUNCIONES DE FILTRADO Y BÚSQUEDA ---
def buscar_pais(paises, nombre):
    """Devuelve países cuyo nombre coincida parcial o totalmente."""
    # NOTA: Normaliza la búsqueda (sin tildes, minúsculas) para hacerla más fácil.
    nombre_normalizado = normalizar_texto(nombre.strip().lower())
    resultado = []
    for p in paises:
        # NOTA: Normaliza el nombre del país para compararlo.
        nombre_pais = normalizar_texto(p["nombre"].lower()) 
        if nombre_normalizado in nombre_pais: # NOTA: Comprueba si la búsqueda está contenida en el nombre del país.
            resultado.append(p)
    return resultado


def filtrar_por_continente(paises, continente):
    """Filtra países por continente (sin importar acentos)."""
    # NOTA: Normaliza el continente buscado.
    continente_normalizado = normalizar_texto(continente.strip().lower())
    resultado = []
    for p in paises:
        # NOTA: Normaliza el continente del país para comparación exacta.
        cont_pais = normalizar_texto(p["continente"].lower()) 
        if cont_pais == continente_normalizado: # NOTA: Compara si son exactamente iguales.
            resultado.append(p)
    return resultado


def filtrar_por_rango(paises, clave, minimo, maximo):
    """Filtra países según rango de población o superficie."""
    resultado = []
    for p in paises:
        # NOTA: Verifica si el valor de la clave (poblacion/superficie) está dentro del rango.
        if minimo <= p[clave] <= maximo: 
            resultado.append(p)
    return resultado

# --- FUNCIONES DE ORDENAMIENTO Y ESTADÍSTICAS ---
def ordenar_paises(paises, clave, descendente=False):
    """Ordena los países según la clave usando algoritmo burbuja."""
    lista = []
    for p in paises:
        lista.append(p) # NOTA: Crea una copia de la lista para no modificar la original.
    
    n = len(lista)
    # NOTA: Bucle exterior del método burbuja.
    for i in range(n): 
        # NOTA: Bucle interior, compara y mueve elementos adyacentes.
        for j in range(0, n - i - 1): 
            if descendente:
                # NOTA: Ordena de mayor a menor.
                if lista[j][clave] < lista[j + 1][clave]: 
                    lista[j], lista[j + 1] = lista[j + 1], lista[j] # SWAP (Intercambio)
            else:
                # NOTA: Ordena de menor a mayor.
                if lista[j][clave] > lista[j + 1][clave]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j] # SWAP
    return lista


def encontrar_mayor_poblacion(paises):
    """Encuentra el país con mayor población manualmente."""
    if len(paises) == 0:
        return None
    mayor = paises[0]
    # NOTA: Recorre la lista, actualizando 'mayor' si encuentra un país con más población.
    for p in paises: 
        if p["poblacion"] > mayor["poblacion"]:
            mayor = p
    return mayor


def encontrar_menor_poblacion(paises):
    """Encuentra el país con menor población manualmente."""
    if len(paises) == 0:
        return None
    menor = paises[0]
    # NOTA: Recorre la lista, actualizando 'menor' si encuentra un país con menos población.
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
        total += p["poblacion"] # NOTA: Suma la población de todos los países.
    return total / len(paises) # NOTA: Divide la suma por la cantidad de países.


def calcular_promedio_superficie(paises):
    """Calcula el promedio de superficie manualmente."""
    if len(paises) == 0:
        return 0
    total = 0
    for p in paises:
        total += p["superficie"] # NOTA: Suma la superficie de todos los países.
    return total / len(paises)


def contar_por_continente(paises):
    """Cuenta cuántos países hay por continente manualmente."""
    continentes = {}
    for p in paises:
        cont = p["continente"]
        if cont in continentes:
            continentes[cont] += 1 # NOTA: Si ya existe, suma 1.
        else:
            continentes[cont] = 1 # NOTA: Si no existe, lo inicializa en 1.
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
    # NOTA: Normaliza el nombre para verificar si existe sin importar mayúsculas/tildes.
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
    
    if existe_pais(paises, nombre): # NOTA: Llama a la función de verificación.
        print(f"Error: el país '{nombre}' ya existe en la lista.")
        return False
    
    # NOTA: Muestra los continentes existentes para que el usuario elija uno igual.
    continentes_existentes = contar_por_continente(paises)
    print("\nContinentes existentes en el sistema:")
    contador = 1
    lista_continentes = []
    for cont in continentes_existentes:
        print(f"  {contador}. {cont}")
        lista_continentes.append(cont)
        contador += 1
    print(f"  {contador}. Escribir otro continente manualmente")
    
    try:
        opcion_cont = int(input("\nSeleccione el número del continente: "))
        if 1 <= opcion_cont <= len(lista_continentes):
            # NOTA: Usa el continente exactamente como está en el sistema.
            continente = lista_continentes[opcion_cont - 1]
        elif opcion_cont == contador:
            continente = input("Escriba el continente: ").strip()
            if len(continente) == 0:
                print("Error: el continente no puede estar vacío.")
                return False
        else:
            print("Error: opción inválida.")
            return False
    except ValueError:
        print("Error: debe ingresar un número válido.")
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
    
    nuevo_pais = { # NOTA: Crea el diccionario con los datos ingresados.
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    
    paises.append(nuevo_pais)
    
    if guardar_paises(nombre_archivo, paises): # NOTA: Intenta guardar la lista actualizada en el CSV.
        print(f"\n¡País '{nombre}' agregado exitosamente!")
        return True
    else:
        paises.pop() # NOTA: Si falla al guardar, elimina el país de la lista de Python para evitar inconsistencia.
        print("Error: no se pudo guardar el país.")
        return False