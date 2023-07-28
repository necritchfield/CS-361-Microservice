# CS-361-Microservice

Communication is handled via a RabbitMQ queue. I used the RabbitMQ tutorial as a template for both sending and receiving: https://www.rabbitmq.com/tutorials/tutorial-one-python.html

Requesting Data: The name of the request queue is send_expr. Requests should be sent as strings in the form "expr val," with expr being "sqrt" for square roots and "sq" for squares. So to get the square root of 16, send "sqrt 16," and to get the square of 4 send "sq 4." Any other calculations should happen in the calculator itself, e.g. "sqrt 2 + 2" wouldn't work, "2 + 2" would need to be evaluated before sending the request (or after for "sqrt(2) + 2").

Receiving Data: The name of the receiving queue is send_result. The result will be sent back in the form of a stringified float, e.g. "sqrt 16" will return "4.0." When the send_expr server receives a request, the result is calculated and sent back automatically, so you'll want to have the receiver set up and listening before sending over any requests.

![image](https://github.com/necritchfield/CS-361-Microservice/assets/127362771/f74a83ca-b476-426d-a5d1-db8a5e220845)
