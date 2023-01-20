import paho.mqtt.client as mqtt
import time
import random

broker = "172.31.80.40"
port = 1883

client = mqtt.Client()

while True:
    try:
     client.connect(broker,port)
     print('Broker connected')
     msg = '{"Humidity":'+str(random.randint(20,100))+',"Temperature":'+str(random.randint(20,40))+'}'
     client.publish('sacet/a11',msg)
     time.sleep(4)

    except:
     print('Broker Connection Failure')
