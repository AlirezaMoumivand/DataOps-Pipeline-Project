# DataOps Pipeline Project

This project demonstrates a complete end-to-end real-time data pipeline using Dockerized components including Kafka, Logstash, Elasticsearch, and Kibana. A custom Python producer simulates data ingestion into the pipeline.

## 🚀 Project Overview

This pipeline:
- Ingests raw/malformed data using a Python script.
- Sends data to a Kafka topic (`test_pipeline`).
- Uses Logstash to clean, transform, and forward data to Elasticsearch.
- Stores the processed data in Elasticsearch.
- Visualizes the results in Kibana.
<!--  -->
---

## 🛠️ Technologies Used

- **Kafka + Zookeeper**: For message brokering.
- **Logstash**: For data filtering and transformation.
- **Elasticsearch**: For indexing and storing processed data.
- **Kibana**: For visualization.
- **Python (kafka-python)**: As the data producer.
- **Docker & Docker Compose**: For container orchestration.

---

## 🧾 Sample Input

```json
[
  {"id": "123", "full_name": "Ali", "timestamp": "2025/01/31 12:34:56", "active": "true"},
  {"id": "124", "full_name": " ", "timestamp": "2025-01-31T14:20:00Z", "active": "false", "extra_field": "remove"}
]
```

---

## ✅ Expected Output in Elasticsearch
```json
[
  {"id": 123, "name": "Ali", "timestamp": "2025-01-31T12:34:56Z", "active": true},
  {"id": 124, "name": null, "timestamp": "2025-01-31T14:20:00Z", "active": false}
]
```

---

## 📦 Project Structure

```bash
.
├── docker-compose.yml
├── Dockerfile
├── producer.py
├── requirements.txt
└── logstash.conf
```


## 🧪 How to Run

 1. Clone the repo:
 ```code
git clone https://github.com/your-username/dataops-pipeline-project.git
cd dataops-pipeline-project
 ```

 2. Build and start services:
  ```code
docker-compose up --build
 ```
  
3. Access Services:
- Kafka topic: test_pipeline (created automatically)
- Elasticsearch: http://localhost:9200
- Kibana: http://localhost:5601

## 📊 Validation
- The data indexed in Elasticsearch can be explored through Kibana.
- Check the `test_pipeline` index in Elasticsearch to verify transformed documents.

## 📁 Output
All services are orchestrated with `docker-compose` for one-click startup, ensuring reliable inter-service communication and reproducibility.

## 🧠 Lessons Learned
- Handling malformed and inconsistent input formats.
- Kafka topic and Logstash setup automation.
- Working with Elasticsearch mappings.
- Date and type normalization in Logstash filters.
