import paho.mqtt.client as mqtt

broker_url = "broker.hivemq.com"
broker_port = 1883

client = mqtt.Client()
client.connect(broker_url, broker_port)
client.subscribe("ENTC/Wifi_Outgoing", qos=1)
client.loop_forever()