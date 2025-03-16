from django.shortcuts import render
from django.shortcuts import redirect
import time
from . import mqttWindmill as mqttwind
from . import mqttSolar as mqttsolar

class MessageContainer:
    def __init__(self):
        self.messages = []  # List to store incoming messages

message_windmill = MessageContainer()
message_solar = MessageContainer()
message_sensor = MessageContainer()

def w_on_messages(client, userdata, msg):
    if(msg.topic == "windmolen/data"):
        # Append the incoming message to the list
        message_windmill.messages.append({
            'topic': msg.topic,
            'payload': msg.payload.decode('utf-8')
        })
    else:
        # Append the incoming message to the list
        message_sensor.messages.append({
            'topic': msg.topic,
            'payload': msg.payload.decode('utf-8')
        })
        
def s_on_messages(client, userdata, msg):
    print(msg.topic)
    if(msg.topic == "solar/data"):
        # Append the incoming message to the list
        message_solar.messages.append({
            'topic': msg.topic,
            'payload': msg.payload.decode('utf-8')
        })
    else:
        # Append the incoming message to the list
        message_sensor.messages.append({
            'topic': msg.topic,
            'payload': msg.payload.decode('utf-8')
        })

mqttwind.client.on_message = w_on_messages
mqttsolar.client.on_message = s_on_messages

def w_display_message(request):
    mqttwind.client.on_message = w_on_messages
    return render(request, 'index.html', {'subject':'windmill','messages_device': message_windmill.messages, 'messages_sensor':  message_sensor.messages})

def w_display_add(request):
    mqttwind.send_request("data:0:0:0:0:0")
    mqttwind.client.on_message = w_on_messages
    time.sleep(0.5)
    return redirect('/windmill')

def w_changeStatus(request):
    # answer = request.GET['status']
    if request.method == 'POST':
       set_wind = request.POST.get('status_wind')
       who_wind = request.POST.get('target_wind')
       stand_wind = request.POST.get('facing_wind')
       mes = 'status:'+str(who_wind)+':'+str(set_wind)+':'+str(stand_wind)+':0:0'
       mqttwind.send_request(mes)
    return redirect('/windmill')


def s_display_message(request):
    mqttsolar.client.on_message = s_on_messages
    return render(request, 'index.html', {'subject':'solar','messages_device': message_solar.messages, 'messages_sensor':  message_sensor.messages})

def s_display_add(request):
    mqttsolar.send_request("data:0:0:0:0:0")
    mqttsolar.client.on_message = s_on_messages
    time.sleep(0.5)
    return redirect('/solar')

def s_changeStatus(request):
    # answer = request.GET['status']
    if request.method == 'POST':
       set_wind = request.POST.get('status_wind')
       who_wind = request.POST.get('target_wind')
       stand_wind = request.POST.get('facing_wind')
       mes = 'status:'+str(who_wind)+':'+str(set_wind)+':'+str(stand_wind)+':0:0'
       mqttsolar.send_request(mes)
    return redirect('/solar')