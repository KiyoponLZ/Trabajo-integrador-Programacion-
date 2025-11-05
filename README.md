# Trabajo-integrador-Programacion-
El trabajo para finalizar esta materia(por ahora)
Proyecto Python – Análisis de Países


Descripción del proyecto

Este proyecto consiste en un programa desarrollado en Python que trabaja con un archivo CSV llamado Paises.csv, el cual contiene información sobre distintos países del mundo: nombre, población, superficie y continente.

El objetivo es permitir al usuario buscar, filtrar, ordenar y analizar los datos de forma interactiva desde un menú, aplicando estructuras de datos y técnicas de programación vistas a lo largo del año.

El programa fue diseñado para ser modular, legible y portátil, de manera que pueda ejecutarse en cualquier computadora sin necesidad de modificar rutas ni configuraciones.

Funcionamiento interno del programa

El programa inicia en el archivo main.py, que muestra un menú principal con distintas opciones para el usuario.

Cuando el usuario selecciona una opción, se llama a una función específica que está definida en funciones.py.

Estas funciones trabajan con una lista de diccionarios llamada paises, donde cada diccionario representa un país con sus respectivos datos.

Al iniciar, el programa carga automáticamente los datos desde el archivo Paises.csv utilizando el módulo os para encontrar la ruta correcta del archivo, incluso si el proyecto se mueve de carpeta.

Dependiendo de la opción elegida, el programa puede:

Buscar países por nombre.

Filtrar por continente o por rango (población o superficie).

Ordenar la lista según distintos criterios.

Calcular estadísticas generales (mayor y menor población, promedios, cantidad por continente).

Agregar un país nuevo validando los datos ingresados.

Si se agrega un nuevo país, los cambios se guardan automáticamente en el archivo Paises.csv.

Finalmente, el programa muestra los resultados por pantalla y vuelve al menú hasta que el usuario decida salir.

Estructura del proyecto

El proyecto está dividido en dos módulos principales para mantener un código organizado y fácil de mantener:

main.py → Contiene el menú principal y la interacción directa con el usuario.

funciones.py → Incluye todas las funciones que ejecutan tareas específicas (búsquedas, filtros, cálculos, etc.).

Esta modularización permite trabajar de forma ordenada, entender mejor cada parte del código y repartir el trabajo entre los integrantes del grupo.

Proyecto-Paises/
├── main.py
├── funciones.py
├── Paises.csv
└── README.md

Instrucciones de uso

Descargar todos los archivos del proyecto en una misma carpeta.

Verificar que el archivo Paises.csv esté en esa carpeta.

Abrir el archivo main.py con Python (por ejemplo, desde Visual Studio Code o IDLE).

Ejecutar el programa con el siguiente comando:

python main.py


Desde el menú, elegir la acción deseada (buscar, filtrar, ordenar, mostrar estadísticas o agregar país).

Ejemplos de entrada y salida
Ejemplo 1 – Buscar un país

Entrada:

Ingrese nombre o parte del nombre del país: Arg


Salida esperada:

País encontrado: Argentina
Población: 45.376.763
Superficie: 2.780.400 km²
Continente: América

Ejemplo 2 – Filtrar por continente

Entrada:

Ingrese continente: Europa


Salida esperada:

Países del continente Europa:
- España
- Francia
- Alemania
- Italia

Ejemplo 3 – Mostrar estadísticas

Salida esperada:

País con mayor población: China (1.410.000.000)
País con menor población: Islandia (372.000)
Promedio de población: 82.000.000
Promedio de superficie: 650.000 km²
Cantidad de países por continente:
- América: 12
- Europa: 15
- Asia: 20
- África: 10
- Oceanía: 5

Ejemplo 4 – Agregar un país

Entrada:

Nombre del país: Andorra
Continente: Europa
Población: 77000
Superficie: 468


Salida esperada:

País agregado correctamente y guardado en el CSV.

Integrantes del grupo y tareas realizadas

Maximiliano Reinoso: Intervencion en las Validaciones Presentación general del proyecto y explicación del objetivo principal.

Maximiliano Méndez: Desarolo de las Funciones , Desarrollo del marco teórico y explicación de las estructuras de datos utilizadas.

Leo Fachinelli: Diseño de la estructura del código y organización de la modularización entre main.py y funciones.py.

Lautaro Fernández: Implementación y explicación del sistema de carga automática del archivo CSV.

Nicolás Ibañez: Armado del cuerpo del codigo ,Demostración práctica del programa y explicación de las funciones principales.

Mailén Ortiz: Correciones y ayuda en el estructurado del codigo ,Conclusión y reflexión final sobre los aprendizajes del grupo.

Conclusión grupal

En conclusión, este proyecto fue una gran oportunidad para aplicar todo lo aprendido durante el año, tanto en programación como en trabajo en equipo.
Desde el principio entendimos que no se trataba solo de escribir código, sino de comprender el proceso completo: desde la planificación hasta las pruebas y correcciones.

Aprendimos a manejar estructuras de datos como listas y diccionarios, que fueron esenciales para organizar la información de los países, y también a trabajar con archivos CSV, algo muy útil y frecuente en proyectos reales.
Dividimos el código en funciones, lo que hizo que fuera más claro y ordenado, permitiéndonos colaborar sin pisarnos el trabajo.

Tuvimos algunos desafíos, como lograr que el programa funcione en cualquier computadora o mantener las funciones separadas correctamente, pero eso nos sirvió para investigar y aprender a resolver problemas de manera independiente.
También tratamos de que el programa no solo funcione bien, sino que sea entendible y amigable para cualquier usuario.

En general, este trabajo nos ayudó a mejorar la lógica, la organización y la comunicación grupal.
Más allá del resultado técnico, lo más importante fue el aprendizaje que nos llevamos: cómo planificar, dividir responsabilidades y construir un programa completo desde cero.
Sentimos que todo el esfuerzo valió la pena y que este proyecto refleja el progreso que logramos durante todo el año.
Muchas gracias por ver nuestra presentación y acompañarnos en este proceso.