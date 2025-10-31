import csv  
import os
import re


def cargar_paises(ruta):
    
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

    
    lineas = [l.strip() for l in lineas if l.strip() != ""]

    if len(lineas) == 0:
        return paises

    
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
    
    lista = []
    for p in paises:
        lista.append(dict(p))

    n = 0
    for _ in lista:
        n += 1

    
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


def agregar_pais_manual(paises, archivo_csv):
    def solo_letras_ascii_y_espacios(s):
        s = s.strip()
        return bool(re.match(r'^[A-Za-z\s]+$', s))

    nombre = input("Nombre del país: ").strip()
    if not nombre or not solo_letras_ascii_y_espacios(nombre):
        print("Nombre inválido. Use sólo letras ASCII y espacios (no acentos ni ñ, no números ni símbolos).")
        return

    if any(p['nombre'].strip().lower() == nombre.lower() for p in paises):
        print("Error: el país ya está cargado. No se puede duplicar.")
        return

    continente = input("Continente: ").strip()
    if not continente or not solo_letras_ascii_y_espacios(continente):
        print("Continente inválido. Use sólo letras ASCII y espacios (no acentos ni ñ, no números ni símbolos).")
        return

    while True:
        pob_input = input("Población (entero): ").strip()
        try:
            poblacion = int(pob_input)
            if poblacion < 0:
                print("La población debe ser un número no negativo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

    while True:
        sup_input = input("Superficie (puede tener decimales): ").strip()
        try:
            superficie = float(sup_input)
            if superficie < 0:
                print("La superficie debe ser un número no negativo.")
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

    try:
        with open(archivo_csv, "a", encoding="utf-8") as f:
            f.write(f"{nombre},{poblacion},{superficie},{continente}\n")
        print("País agregado correctamente y guardado en el CSV.")
    except Exception as e:
        print("País agregado en memoria pero no se pudo guardar en el CSV:", e)
