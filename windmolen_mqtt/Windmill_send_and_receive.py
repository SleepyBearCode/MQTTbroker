import paho.mqtt.client as mqtt
import json
import random
import time

import schedule

def get_random_row(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    if isinstance(data, list) and len(data) > 0:
        random_index = random.randint(0, len(data) - 1)
        random_row = data[random_index]
        
        if random_row['status'] != False:
            random_row["produceert"] = random.randint(100, 1500)
            random_row["gemiddelde_productie"] = random.randint(100, 20000)
        else: 
            random_row["produceert"] = 0 
            random_row["gemiddelde_productie"] = random.randint(100, 20000)
        
        return random_row 
    else:
        print("Error: The JSON data is not a non-empty list.")
        
def on_connect(client, userdata, flags, rc):
    print("Verbonden met de broker met resultaatcode " + str(rc))
    clientone.subscribe("windmolen/request")

def on_message(client, userdata, msg):
    ans1,ans2,ans3,ans4,ans5,ans6 =  msg.payload.decode().split(':')
    if ans1 == "data":
        job()
    else:
        changeWindmil(ans2,ans3,ans4)         

def on_publish(client, userdata, mid):
    print("Message Published")
 
def changeWindmil(windmil,status,facing):
    file_path = 'windmolen_mqtt\Windmills.json'

    with open(file_path, 'r') as file:
        data_list = json.load(file)

    for entry in data_list:
        if entry["windmolen"] == windmil:
            entry["status"] = status
            entry["facing"] = facing
            break

    with open(file_path, 'w') as file:
        json.dump(data_list, file, indent=2)

    
def job():
    json_file_path = 'windmolen_mqtt\Windmills.json' 
    random_row = get_random_row(json_file_path)

    if random_row:
        broker_address = "localhost"  
        port = 1883  
        topic = "windmolen/data"  
        
        clienttwo = mqtt.Client()
        clienttwo.username_pw_set(username="wind", password="molen")
        clienttwo.on_connect = on_connect
        clienttwo.on_publish = on_publish
        
        # Maak verbinding met de MQTT-broker
        clienttwo.connect(broker_address, port, 60)

        payload = json.dumps(random_row)
        clienttwo.publish(topic, payload)
        time.sleep(2)

        clienttwo.disconnect()

# MQTT-configuratie
broker_adres = "localhost" 
poort = 1883  

# Maak een MQTT-client en stel de callbacks in
clientone = mqtt.Client()
clientone.on_connect = on_connect
clientone.on_message = on_message
clientone.username_pw_set(username="wind", password="molen")

# Maak verbinding met de MQTT-broker
clientone.connect(broker_adres, poort, 60)

# Start de MQTT-loop om berichten te ontvangen
clientone.loop_start()

schedule.every(5).minutes.do(job)

try:
    while True:
        schedule.run_pending()
        time.sleep(1)  
except KeyboardInterrupt:
    clientone.disconnect()
