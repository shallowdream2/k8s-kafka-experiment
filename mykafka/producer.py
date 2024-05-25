from kafka import KafkaProducer
import time
import json

# 创建Kafka生产者
producer = KafkaProducer(bootstrap_servers='kafka:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))


# 生成消息并发送到Kafka
while True:
    message1 = {'message1': 'Hello Kafka, send to 1', 'timestamp': time.time()}
    message2 = {'message2': 'Hello Kafka, send to 2', 'timestamp': time.time()}
    producer.send('test-topic', value=message1)
    producer.send('test-topic-2', value=message2)
    print(f'Sent: {message1}')
    print(f'Sent: {message2}')
    time.sleep(5)
