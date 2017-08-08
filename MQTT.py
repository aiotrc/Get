import paho.mqtt.client as mqtt  # import the client1


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)


broker_address = "127.0.0.1"
client = mqtt.Client("P1")  # create new instance

client.on_message = on_message  # attach function to callback

client.connect(broker_address, 5000)  # connect to broker
client.loop_start()  # start the loop

print("Subscribing to topic", "agent_id")
client.subscribe("agent_id")

print("Publishing message to topic", "agent_id")
client.publish("agent_id", "50")

client.loop_stop()  # stop the loop

if __name__ == "__main__":
    pass
