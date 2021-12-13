"""
Two Publisher;
1-) manage 1th sensor and 2th sensors : led on and led off
2-) manage 3th sensor and 4th sensors : get led status and flip-flop animation
"""

import paho.mqtt.client as mqtt # paho lib.

# connections.
client = mqtt.Client()
client.connect("localhost",1883,60)

# publishers
client.publish("sensors/ledon", "Led ON");
client.publish("sensors/ledoff", "Led OFF");
client.publish("sensors/ledstatus", "Led Status");
client.publish("sensors/ledflipflop", "Start");

# disconnect
client.disconnect();