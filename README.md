# Escenario elegido: A — Entrenar un modelo y desplegarlo como API para predicciones

---

## Matriz de decisión inicial

| Criterio                                 | Peso | Python  | R      | Java    | Node    |
| ---------------------------------------- | ---- | ------- | ------ | ------- | ------- |
| Ecosistema IA/ML (librerías, comunidad)  | 5    | 5       | 3      | 3       | 3       |
| Productividad / prototipado              | 4    | 5       | 4      | 3       | 4       |
| Rendimiento / latencia                   | 4    | 3       | 2      | 5       | 4       |
| Concurrencia / I-O / servicios           | 4    | 3       | 2      | 5       | 5       |
| Integración Big Data (Spark, conectores) | 3    | 4       | 3      | 5       | 3       |
| Despliegue y portabilidad                | 4    | 4       | 3      | 5       | 4       |
| Mantenibilidad / tipado / tooling        | 3    | 3       | 2      | 5       | 4       |
| Talento disponible (equipo)              | 4    | 5       | 3      | 4       | 4       |
| **TOTAL ponderado**                      |      | **126** | **86** | **133** | **120** |

---

## Ecosistema IA/ML — Peso 5

Es el núcleo del escenario.
Se necesita:

* librerías maduras como TensorFlow, PyTorch y Scikit-learn
* herramientas de validación y evaluación
* serialización del modelo
* comunidad con ejemplos reales

Si el lenguaje falla en este punto, el proyecto es inviable. Se considera un requisito crítico.

### Puntuaciones

* **Python = 5**
  Estándar de facto en IA. Dispone de TensorFlow, PyTorch, Scikit-learn, Pandas y HuggingFace, con documentación extensa y ejemplos para cualquier tipo de modelo.

* **R = 3**
  Muy potente en estadística clásica, pero más limitado en deep learning y en despliegue como API.

* **Java = 3**
  Posee librerías como DL4J o Weka, aunque no es la primera opción para entrenar modelos actuales.

* **Node = 3**
  Existe TensorFlow.js, pero su ecosistema es mucho más reducido que el de Python.

---

## Productividad / prototipado — Peso 4

Antes de construir la API se debe:

* probar numerosos enfoques
* limpiar y transformar datos
* modificar características
* reentrenar modelos

El coste real está en iterar rápido, lo que afecta directamente al tiempo del proyecto.

### Puntuaciones

* **Python = 5** — notebooks, scripts cortos y gran cantidad de ejemplos
* **R = 4** — excelente para análisis, algo menos versátil
* **Java = 3** — demasiado código base para pruebas rápidas
* **Node = 4** — ágil para APIs, pero débil para ML puro

---

## Rendimiento / latencia — Peso 4

Una API de predicción debe:

* responder en milisegundos
* manejar picos de carga
* no bloquear al cliente

Si la latencia es elevada, el modelo pierde utilidad.

### Puntuaciones

* **Java = 5** — JVM optimizada y multihilo real
* **Node = 4** — buen rendimiento I/O con event loop
* **Python = 3** — penalizado por GIL y naturaleza interpretada
* **R = 2** — el menos adecuado para producción

---

## Concurrencia / I-O / servicios — Peso 4

Desplegar como API implica:

* múltiples peticiones simultáneas
* acceso a bases de datos y caché
* colas y balanceadores

### Puntuaciones

* **Java = 5** — hilos, pools y frameworks como Spring
* **Node = 5** — modelo asíncrono muy eficiente
* **Python = 3** — async existente pero limitado
* **R = 2** — orientado a análisis, no a servidores

---

## Integración Big Data — Peso 3

Puede requerirse:

* lectura desde Spark
* conectores con data lake
* pipelines batch

### Puntuaciones

* **Java = 5** — lenguaje nativo de Spark y Kafka
* **Python = 4** — PySpark ampliamente utilizado
* **R = 3** — integración más limitada
* **Node = 3** — posible pero poco estándar

---

## Despliegue y portabilidad — Peso 4

El modelo debe ejecutarse en:

* Docker
* entornos cloud
* CI/CD
* diferentes sistemas

### Puntuaciones

* **Java = 5** — JAR estable y despliegue empresarial
* **Node = 4** — despliegue sencillo
* **Python = 4** — bueno con Docker, dependencias delicadas
* **R = 3** — más complejo para APIs

