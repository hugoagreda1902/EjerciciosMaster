# Benchmark: Python vs NumPy vs Numba

## Configuración

* Operación: sum((x - mean)**2)
* Tamaño: 10.000.000 elementos
* 3 ejecuciones por versión
* Medición: time.perf_counter()

## Resultados

### Float64

| Versión     | Tiempo medio |
| ----------- | ------------ |
| Python puro | 1.4278 s     |
| NumPy       | 0.0856 s     |
| Numba       | 0.0305 s     |

### Float32

| Versión     | Tiempo medio |
| ----------- | ------------ |
| Python puro | 1.4351 s     |
| NumPy       | 0.0469 s     |
| Numba       | 0.0302 s     |

## Ratios reales obtenidos

* NumPy vs Python en float64: **x16.7**
* NumPy vs Python en float32: **x30.6**
* Numba vs Python: **x46 a x47**
* Numba vs NumPy: entre **x1.6 y x2.8**
* Mejora por usar float32 en NumPy: casi **2 veces** mas rapido

## Conclusiones

1. Python no es lento por definicion.
   El problema es el bucle interpretado elemento a elemento.
   Cuando el calculo se delega a codigo nativo mediante NumPy o Numba, el rendimiento se acerca al de C.

2. La vectorizacion es clave.
   NumPy trabaja sobre memoria contigua y utiliza rutinas optimizadas en C y Fortran, evitando el coste del interprete.

3. Numba demuestra que se puede mantener sintaxis Python con rendimiento casi nativo.
   Compila la funcion a codigo maquina y elimina la sobrecarga del bucle.

4. Float32 frente a Float64.

   * Float32 ocupa la mitad de memoria y mejora el uso de cache.
   * En este experimento casi duplica la velocidad de NumPy.
   * Float64 solo es necesario cuando la precision numerica es critica.

## Leccion aprendida

Optimizar importa cuando:

* existen millones de operaciones repetitivas
* el codigo se ejecuta en produccion de forma continua
* el coste de infraestructura depende del tiempo de CPU

La eleccion adecuada de librerias permite multiplicar el rendimiento por mas de 40 sin abandonar Python ni aumentar la complejidad del codigo.

## Relacion con el proyecto

En el contexto del proyecto de **entrenar un modelo y desplegarlo como API de predicciones**, estos resultados tienen impacto directo.
La API prioriza latencia y coste por peticion, no una precision matematica extrema, por lo que **float32 es la opcion mas adecuada**: reduce casi a la mitad el tiempo de calculo y el consumo de memoria, permitiendo atender mas peticiones por segundo con la misma infraestructura.

El experimento demuestra que la parte critica del sistema no debe implementarse con bucles Python, sino mediante **NumPy o Numba**, que delegan el calculo a codigo nativo.
Esto permite mantener Python como lenguaje principal del proyecto, obteniendo productividad en el entrenamiento y, al mismo tiempo, rendimiento suficiente para un servicio en produccion sin necesidad de reescribir el sistema en C o Java.
