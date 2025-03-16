import paho.mqtt.client as mqtt

client = mqtt.Client()
client.username_pw_set(username="wind", password="molen")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
        client.subscribe('windmolen/data')
        client.subscribe('windmolen/request')
    else:
        print(f'Bad connection. Code: {rc}')
        # You might want to implement reconnection logic here

def on_message(mqtt_client, userdata, msg):
    return msg.topic, msg.payload

# Function to send a request for new data
def send_request(request_message):
    # Publish a request on the request topic
    client.publish('windmolen/request', request_message)
    print(f"Request published on topic {'windmolen/request'}: {request_message}")

client.on_connect = on_connect
client.on_message = on_message

def on_disconnect(client, userdata, rc):
    print(f'Disconnected with result code {rc}')
    # You might want to implement reconnection logic here

client.on_disconnect = on_disconnect

client.connect("localhost", 1883, 60)

client.loop_start()
