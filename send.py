#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='send_expr')

message = 'sq 4'
channel.basic_publish(exchange='', routing_key='send_expr', body=message)
print(" [x] Sent " + message)
connection.close()