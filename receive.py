#!/usr/bin/env python
import pika, sys, os, squares

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='send_expr')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
        
        # parse message, carry out function
        message = body.decode()
        req = message.split()
        op = req[0]
        num = req[1]
        if (op == "sqrt"):
            result = str(squares.square_root(num))
        elif (op == "sq"):
            result = str(squares.square(num))
        
        # make new connection to send result
        connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='send_result')

        channel.basic_publish(exchange='', routing_key='send_result', body=result)
        print(" [x] Sent " + result)
        connection.close()

    channel.basic_consume(queue='send_expr', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)