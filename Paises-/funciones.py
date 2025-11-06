import os
import re

# ----------------------------------------------------------
# FUNCIÓN: cargar_paises
# ----------------------------------------------------------
# Esta función abre el archivo CSV donde están los países y carga sus datos.
# Busca el archivo automáticamente en la misma carpeta del proyecto.
# Devuelve una lista de diccionarios, donde cada país tiene:
# nombre, población, superficie y continente.
def cargar_paises(ruta_csv):
    paises = []

    # Ubica la carpeta donde está este archivo (funciones.py)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_completa = os.path.join(base_dir, ruta_csv)

    # Verifica si el archivo existe
    if not os.path.isfile(ruta_completa):
        print("Error: el archivo no existe en la ruta:", ruta_completa)
        return paises

    # Intenta abrir y leer el archivo
    try:
        with open(ruta_completa, "r", encoding="utf-8") as f:
            lineas = f.readlines()
    except Exception as e:
        print("Error al abrir el archivo:", e)
        return paises

    # Elimina líneas vacías y espacios innecesarios
    lineas = [l.strip() for l in lineas if l.strip() != ""]

    # Si el archivo está vacío, devuelve una lista vacía
    if len(lineas) == 0:
        return paises

    # Verifica si la primera línea tiene los nombres de columnas
    primera = lineas[0].lower()
    if "nombre" in primera and "poblacion" in primera:
        datos = lineas[1:]
    else:
        datos = lineas

    # Recorre cada línea y la convierte en un diccionario
    for i, linea in enumerate(datos, start=1):
        partes = linea.split(",")
        if len(partes) < 4:
            print("Advertencia: línea", i, "mal formada:", linea)
            continue

        nombre = partes[0].strip()
        pobl_str = partes[1].strip()
        sup_str = partes[2].strip()
        continente = partes[3].strip()

        # Convierte la población a número
        try:
            pobl = int(pobl_str.replace(".", "").replace(" ", ""))
        except:
            try:
                pobl = int(float(pobl_str))
            except:
                print("Advertencia: población inválida en línea", i, ":", pobl_str)
                continue

        # Convierte la superficie a número
        try:
            sup = int(sup_str.replace(".", "").replace(" ", ""))
        except:
            try:
                sup = int(float(sup_str))
            except:
                print("Advertencia: superficie inválida en línea", i, ":", sup_str)
                continue

        # Crea un diccionario con los datos del país
        pais = {
            "nombre": nombre,
            "poblacion": pobl,
            "superficie": sup,
            "continente": continente
        }
        paises.append(pais)

    return paises


# ----------------------------------------------------------
# FUNCIÓN: buscar_pais
# ----------------------------------------------------------
# Busca países que contengan un texto dentro de su nombre.
# Ejemplo: buscar "ar" puede devolver "Argentina".
# No distingue entre mayúsculas y minúsculas.
def buscar_pais(paises, texto):
    if not texto:
        return []
    txt = texto.strip().lower()  # convierte a minúsculas
    resultados = []
    for p in paises:
        nombre = p.get("nombre", "").lower()
        if txt in nombre:
            resultados.append(p)
    return resultados


# ----------------------------------------------------------
# FUNCIÓN: filtrar_por_continente
# ----------------------------------------------------------
# Devuelve una lista con los países que pertenecen a un continente específico.
# No distingue entre mayúsculas y minúsculas (por ejemplo: "Europa" o "europa").
def filtrar_por_continente(paises, continente):
    if not continente:
        return []
    cont = continente.strip().lower()
    resultados = []
    for p in paises:
        if p.get("continente", "").lower() == cont:
            resultados.append(p)
    return resultados


# ----------------------------------------------------------
# FUNCIÓN: filtrar_por_rango
# ----------------------------------------------------------
# Permite filtrar países según un rango de población o superficie.
# Convierte los valores ingresados a números para evitar errores.
def filtrar_por_rango(paises, campo, minimo, maximo):
    if campo not in ("poblacion", "superficie"):
        return []
    resultados = []
    for p in paises:
        try:
            valor = int(p.get(campo, 0))
        except:
            continue
        if minimo <= valor <= maximo:
            resultados.append(p)
    return resultados


