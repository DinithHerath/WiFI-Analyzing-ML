import paho.mqtt.client as mqtt
import ast

broker_url = "broker.hivemq.com"
broker_port = 1883


def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code"(rc))


def on_disconnect(client, userdata, rc):
    print("Client Got Disconnected")


def on_message(client, userdata, message):
    data_store(message.payload)


def data_store(data_recieved):
    data = ast.literal_eval(data_recieved.decode("utf-8"))
    print(data)


client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.connect(broker_url, broker_port)
client.subscribe("ENTC/Wifi_Outgoing", qos=1)
client.loop_forever()
