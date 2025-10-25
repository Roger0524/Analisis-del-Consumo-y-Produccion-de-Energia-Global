import time
import json
import random
from kafka import KafkaProducer

def generate_energy_data():
    return {
        "country_id": random.randint(1, 5),
        "energy_consumption": round(random.uniform(1000, 50000), 2),
        "renewable_percentage": round(random.uniform(10, 80), 2),
        "timestamp": int(time.time())
    }

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

print("Iniciando generador de datos...")

try:
    while True:
        energy_data = generate_energy_data()
        producer.send('Streaming_OWD_Energy', value=energy_data)
        print(f"Enviado: {energy_data}")
        time.sleep(3)
        
except KeyboardInterrupt:
    print("Deteniendo generador...")
finally:
    producer.close()
