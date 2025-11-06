import csv

# ---------------- CARGAR PAISES DESDE CSV ----------------
# Esta función lee el archivo CSV y devuelve una lista de diccionarios.
# Cada país tiene: nombre, población, superficie y continente.
def cargar_paises(ruta_archivo):
    paises = []
    try:
        with open(ruta_archivo, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    fila['poblacion'] = int(fila['poblacion'])
                    fila['superficie'] = int(fila['superficie'])
                except ValueError:
                    continue  # Si hay un error en los datos numéricos, se salta esa fila
                paises.append(fila)
    except FileNotFoundError:
        print(f"Error: el archivo '{ruta_archivo}' no se encontró.")
    return paises


# ---------------- GUARDAR PAISES EN CSV ----------------
# Guarda la lista actualizada de países en el archivo CSV
def guardar_paises(ruta_archivo, paises):
    try:
        with open(ruta_archivo, 'w', newline='', encoding='utf-8') as archivo:
            campos = ['nombre', 'poblacion', 'superficie', 'continente']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(paises)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")


# ---------------- BUSCAR PAIS ----------------
# Devuelve una lista con los países cuyo nombre contenga la palabra buscada (sin importar mayúsculas o minúsculas)
def buscar_pais(paises, nombre):
    nombre = nombre.strip().lower()
    resultado = [p for p in paises if nombre in p['nombre'].lower()]
    return resultado


# ---------------- FILTRAR POR CONTINENTE ----------------
# Devuelve los países del continente indicado (sin importar mayúsculas o minúsculas)
def filtrar_por_continente(paises, continente):
    continente = continente.strip().lower()
    resultado = [p for p in paises if p['continente'].lower() == continente]
    return resultado


# ---------------- FILTRAR POR RANGO ----------------
# Permite filtrar países por población o superficie dentro de un rango dado
def filtrar_por_rango(paises, clave, minimo, maximo):
    resultado = [p for p in paises if minimo <= p[clave] <= maximo]
    return resultado


# ---------------- ORDENAR PAISES ----------------
# Ordena los países según una clave dada y el sentido (ascendente o descendente)
# En lugar de usar sort() se implementa el método burbuja
def ordenar_paises(paises, clave, descendente=False):
    lista = paises.copy()
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if descendente:
                if lista[j][clave] < lista[j + 1][clave]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
            else:
                if lista[j][clave] > lista[j + 1][clave]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


# ---------------- ESTADÍSTICAS ----------------
# Calcula los países con mayor y menor población, promedios y cantidad por continente
def estadisticas(paises):
    if not paises:
        return None

    mayor_pob = max(paises, key=lambda p: p['poblacion'])
    menor_pob = min(paises, key=lambda p: p['poblacion'])
    promedio_pob = sum(p['poblacion'] for p in paises) / len(paises)
    promedio_sup = sum(p['superficie'] for p in paises) / len(paises)

    cantidad_cont = {}
    for p in paises:
        cont = p['continente']
        cantidad_cont[cont] = cantidad_cont.get(cont, 0) + 1

    return {
        "mayor_poblacion": mayor_pob,
        "menor_poblacion": menor_pob,
        "promedio_poblacion": promedio_pob,
        "promedio_superficie": promedio_sup,
        "cantidad_por_continente": cantidad_cont
    }


# ---------------- AGREGAR PAIS MANUALMENTE ----------------
# Permite ingresar un nuevo país desde teclado y lo guarda en el CSV
def agregar_pais_manual(paises, ruta_archivo):
    nombre = input("Nombre del país: ").strip()
    continente = input("Continente: ").strip()
    try:
        poblacion = int(input("Población: "))
        superficie = int(input("Superficie: "))
    except ValueError:
        print("Error: debe ingresar valores numéricos válidos.")
        return None

    nuevo = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo)
    guardar_paises(ruta_archivo, paises)
    return nuevo
