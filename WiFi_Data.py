import paho.mqtt.client as mqtt

broker_url = "broker.hivemq.com"
broker_port = 1883

def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code " (rc))

def on_disconnect(client, userdata, rc):
    print("Client Got Disconnected")

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.connect(broker_url, broker_port)
client.subscribe("ENTC/Wifi_Outgoing", qos=1)
client.loop_forever()