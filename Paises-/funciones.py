import csv  
import os


def cargar_paises(ruta):
    """Carga el CSV manualmente y devuelve lista de dicts.
    Formato esperado: nombre,poblacion,superficie,continente (encabezado opcional).
    """
    paises = []
    if not os.path.isfile(ruta):
        print("Error: el archivo no existe.")
        return paises
    try:
        f = open(ruta, "r", encoding="utf-8")
        lineas = f.readlines()
        f.close()
    except Exception as e:
        print("Error al abrir el archivo:", e)
        return paises

    # limpiar líneas
    lineas = [l.strip() for l in lineas if l.strip() != ""]

    if len(lineas) == 0:
        return paises

    # saltar posible encabezado
    primera = lineas[0].lower()
    if "nombre" in primera and "poblacion" in primera:
        datos = lineas[1:]
    else:
        datos = lineas

    for i, linea in enumerate(datos, start=1):
        partes = linea.split(",")
        if len(partes) < 4:
            print("Advertencia: línea", i, "mal formada:", linea)
            continue
        nombre = partes[0].strip()
        pobl_str = partes[1].strip()
        sup_str = partes[2].strip()
        continente = partes[3].strip()

        # convertir población
        try:
            pobl = int(pobl_str.replace(".", "").replace(" ", ""))
        except:
            try:
                pobl = int(float(pobl_str))
            except:
                print("Advertencia: población inválida en línea", i, ":", pobl_str)
                continue

        # convertir superficie
        try:
            sup = int(sup_str.replace(".", "").replace(" ", ""))
        except:
            try:
                sup = int(float(sup_str))
            except:
                print("Advertencia: superficie inválida en línea", i, ":", sup_str)
                continue

        pais = {
            "nombre": nombre,
            "poblacion": pobl,
            "superficie": sup,
            "continente": continente
        }
        paises.append(pais)

    return paises


def buscar_pais(paises, texto):
    
    if not texto:
        return []
    txt = texto.lower()
    resultados = []
    for p in paises:
        nombre = p.get("nombre", "").lower()
        if txt in nombre:
            resultados.append(p)
    return resultados


def filtrar_por_continente(paises, continente):
   
    if not continente:
        return []
    cont = continente.lower()
    resultados = []
    for p in paises:
        if p.get("continente", "").lower() == cont:
            resultados.append(p)
    return resultados


def filtrar_por_rango(paises, campo, minimo, maximo):
    
    if campo not in ("poblacion", "superficie"):
        return []
    resultados = []
    for p in paises:
        try:
            valor = int(p.get(campo, 0))
        except:
            continue
        if valor >= minimo and valor <= maximo:
            resultados.append(p)
    return resultados


def ordenar_paises(paises, campo, descendente=False):
    # copia simple
    lista = []
    for p in paises:
        lista.append(dict(p))

    n = 0
    for _ in lista:
        n += 1

    # comparación sencilla
    def menor(a, b):
        if campo == "nombre":
            try:
                return a.get("nombre", "").lower() < b.get("nombre", "").lower()
            except:
                return False
        else:
            try:
                return int(a.get(campo, 0)) < int(b.get(campo, 0))
            except:
                return False

    # bubble sort (fácil de entender)
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
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
    return lista


def estadisticas(paises):
    """Calcula mayor/menor población, promedios y cantidad por continente."""
    if not paises:
        return None

    mayor = None
    menor = None
    suma_pob = 0
    suma_sup = 0
    contador = 0
    por_continente = {}

    for p in paises:
        try:
            pob = int(p.get("poblacion", 0))
        except:
            continue
        try:
            sup = int(p.get("superficie", 0))
        except:
            sup = 0

        if mayor is None or pob > mayor["poblacion"]:
            mayor = p
        if menor is None or pob < menor["poblacion"]:
            menor = p

        suma_pob += pob
        suma_sup += sup
        contador += 1

        cont = p.get("continente", "Desconocido")
        if cont in por_continente:
            por_continente[cont] += 1
        else:
            por_continente[cont] = 1

    if contador == 0:
        return None

    promedio_pob = suma_pob / contador
    promedio_sup = suma_sup / contador

    return {
        "mayor_poblacion": mayor,
        "menor_poblacion": menor,
        "promedio_poblacion": promedio_pob,
        "promedio_superficie": promedio_sup,
        "cantidad_por_continente": por_continente
    }
