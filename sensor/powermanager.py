import random
import paho.mqtt.client as mqtt
import time
import schedule

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
    else:
        print(f'Bad connection. Code: {rc}')

def on_disconnect(client, userdata, rc):
    print(f'Disconnected with result code {rc}')

def send_request(request_message):
    client.publish('solar/request', request_message)
    print(f"Request published on topic {'solar/request'}: {request_message}")

def determine_by_used(amount_used):
    threshold_used = 700  
    return amount_used > threshold_used

def determine_by_sun_force(sun_force):
    threshold_wind = 30  
    return sun_force <= threshold_wind

def generate_sun_direction():
    directions = ['North', 'South', 'East', 'West']
    return random.choice(directions)

def prod():
    
    sun_force = random.uniform(0, 50)  

    used_amount = random.randint(0, 1000)

    sun_facing = generate_sun_direction()
    
    status = "On" if determine_by_used(used_amount) or determine_by_sun_force(sun_force) else "Off"

    # Print the results
    # print(f"Amount used by the company: {used_amount}")
    # print(f"Sun force: {sun_force}")
    # print(f"Sun direction: {sun_facing} ")
    # print(f"Status: {status}")
   
    mes = 'status:'+str(0)+':'+str(status)+':'+str(sun_facing)+':'+str(used_amount)+':'+str(sun_force)
    client.connect("localhost", 1883, 60)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    
    send_request(mes)
    
    client.loop_stop()
    client.disconnect()
    

client = mqtt.Client()
client.username_pw_set(username="solar", password="panel")
prod()

# Schedule the job to run every 2 minute
schedule.every(2).minutes.do(prod)

# Run the scheduled jobs
while True:
    schedule.run_pending()
    time.sleep(1)
