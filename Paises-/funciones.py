import csv  


def cargar_paises(nombre_archivo):
    paises = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }
                paises.append(pais)
    except FileNotFoundError:
        print(" Error: el archivo no existe.")
    except ValueError:
        print(" Error: formato de datos incorrecto en el CSV.")
    return paises




def buscar_pais(paises, nombre):
    """Devuelve países cuyo nombre coincida parcial o totalmente."""
    return [p for p in paises if nombre.lower() in p["nombre"].lower()]


def filtrar_por_continente(paises, continente):
    """Filtra países por continente."""
    return [p for p in paises if p["continente"].lower() == continente.lower()]


def filtrar_por_rango(paises, clave, minimo, maximo):
    """Filtra países según rango de población o superficie."""
    return [p for p in paises if minimo <= p[clave] <= maximo]


def ordenar_paises(paises, clave, descendente=False):
    """Ordena los países según la clave (nombre, poblacion, superficie)."""
    return sorted(paises, key=lambda p: p[clave], reverse=descendente)


def estadisticas(paises):
    """Calcula estadísticas generales del conjunto de países."""
    if not paises:
        return None

    max_pob = max(paises, key=lambda p: p["poblacion"])
    min_pob = min(paises, key=lambda p: p["poblacion"])
    prom_pob = sum(p["poblacion"] for p in paises) / len(paises)
    prom_sup = sum(p["superficie"] for p in paises) / len(paises)

    continentes = {}
    for p in paises:
        cont = p["continente"]
        continentes[cont] = continentes.get(cont, 0) + 1

    return {
        "mayor_poblacion": max_pob,
        "menor_poblacion": min_pob,
        "promedio_poblacion": prom_pob,
        "promedio_superficie": prom_sup,
        "cantidad_por_continente": continentes
    }
