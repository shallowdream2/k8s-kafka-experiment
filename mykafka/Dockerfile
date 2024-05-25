# 使用官方的Python基础镜像
FROM python:3.9

# 安装Kafka Python客户端
RUN pip install kafka-python

# 将生产者和消费者脚本复制到容器中
COPY producer.py /app/producer.py
COPY consumer1.py /app/consumer1.py
COPY consumer2.py /app/consumer2.py

WORKDIR /app
