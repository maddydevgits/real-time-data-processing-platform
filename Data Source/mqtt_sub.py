import paho.mqtt.client as mqtt

broker = "172.31.80.40"
port = 1883

client = mqtt.Client()
client.connect(broker,port)
print('Broker Connected')

client.subscribe('sacet/a11')

def notification(client,userdata,msg):
    print(msg.payload)

client.on_message = notification
client.loop_forever()
