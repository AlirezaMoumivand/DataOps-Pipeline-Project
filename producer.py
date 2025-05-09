from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

data = [
    {"id": "123", "full_name": "Ali",
        "timestamp": "2025/01/31 12:34:56", "active": "true"},
    {"id": "124", "full_name": " ", "timestamp": "2025-01-31T14:20:00Z",
        "active": "false", "extra_field": "remove"}
]

for item in data:
    producer.send('test_pipeline', item)

producer.flush()
