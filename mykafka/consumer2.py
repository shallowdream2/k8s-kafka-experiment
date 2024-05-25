from kafka import KafkaConsumer
import json

# 创建Kafka消费者
consumer = KafkaConsumer('test-topic-2',
                         bootstrap_servers='kafka:9092',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# 处理消息
for message in consumer:
    print(f'Consumer2 received: {message.value}')
