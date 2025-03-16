import random
import paho.mqtt.client as mqtt
import time
import schedule

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
        client.subscribe('windmolen/data')
    else:
        print(f'Bad connection. Code: {rc}')
        
def on_message(mqtt_client, userdata, msg):
    return msg.topic, msg.payload
        
def send_request(request_message):
    client.publish('windmolen/request', request_message)
    print(f"Request published on topic {'windmolen/request'}: {request_message}")

def generate_wind_direction():
    directions = ['North', 'South', 'East', 'West']
    return random.choice(directions)

def generate_windmill():
    windmill = ['Windmolen_1', 'Windmolen_2', 'Windmolen_3', 'Windmolen_4']
    return random.choice(windmill)

def determine_by_used(amount_used):
    threshold_used = 700  
    return amount_used > threshold_used

def determine_by_wind_force(wind_force):
    threshold_wind = 30  
    return wind_force <= threshold_wind

def on_disconnect(client, userdata, rc):
    print(f'Disconnected with result code {rc}')

def send_request(request_message):
    client.publish('windmolen/request', request_message)
    print(f"Request published on topic {'windmolen/request'}: {request_message}")

def prod():
     
    wind_direction = generate_wind_direction()
    wind_intensity = random.randint(0, 50)  
 
    used_amount = random.uniform(0, 1000)
    
    status =  "On" if determine_by_used(used_amount) or determine_by_wind_force(wind_intensity) else "Off"
    windmill = generate_windmill()  
    
    # Print the results
    # print(f"The wind comes from the {wind_direction}.")
    # print(f"Amount used by the company: {used_amount}")
    # print(f"The wind has an intensity of {wind_intensity}.")
    # print(f"Status: {status}")

    client.on_disconnect = on_disconnect

    client.connect("localhost", 1883, 60)    
    
    mes = 'status:'+str(windmill)+':'+str(status)+':'+str(wind_direction)+':'+str(used_amount)+':'+str(wind_intensity)
    client.on_connect = on_connect
    client.on_message = on_message
    
    send_request(mes)
    
    client.loop_stop()
    client.disconnect()

client = mqtt.Client()
client.username_pw_set(username="wind", password="molen")
prod()

schedule.every(1).minutes.do(prod)

while True:
    schedule.run_pending()
    time.sleep(1)

