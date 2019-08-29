import paho.mqtt.client as mqtt  # mqtt client library
import pandas as pd  # data processing library
import ast  # library for data validation
import os
import csv  # library for handling csv files

broker_url = "broker.hivemq.com"  # broker URL
broker_port = 1883  # broker port


def on_connect(client, userdata, flags, rc):  # on connect interrupt
    print("Connected With Result Code", (rc))


def on_disconnect(client, userdata, rc):  # on disconnect interrupt
    print("Client Got Disconnected")


def on_message(client, userdata, message):  # on message interrupt
    data_store(message.payload)


def data_store(data_recieved):  # the procedure to do when data recieved
    filename = "wifi_data.csv"
    fixed_wifi = {"UoM_Wireless1": -100, "UoM_Wireless6": -100, "UoM_Wireless11": -100, "eduroam1": -100,
                  "eduroam6": -100, "eduroam11": -100, "Jungle Book10": -100,
                  "PROLINK_H5004NK_8766E11": -100, "UNIC-wifi11": -100}
    # this should be changed according to position of the NodeMCU
    try:
        data = ast.literal_eval(data_recieved.decode("utf-8"))
        print(data)
        for key, value in data.items():
            if key in fixed_wifi and fixed_wifi[key] == 100:
                fixed_wifi[key] = int(value)
        fixed_wifi["id"] = int(data["id"])
        # formatting data to a data frame and taking transpose
        data_format = pd.Series(data).to_frame().T
        print(data_format)
        data_format.to_csv(filename, index=False, mode='a',
                           header=(not os.path.exists(filename)))
    except Exception as exc:  # exception handling
        print(exc)


def create_csv():
    filename = "wifi_data.csv"
    fixed_wifi = {"id": 1, "UoM_Wireless1": -100, "UoM_Wireless6": -100, "UoM_Wireless11": -100,
                  "eduroam1": -100, "eduroam6": -100, "eduroam11": -100, "Jungle Book10": -100,
                  "PROLINK_H5004NK_8766E11": -100, "UNIC-wifi11": -100}
    # this should be changed according to position of the NodeMCU
    # creating header of the output file.
    with open(filename, 'r') as csvfileread:
        has_header = csv.Sniffer().has_header(csvfileread.read(256)) #checking for the header using sniffer
        csvfileread.seek(0)    
    if has_header != True:
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = fixed_wifi.keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        print("File created.")
    else:
        print("File already there with header.")


client = mqtt.Client()  # defining client
create_csv()  # creating csv file header
# assigning interrupts for client variable
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.connect(broker_url, broker_port)  # connect using this port
# subscription topic - change this according to your preference
client.subscribe("ENTC/Wifi_Outgoing", qos=1)
# loop which run forever and interrupts at any above interrupt incidences
client.loop_forever()
