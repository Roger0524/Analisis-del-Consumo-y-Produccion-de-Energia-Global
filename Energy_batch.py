# Importar librerías
from pyspark.sql import SparkSession, functions as F

# 1. Crear la sesión de Spark
spark = SparkSession.builder.appName("Tarea3_OWD_Energy").getOrCreate()

# 2. Definir la ruta del archivo CSV
file_path = "hdfs://localhost:9000/Tarea3/OWD_Energy.csv"

# 3. Cargar el dataset
df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(file_path)

# 4. Mostrar esquema y tres primeros registros
df.printSchema()
df.show(3)

# 5. Limpieza de datos
df = df.dropna(subset=["country", "year"])
df = df.fillna(0)

# 6. Crear columna con consumo energético por PIB
if "energy_per_capita" in df.columns and "gdp" in df.columns:
    df = df.withColumn("energy_per_gdp", F.col("energy_per_capita") / F.when(F.col("gdp") == 0, None).otherwise(F.col("gdp")))

# 7. Análisis exploratorio básico (EDA)
print("=== Estadísticas básicas ===")
df.describe(["energy_per_capita", "renewables_share_energy", "gdp"]).show()

print("=== Promedio de energía per cápita por país ===")
df.groupBy("country").agg(F.avg("energy_per_capita").alias("promedio_energia_pc")) \
  .orderBy(F.desc("promedio_energia_pc")).show(10, False)

# 8. Guardar resultados procesados
output_path = "hdfs://localhost:9000/Tarea3/Resultado_OWD_Energy"
df.write.mode("overwrite").parquet(output_path)

print(f"\nProcesamiento finalizado")

# 9. Cerrar sesión Spark
spark.stop()