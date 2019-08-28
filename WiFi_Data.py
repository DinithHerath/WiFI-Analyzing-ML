import paho.mqtt.client as mqtt  # mqtt client library
import pandas as pd
import ast  # library for data validation

broker_url = "broker.hivemq.com"  # broker URL
broker_port = 1883  # broker port


def on_connect(client, userdata, flags, rc):  # on connect interrupt
    print("Connected With Result Code", (rc))


def on_disconnect(client, userdata, rc):  # on disconnect interrupt
    print("Client Got Disconnected")


def on_message(client, userdata, message):  # on message interrupt
    data_store(message.payload)


def data_store(data_recieved):  # the procedure to do when data recieved
    data = ast.literal_eval(data_recieved.decode("utf-8"))
    print(data)
    filename = "wifi_data.csv"
    try:
        data_format = pd.Series(data).to_frame().T #formatting data to a data frame and taking transpose
        print(data_format)
    except Exception as exc: #exception handling
        print(exc)


client = mqtt.Client()  # defining client
# assigning interrupts for client variable
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.connect(broker_url, broker_port)  # connect using this port
# subscription topic - change this according to your preference
client.subscribe("ENTC/Wifi_Outgoing", qos=1)
# loop which run forever and interrupts at any above interrupt incidences
client.loop_forever()
