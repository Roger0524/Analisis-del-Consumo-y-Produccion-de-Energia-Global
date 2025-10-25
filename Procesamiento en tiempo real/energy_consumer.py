from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("EnergyStreaming") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

schema = StructType([
    StructField("country_id", IntegerType()),
    StructField("energy_consumption", FloatType()),
    StructField("renewable_percentage", FloatType()),
    StructField("timestamp", TimestampType())
])

df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "Streaming_OWD_Energy") \
    .load()

parsed_df = df.select(
    from_json(col("value").cast("string"), schema).alias("data")
).select("data.*")

windowed_stats = parsed_df \
    .groupBy(
        window(col("timestamp"), "1 minute"),
        col("country_id")
    ) \
    .agg(
        avg("energy_consumption").alias("avg_energy"),
        avg("renewable_percentage").alias("avg_renewable"),
        count("*").alias("total_records")
    )

query = windowed_stats \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
