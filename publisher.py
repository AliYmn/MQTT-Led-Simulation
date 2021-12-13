"""
Two Publisher;
1-) manage 1th sensor and 2th sensors : led on and led off
2-) manage 3th sensor: get led status 
3-) manage 4th sensor : temperature periodically
"""

import paho.mqtt.client as mqtt # paho lib.

# connections.
client = mqtt.Client()
client.connect("localhost",1883,60)

loop = True
commands = ""
while loop:
    commands = input("Write Commands or (/help to show all commands.) : ")
    if commands == "/help":
        print(
        """ 
        /quit : Close the program.
        /ledon : Led ON.
        /ledoff : Led Off
        /status : it returns information about led status such as on or off
        """)
    elif commands == "/ledon":
        client.publish("sensors/ledon", "Led ON");
    elif commands == "/ledoff":
        client.publish("sensors/ledoff", "Led OFF");
    elif commands == "/status":
        client.publish("sensors/ledstatus", "Led Status");
    elif commands == "/quit":
        client.disconnect();
        break
    else:
        print("{} this command not found.".format(commands))

# disconnect
client.disconnect();