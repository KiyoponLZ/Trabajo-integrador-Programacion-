# Trabajo-integrador-Programacion-
El trabajo para finalizar esta materia
Proyecto Python – Análisis de Países
Descripción del programa

Este proyecto consiste en un programa desarrollado en Python que permite analizar y gestionar información sobre distintos países a partir de un archivo CSV.
El objetivo principal fue aplicar los conceptos aprendidos de listas, diccionarios, funciones, archivos y modularización, para crear un sistema capaz de realizar búsquedas, filtros, ordenamientos y cálculos estadísticos sobre los datos.

El programa está diseñado para ser fácil de usar, presentando un menú con distintas opciones y trabajando con datos almacenados en una estructura clara y ordenada.

Estructura del proyecto

El proyecto se encuentra dividido en varios archivos con funciones específicas, lo que facilita su comprensión y mantenimiento:

main.py → Contiene el menú principal, gestiona las opciones del usuario y muestra los resultados.

funciones.py → Incluye todas las funciones necesarias para el funcionamiento del programa (búsqueda, filtrado, ordenamiento, estadísticas, carga de datos, etc.).

Paises.csv → Archivo de datos que contiene información sobre cada país.

README.md → Documento con la descripción, funcionamiento y detalles del proyecto.

Instrucciones de uso

Asegurarse de tener instalado Python 3.10 o superior.

Descargar todos los archivos del repositorio y mantenerlos dentro de la misma carpeta (el programa busca automáticamente el archivo CSV).

Abrir una terminal en la carpeta del proyecto y ejecutar el comando:

python main.py


Seguir las instrucciones que aparecen en pantalla para navegar por el menú.

El programa permite realizar distintas acciones sobre los datos cargados, como buscar, filtrar, ordenar o agregar países.

Estructura de datos utilizada

El programa utiliza una lista de diccionarios para almacenar la información de los países.
Cada elemento de la lista representa un país con los siguientes campos:

{
  "nombre": "Argentina",
  "poblacion": 45376763,
  "superficie": 2780400,
  "continente": "América"
}


Esta estructura facilita el acceso a los datos, la búsqueda y el filtrado por diferentes criterios.

Funcionalidades principales

El sistema permite realizar las siguientes operaciones:

Cargar datos desde un archivo CSV de manera automática.

Buscar países por texto dentro del nombre.

Filtrar países por continente o por rangos de población o superficie.

Ordenar países por nombre, población o superficie, tanto ascendente como descendente.

Obtener estadísticas, como:

País con mayor y menor población

Promedio de población y superficie

Cantidad de países por continente

Agregar un nuevo país manualmente, que se guarda también en el archivo CSV.

Ejemplos de ejecución

Ejemplo 1: Búsqueda por nombre

Ingrese texto: ar
Resultados:
- Argentina
- Paraguay


Ejemplo 2: Estadísticas

País con mayor población: China
País con menor población: Islandia
Promedio de población: 45.321.000
Promedio de superficie: 985.000 km²
Países por continente:
América: 18
Europa: 14
Asia: 10
África: 9
Oceanía: 5


Ejemplo 3: Agregar un país

Nombre del país: Noruega
Continente: Europa
Población: 5421241
Superficie: 385207
País agregado correctamente y guardado en el CSV.

Participación de los integrantes

El proyecto fue desarrollado de manera grupal. Cada integrante colaboró en distintas etapas del trabajo:

Maxi → Diseño del menú principal y pruebas generales.

Maisi → Redacción del marco teórico y documentación.

Leo → Desarrollo de funciones de búsqueda y filtrado.

Lauti → Implementación del ordenamiento manual y validaciones.

Nico → Carga automática del CSV y estadísticas generales y estructura del codigo

Mai → Redacción de conclusiones y apoyo en la exposición del video , desarollo de validaciones y correciones del codigo

Conclusiones grupales

A lo largo del desarrollo del proyecto aprendimos a trabajar con datos estructurados, a modularizar el código y a organizar la lógica del programa en distintas funciones para hacerlo más claro y reutilizable.
También comprendimos la importancia de los comentarios, la validación de datos y la lectura de archivos externos.

Este trabajo nos permitió afianzar los conceptos fundamentales de programación en Python, como el uso de listas y diccionarios, el manejo de archivos y la creación de programas con estructura y propósito.