---

## Mantenibilidad / tipado — Peso 3

A largo plazo se valora:

* código legible
* testing
* tipado

### Puntuaciones

* **Java = 5** — tipado fuerte y arquitectura clara
* **Node = 4** — TypeScript mejora el mantenimiento
* **Python = 3** — tipado opcional
* **R = 2** — menos orientado a software robusto

---

## Talento disponible — Peso 4

Es clave considerar:

* quién mantendrá el sistema
* disponibilidad de perfiles
* conocimiento del equipo

### Puntuaciones

* **Python = 5** — mercado dominante en IA
* **Java = 4** — gran base de desarrolladores backend
* **Node = 4** — muy extendido en web
* **R = 3** — nicho más académico

---

## Conclusión

El lenguaje ganador es **Java (133 puntos)** porque combina alto rendimiento, concurrencia real y un ecosistema sólido para producción e integración con herramientas como Spark o Kafka. En un escenario de API de predicciones, la robustez operativa pesa más que la velocidad de prototipado.

El principal riesgo es la menor agilidad en entrenamiento y experimentación frente a Python. Esto se mitiga con un enfoque híbrido: **Python para entrenar y Java para servir**, usando ONNX/PMML o microservicios. También es viable emplear Java como orquestador y exponer el modelo Python mediante FastAPI o gRPC.

---

# Extensión — Decisión separada por fases y coste de operación

Se añade el criterio **Coste de operación / infraestructura**, que considera consumo de recursos, escalado, licencias y complejidad DevOps.

---

## Matriz 1 — Lenguaje para ENTRENAMIENTO

| Criterio                    | Peso | Python  | R       | Java    | Node   |
| --------------------------- | ---- | ------- | ------- | ------- | ------ |
| Ecosistema IA/ML            | 5    | 5       | 4       | 3       | 2      |
| Productividad / prototipado | 5    | 5       | 4       | 3       | 3      |
| Rendimiento de cálculo      | 3    | 4       | 3       | 4       | 3      |
| Integración Big Data        | 3    | 4       | 3       | 4       | 3      |
| Despliegue del modelo       | 3    | 4       | 3       | 4       | 3      |
| Mantenibilidad              | 3    | 3       | 2       | 5       | 4      |
| Talento disponible          | 4    | 5       | 3       | 4       | 4      |
| Coste operación             | 3    | 4       | 3       | 4       | 3      |
| **TOTAL**                   |      | **128** | **100** | **111** | **96** |

### Conclusión entrenamiento

El ganador es **Python** por su ecosistema dominante y rapidez de experimentación. El coste operativo es razonable gracias a librerías optimizadas y soporte GPU. El riesgo de mantenimiento se reduce con MLOps y contenedores.

---

## Matriz 2 — Lenguaje para DESPLIEGUE

| Criterio                  | Peso | Python  | R      | Java    | Node    |
| ------------------------- | ---- | ------- | ------ | ------- | ------- |
| Rendimiento / latencia    | 5    | 3       | 2      | 5       | 4       |
| Concurrencia e I/O        | 5    | 3       | 2      | 5       | 5       |
| Despliegue y portabilidad | 4    | 4       | 2      | 5       | 4       |
| Integración con servicios | 4    | 3       | 2      | 5       | 4       |
| Mantenibilidad / tipado   | 4    | 3       | 2      | 5       | 4       |
| Ecosistema ML             | 3    | 5       | 3      | 3       | 3       |
| Talento disponible        | 4    | 5       | 3      | 4       | 4       |
| Coste operación           | 4    | 4       | 3      | 5       | 4       |
| **TOTAL**                 |      | **118** | **79** | **140** | **132** |

### Conclusión despliegue

El más adecuado es **Java**, con mejor latencia, concurrencia y menor coste por petición en alta carga, además de herramientas maduras de monitorización.

---

## Conclusión final de la extensión

La solución óptima es **híbrida**:

* **Python para entrenamiento y validación**
* **Java para el servicio en producción**

Este enfoque reduce costes y riesgos, separando ciencia de datos e ingeniería de servicio. La integración puede realizarse con ONNX/PMML o mediante REST/gRPC.
