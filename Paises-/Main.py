# Importo todas las funciones desde el archivo funciones.py
# (ahí están las tareas principales como buscar, filtrar, ordenar, etc.)
from funciones import *

# ---------------- MENÚ PRINCIPAL ----------------
# Esta función solo muestra las opciones que el usuario puede elegir
def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Buscar país por nombre")
    print("2. Filtrar países por continente")
    print("3. Filtrar países por rango de población")
    print("4. Filtrar países por rango de superficie")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Agregar país manualmente")
    print("0. Salir")

# ---------------- MOSTRAR PAÍSES ----------------
# Esta función recibe una lista de países y los muestra por pantalla
def mostrar_paises(lista):
    # Si la lista está vacía, muestra un mensaje y corta la función
    if not lista:
        print("No se encontraron resultados.")
        return
    # Si hay países, recorre la lista y muestra cada uno
    for p in lista:
        print(f"{p['nombre']:} | Población: {p['poblacion']:} | Superficie: {p['superficie']:} | {p['continente']}")

# ---------------- FUNCIÓN PRINCIPAL ----------------
def main():
    
    # Acá se indica la ruta donde está guardado el archivo CSV con los países
    archivo_csv = "c:\\Users\\Luciano Nicolas\\Documents\\GitHub\\Trabajo-integrador-Programacion-\\Paises-\\Paises.csv"

    # Se cargan los países desde el CSV usando una función del archivo funciones.py
    paises = cargar_paises(archivo_csv)

    # Si no se pudieron cargar los datos, se corta el programa
    if not paises:
        print("No se pudieron cargar los datos. Verifique el archivo CSV.")
        return

    # Bucle principal del programa: se repite hasta que el usuario elige salir
    while True:
        mostrar_menu()  # Muestra las opciones
        opcion = input("Seleccione una opción: ")  # Pide al usuario qué quiere hacer

        # --- Opción 1: Buscar país por nombre ---
        if opcion == "1":
            nombre = input("Ingrese nombre o parte del nombre del país: ")
            resultado = buscar_pais(paises, nombre)  # Llama a la función que busca el país
            mostrar_paises(resultado)

        # --- Opción 2: Filtrar por continente ---
        elif opcion == "2":
            cont = input("Ingrese continente: ")
            resultado = filtrar_por_continente(paises, cont)
            mostrar_paises(resultado)

        # --- Opción 3: Filtrar por rango de población ---
        elif opcion == "3":
            try:
                min_pob = int(input("Población mínima: "))
                max_pob = int(input("Población máxima: "))
                resultado = filtrar_por_rango(paises, "poblacion", min_pob, max_pob)
                mostrar_paises(resultado)
            except ValueError:
                print("Error: debe ingresar valores numéricos.")

        # --- Opción 4: Filtrar por rango de superficie ---
        elif opcion == "4":
            try:
                min_sup = int(input("Superficie mínima: "))
                max_sup = int(input("Superficie máxima: "))
                resultado = filtrar_por_rango(paises, "superficie", min_sup, max_sup)
                mostrar_paises(resultado)
            except ValueError:
                print("Error: debe ingresar valores numéricos.")

        # --- Opción 5: Ordenar países ---
        elif opcion == "5":
            clave = input("Ordenar por (nombre/poblacion/superficie): ").lower()
            sentido = input("¿Descendente? (s/n): ").lower() == "s"
            # Verifica que la clave sea válida antes de ordenar
            if clave in ["nombre", "poblacion", "superficie"]:
                resultado = ordenar_paises(paises, clave, sentido)
                mostrar_paises(resultado)
            else:
                print("Clave inválida.")

        # --- Opción 6: Mostrar estadísticas ---
        elif opcion == "6":
            est = estadisticas(paises)
            if est:
                print(f"\nPaís con mayor población: {est['mayor_poblacion']['nombre']} ({est['mayor_poblacion']['poblacion']})")
                print(f"País con menor población: {est['menor_poblacion']['nombre']} ({est['menor_poblacion']['poblacion']})")
                print(f"Población promedio: {est['promedio_poblacion']:.2f}")
                print(f"Superficie promedio: {est['promedio_superficie']:.2f}")
                print("\nCantidad de países por continente:")
                # Recorre el diccionario y muestra cuántos países hay por continente
                for cont, cant in est["cantidad_por_continente"].items():
                    print(f"  {cont}: {cant}")

        # --- Opción 7: Agregar país manualmente ---
        elif opcion == "7":
            # Llama a la función que pide los datos al usuario y guarda el nuevo país
            agregar_pais_manual(paises, archivo_csv)

        # --- Opción 0: Salir del programa ---
        elif opcion == "0":
            print("Saliendo del programa...")
            break

        # --- Si elige algo inválido ---
        else:
            print("Opción inválida. Intente nuevamente.")

# ---------------- PUNTO DE ENTRADA ----------------
# Esto hace que el programa empiece a ejecutarse desde acá
if __name__ == "__main__":
    main()
