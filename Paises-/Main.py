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
    if not lista:
        print("No se encontraron resultados.")
        return
    for p in lista:
        print(f"{p['nombre']:} | Población: {p['poblacion']:} | Superficie: {p['superficie']:} | {p['continente']}")


def main():
    
    archivo_csv = "c:\\Users\\Luciano Nicolas\\Documents\\GitHub\\Trabajo-integrador-Programacion-\\Paises-\\Paises.csv"
    paises = cargar_paises(archivo_csv)
    if not paises:
        print("No se pudieron cargar los datos. Verifique el archivo CSV.")
        return

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese nombre o parte del nombre del país: ")
            resultado = buscar_pais(paises, nombre)
            mostrar_paises(resultado)

        elif opcion == "2":
            cont = input("Ingrese continente: ")
            resultado = filtrar_por_continente(paises, cont)
            mostrar_paises(resultado)

        elif opcion == "3":
            try:
                min_pob = int(input("Población mínima: "))
                max_pob = int(input("Población máxima: "))
                resultado = filtrar_por_rango(paises, "poblacion", min_pob, max_pob)
                mostrar_paises(resultado)
            except ValueError:
                print("Error: debe ingresar valores numéricos.")

        elif opcion == "4":
            try:
                min_sup = int(input("Superficie mínima: "))
                max_sup = int(input("Superficie máxima: "))
                resultado = filtrar_por_rango(paises, "superficie", min_sup, max_sup)
                mostrar_paises(resultado)
            except ValueError:
                print("Error: debe ingresar valores numéricos.")

        elif opcion == "5":
            clave = input("Ordenar por (nombre/poblacion/superficie): ").lower()
            sentido = input("¿Descendente? (s/n): ").lower() == "s"
            if clave in ["nombre", "poblacion", "superficie"]:
                resultado = ordenar_paises(paises, clave, sentido)
                mostrar_paises(resultado)
            else:
                print("Clave inválida.")

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
            # Llama a la función centralizada en funciones.py
            agregar_pais_manual(paises, archivo_csv)

        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
