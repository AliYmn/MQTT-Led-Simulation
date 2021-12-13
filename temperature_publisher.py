import paho.mqtt.client as mqtt # paho lib.
import time
import random
# connections.
client = mqtt.Client()
client.connect("localhost",1883,60)
while True:
    print("Temperature working. It will send temperature periodically.")
    client.publish("sensors/temperature", str(random.randint(1, 100)));
    time.sleep(3)
# disconnect
client.disconnect();