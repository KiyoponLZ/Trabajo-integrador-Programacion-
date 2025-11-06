from funciones import * # NOTA: Importa todas las funciones de manejo de datos (cargar, filtrar, ordenar, etc.)

# --- INTERFAZ DE USUARIO ---
def mostrar_menu():
    # NOTA: Función simple para imprimir las opciones disponibles al usuario.
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Buscar país por nombre")
    print("2. Filtrar países por continente")
    print("3. Filtrar países por rango de población")
    print("4. Filtrar países por rango de superficie")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Agregar país manualmente")
    print("0. Salir")


def mostrar_paises(lista):
    # NOTA: Función para mostrar los resultados de una búsqueda/filtro de forma formateada.
    if len(lista) == 0:
        print("No se encontraron resultados.")
        return
    # NOTA: Usa formato de alineación (:15, :10) para que las columnas se vean ordenadas.
    for p in lista:
        print(f"{p['nombre']:15} | Población: {p['poblacion']:10} | Superficie: {p['superficie']:10} | {p['continente']}")


# --- FUNCIÓN PRINCIPAL ---
def main():
    # NOTA: Carga inicial de datos desde el CSV al inicio del programa.
    # NOTA: Ahora devuelve la ruta completa del archivo para evitar crear archivos duplicados al guardar.
    paises, archivo_csv = cargar_paises("Paises.csv")
    if len(paises) == 0:
        print("No se pudieron cargar los datos. Verifique el archivo CSV.")
        return

    while True: # NOTA: Bucle principal que mantiene el programa en ejecución hasta que el usuario elija "0".
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip() # NOTA: Captura la opción y elimina espacios.

        # --- OPCIÓN 1: BUSCAR POR NOMBRE ---
        if opcion == "1":
            nombre = input("Ingrese nombre o parte del nombre del país: ").strip()
            if len(nombre) > 0:
                resultado = buscar_pais(paises, nombre) # NOTA: Llama a la función de búsqueda (usa normalización de texto).
                mostrar_paises(resultado)
            else:
                print("Error: debe ingresar un nombre válido.")

        # --- OPCIÓN 2: FILTRAR POR CONTINENTE ---
        elif opcion == "2":
            cont = input("Ingrese continente: ").strip()
            if len(cont) > 0:
                resultado = filtrar_por_continente(paises, cont) # NOTA: Llama a la función de filtro (clave para América/África).
                mostrar_paises(resultado)
            else:
                print("Error: debe ingresar un continente válido.")

        # --- OPCIÓN 3: FILTRAR POR POBLACIÓN ---
        elif opcion == "3":
            try:
                min_pob = int(input("Población mínima: "))
                max_pob = int(input("Población máxima: "))
                # NOTA: Validaciones de rango (no negativos, mínimo < máximo).
                if min_pob < 0 or max_pob < 0:
                    print("Error: los valores no pueden ser negativos.")
                elif min_pob > max_pob:
                    print("Error: el mínimo no puede ser mayor que el máximo.")
                else:
                    resultado = filtrar_por_rango(paises, "poblacion", min_pob, max_pob) # NOTA: Filtra por la clave "poblacion".
                    mostrar_paises(resultado)
            except ValueError:
                print("Error: debe ingresar valores numéricos.")

        # --- OPCIÓN 4: FILTRAR POR SUPERFICIE ---
        elif opcion == "4":
            try:
                min_sup = int(input("Superficie mínima: "))
                max_sup = int(input("Superficie máxima: "))
                # NOTA: Validaciones de rango (no negativos, mínimo < máximo).
                if min_sup < 0 or max_sup < 0:
                    print("Error: los valores no pueden ser negativos.")
                elif min_sup > max_sup:
                    print("Error: el mínimo no puede ser mayor que el máximo.")
                else:
                    resultado = filtrar_por_rango(paises, "superficie", min_sup, max_sup) # NOTA: Filtra por la clave "superficie".
                    mostrar_paises(resultado)
            except ValueError:
                print("Error: debe ingresar valores numéricos.")

        # --- OPCIÓN 5: ORDENAR PAÍSES ---
        elif opcion == "5":
            clave = input("Ordenar por (nombre/poblacion/superficie): ").strip().lower()
            # NOTA: Valida que la clave de ordenamiento sea una de las permitidas.
            if clave not in ["nombre", "poblacion", "superficie"]: 
                print("Clave inválida.")
            else:
                sentido = input("¿Descendente? (s/n): ").strip().lower()
                descendente = sentido == "s" # NOTA: True si el usuario ingresa 's'.
                resultado = ordenar_paises(paises, clave, descendente) # NOTA: Llama a la función de ordenamiento (burbuja).
                mostrar_paises(resultado)

        # --- OPCIÓN 6: MOSTRAR ESTADÍSTICAS ---
        elif opcion == "6":
            est = estadisticas(paises) # NOTA: Obtiene el diccionario con todas las estadísticas.
            if est:
                # NOTA: Imprime los resultados de las estadísticas de forma formateada.
                print(f"\nPaís con mayor población: {est['mayor_poblacion']['nombre']} ({est['mayor_poblacion']['poblacion']})")
                print(f"País con menor población: {est['menor_poblacion']['nombre']} ({est['menor_poblacion']['poblacion']})")
                print(f"Población promedio: {est['promedio_poblacion']:.2f}")
                print(f"Superficie promedio: {est['promedio_superficie']:.2f}")
                print("\nCantidad de países por continente:")
                for cont, cant in est["cantidad_por_continente"].items():
                    print(f"  {cont}: {cant}")

        # --- OPCIÓN 7: AGREGAR PAÍS ---
        elif opcion == "7":
            # NOTA: Usa la ruta completa del archivo para guardar en la misma ubicación donde se cargó.
            agregar_pais(paises, archivo_csv)

        # --- OPCIÓN 0: SALIR ---
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        
        # --- OPCIÓN INVÁLIDA ---
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    # NOTA: Punto de inicio del script. Solo se ejecuta cuando se corre directamente.
    main()
