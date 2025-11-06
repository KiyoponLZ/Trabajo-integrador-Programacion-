from funciones import *


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


def mostrar_paises(lista):
    if len(lista) == 0:
        print("No se encontraron resultados.")
        return
    for p in lista:
        print(f"{p['nombre']:15} | Población: {p['poblacion']:10} | Superficie: {p['superficie']:10} | {p['continente']}")


def main():
    paises = cargar_paises("Paises.csv")
    if len(paises) == 0:
        print("No se pudieron cargar los datos. Verifique el archivo CSV.")
        return

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Ingrese nombre o parte del nombre del país: ").strip()
            if len(nombre) > 0:
                resultado = buscar_pais(paises, nombre)
                mostrar_paises(resultado)
            else:
                print("Error: debe ingresar un nombre válido.")

        elif opcion == "2":
            cont = input("Ingrese continente: ").strip()
            if len(cont) > 0:
                resultado = filtrar_por_continente(paises, cont)
                mostrar_paises(resultado)
            else:
                print("Error: debe ingresar un continente válido.")

        elif opcion == "3":
            try:
                min_pob = int(input("Población mínima: "))
                max_pob = int(input("Población máxima: "))
                if min_pob < 0 or max_pob < 0:
                    print("Error: los valores no pueden ser negativos.")
                elif min_pob > max_pob:
                    print("Error: el mínimo no puede ser mayor que el máximo.")
                else:
                    resultado = filtrar_por_rango(paises, "poblacion", min_pob, max_pob)
                    mostrar_paises(resultado)
            except ValueError:
                print("Error: debe ingresar valores numéricos.")

        elif opcion == "4":
            try:
                min_sup = int(input("Superficie mínima: "))
                max_sup = int(input("Superficie máxima: "))
                if min_sup < 0 or max_sup < 0:
                    print("Error: los valores no pueden ser negativos.")
                elif min_sup > max_sup:
                    print("Error: el mínimo no puede ser mayor que el máximo.")
                else:
                    resultado = filtrar_por_rango(paises, "superficie", min_sup, max_sup)
                    mostrar_paises(resultado)
            except ValueError:
                print("Error: debe ingresar valores numéricos.")

        elif opcion == "5":
            clave = input("Ordenar por (nombre/poblacion/superficie): ").strip().lower()
            if clave not in ["nombre", "poblacion", "superficie"]:
                print("Clave inválida.")
            else:
                sentido = input("¿Descendente? (s/n): ").strip().lower()
                descendente = sentido == "s"
                resultado = ordenar_paises(paises, clave, descendente)
                mostrar_paises(resultado)

        elif opcion == "6":
            est = estadisticas(paises)
            if est:
                print(f"\nPaís con mayor población: {est['mayor_poblacion']['nombre']} ({est['mayor_poblacion']['poblacion']})")
                print(f"País con menor población: {est['menor_poblacion']['nombre']} ({est['menor_poblacion']['poblacion']})")
                print(f"Población promedio: {est['promedio_poblacion']:.2f}")
                print(f"Superficie promedio: {est['promedio_superficie']:.2f}")
                print("\nCantidad de países por continente:")
                for cont, cant in est["cantidad_por_continente"].items():
                    print(f"  {cont}: {cant}")

        elif opcion == "7":
            agregar_pais(paises, "Paises.csv")

        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()