# ----------------------------------------------------------
# FUNCIÓN: ordenar_paises
# ----------------------------------------------------------
# Ordena los países por nombre, población o superficie.
# Se puede elegir ascendente o descendente.
# Además, compara sin distinguir mayúsculas.
def ordenar_paises(paises, campo, descendente=False):
    lista = [dict(p) for p in paises]  # copia de la lista original
    n = len(lista)

    def menor(a, b):
        if campo == "nombre":
            return a.get("nombre", "").lower() < b.get("nombre", "").lower()
        else:
            return int(a.get(campo, 0)) < int(b.get(campo, 0))

    # Método burbuja (bubble sort)
    for i in range(n):
        for j in range(0, n - 1 - i):
            swap = False
            if descendente:
                if menor(lista[j], lista[j + 1]):
                    swap = True
            else:
                if menor(lista[j + 1], lista[j]):
                    swap = True
            if swap:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


# ----------------------------------------------------------
# FUNCIÓN: estadisticas
# ----------------------------------------------------------
# Calcula estadísticas básicas:
# - País con mayor y menor población
# - Promedio de población y superficie
# - Cantidad de países por continente
def estadisticas(paises):
    if not paises:
        return None

    mayor = menor = None
    suma_pob = suma_sup = contador = 0
    por_continente = {}

    for p in paises:
        pob = int(p.get("poblacion", 0))
        sup = int(p.get("superficie", 0))

        if mayor is None or pob > mayor["poblacion"]:
            mayor = p
        if menor is None or pob < menor["poblacion"]:
            menor = p

        suma_pob += pob
        suma_sup += sup
        contador += 1

        cont = p.get("continente", "Desconocido")
        cont = cont.strip().capitalize()
        por_continente[cont] = por_continente.get(cont, 0) + 1

    promedio_pob = suma_pob / contador
    promedio_sup = suma_sup / contador

    return {
        "mayor_poblacion": mayor,
        "menor_poblacion": menor,
        "promedio_poblacion": promedio_pob,
        "promedio_superficie": promedio_sup,
        "cantidad_por_continente": por_continente
    }


# ----------------------------------------------------------
# FUNCIÓN: agregar_pais_manual
# ----------------------------------------------------------
# Permite ingresar un nuevo país desde teclado.
# El país se guarda tanto en la lista como en el archivo CSV.
# Las validaciones evitan errores comunes de escritura o duplicación.
def agregar_pais_manual(paises, archivo_csv):
    def solo_letras_ascii_y_espacios(s):
        s = s.strip()
        return bool(re.match(r'^[A-Za-z\s]+$', s))

    nombre = input("Nombre del país: ").strip()
    if not nombre or not solo_letras_ascii_y_espacios(nombre):
        print("Nombre inválido. Use sólo letras ASCII y espacios.")
        return

    if any(p['nombre'].strip().lower() == nombre.lower() for p in paises):
        print("Error: el país ya está cargado.")
        return

    continente = input("Continente: ").strip()
    if not continente or not solo_letras_ascii_y_espacios(continente):
        print("Continente inválido.")
        return

    while True:
        try:
            poblacion = int(input("Población (entero): ").strip())
            if poblacion < 0:
                print("La población debe ser no negativa.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

    while True:
        try:
            superficie = float(input("Superficie (puede tener decimales): ").strip())
            if superficie < 0:
                print("La superficie debe ser no negativa.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número (ej. 1234 o 1234.56).")

    nuevo = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(nuevo)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_completa = os.path.join(base_dir, archivo_csv)

    try:
        with open(ruta_completa, "a", encoding="utf-8") as f:
            f.write(f"{nombre},{poblacion},{superficie},{continente}\n")
        print("País agregado correctamente y guardado en el CSV.")
    except Exception as e:
        print("País agregado en memoria pero no se pudo guardar en el CSV:", e)
