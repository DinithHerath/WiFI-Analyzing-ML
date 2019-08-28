import paho.mqtt.client as mqtt #mqtt client library
import ast #library for data validation

broker_url = "broker.hivemq.com" #broker URL
broker_port = 1883 #broker port


def on_connect(client, userdata, flags, rc): #on connect interrupt
    print("Connected With Result Code",(rc))


def on_disconnect(client, userdata, rc): #on disconnect interrupt
    print("Client Got Disconnected")


def on_message(client, userdata, message): #on message interrupt
    data_store(message.payload)


def data_store(data_recieved): #the procedure to do when data recieved
    data = ast.literal_eval(data_recieved.decode("utf-8"))
    print(data)


client = mqtt.Client() #defining client
#assigning interrupts for client variable
client.on_connect = on_connect 
client.on_disconnect = on_disconnect
client.connect(broker_url, broker_port) #connect using this port
client.subscribe("ENTC/Wifi_Outgoing", qos=1) #subscription topic - change this according to your preference
client.loop_forever() #loop which run forever and interrupts at any above interrupt incidences
