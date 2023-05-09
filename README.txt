CS361 Calorie Calculator Microservice
Author: Jayden Fong
Date: 5/8/2023

HOW TO REQUEST DATA:

To request data from the microservice, you need to send a JSON message containing the following information:

weight: Weight of the person (in kilograms).
height: Height of the person (in centimeters).
age: Age of the person (in years).
gender: Gender of the person ('male' or 'female').
You can make a request to the microservice by sending a JSON message to the TCP socket on port 5555. 
Here's an example using Python:

```
python
Copy code
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

message = {
    'weight': 70,
    'height': 175,
    'age': 30,
    'gender': 'male'
}

socket.send_json(message)

response = socket.recv_json()
caloric_intake = response['caloric_intake']
print("Caloric Intake:", caloric_intake)
```

Replace the values of weight, height, age, and gender with the appropriate values for your request.

HOW TO RECIEVE DATA:
The microservice receives the request, extracts the necessary data, calculates the caloric intake using the provided formula, and sends back the response.

To receive the data from the microservice, you need to create a socket and bind it to a TCP port. In this code, the microservice binds to port 5555. You can connect to this port and receive the response using ZeroMQ REQ socket.

Here's an example of how to receive the response using Python:

```
python
Copy code
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

message = {
    'weight': 70,
    'height': 175,
    'age': 30,
    'gender': 'male'
}

socket.send_json(message)

response = socket.recv_json()
caloric_intake = response['caloric_intake']
print("Caloric Intake:", caloric_intake)\
```

UML SEQUENCE DIAGRAM:
Below is a UML sequence diagram that illustrates the interaction between the client and the microservice for requesting and receiving data.

scss
Copy code
  Client                         Microservice
    |                                 |
    |--------(1. Request)------------>|
    |                                 |
    |<-------(2. Response)------------|
    |                                 |
The client sends a request to the microservice by sending a JSON message containing the required data.
The microservice receives the request, extracts the necessary data, calculates the caloric intake, and sends back the response containing the calculated caloric intake.
Note: The diagram represents a simplified view of the interaction between the client and the microservice and does not include error handling or other details.

