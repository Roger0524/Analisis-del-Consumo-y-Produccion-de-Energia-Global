# Análisis del Consumo y Producción de Energía Global con Apache Spark

## 📘 Descripción General
Este proyecto utiliza **Apache Spark** para procesar y analizar un conjunto de datos de gran volumen relacionado con el consumo, producción y fuentes de energía en más de 200 países.  
Los datos fueron obtenidos de **Our World in Data – Energy**, elaborados por la Universidad de Oxford, y permiten estudiar la transición hacia fuentes sostenibles y bajas en carbono.

## ⚙️ Tecnologías Utilizadas
- Apache Spark 3.x  
- HDFS (Hadoop Distributed File System)  
- Apache Kafka  
- PySpark (Python 3.x)  
- JDK 11  
- Linux / Ubuntu (VirtualBox)

## 🧾 Dataset
- **Fuente:** [Our World in Data – Energy](https://ourworldindata.org/energy)  
- **Formato:** CSV  
- **Variables clave:** `country`, `year`, `energy_per_capita`, `renewables_share_energy`, `gdp`, entre otras.  
- **Registros:** 23,195  
- **Tamaño:** ~9 MB  

## 🚀 Procesamiento Batch
1. Carga del dataset desde HDFS.  
2. Limpieza de datos (valores nulos, duplicados, formatos).  
3. Creación de una nueva columna (`energy_per_gdp`).  
4. Análisis exploratorio (estadísticas y promedios por país).  
5. Almacenamiento de resultados en formato **Parquet** en HDFS.

## ⚡ Procesamiento en Tiempo Real
- **Apache Kafka:** Se configuró un *topic* para simular la llegada de datos energéticos en tiempo real.  
- **Spark Streaming:** Consume los datos desde Kafka, calcula métricas dinámicas y muestra resultados en consola.  

## 🏢 Arquitectura de la Solución
La solución se compone de las siguientes capas:
1. **Ingesta de Datos:** HDFS (CSV original) y Kafka (datos en streaming).  
2. **Procesamiento Batch:** Spark SQL y DataFrames.  
3. **Procesamiento en Tiempo Real:** Spark Streaming + Kafka Consumer.  
4. **Almacenamiento:** HDFS (formato Parquet).  
5. **Visualización:** Consola y gráficos básicos (EDA).

## 🖼️ Capturas de Resultados
- `docs/Captura_EDA.png` – Estadísticas básicas del dataset.  
- `docs/Captura_HDFS.png` – Resultados almacenados en HDFS.  
- `docs/Captura_Streaming.png` – Ejecución de Spark Streaming.

## 👦 Autor
**Roger Andres Saumeth Visbal**  
*Big Data*  
Universidad Nacional Abierta y a Distancia
2025
