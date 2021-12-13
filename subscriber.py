"""
Four Sensors;
1th sensors : Turn on the led.
2th sensors : Turn off the led.
3th sensors : give information about led status such on or off
4th sensors : flip-flop led animation
"""

import paho.mqtt.client as mqtt

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe([("sensors/ledon",0),("sensors/ledoff",0),("sensors/ledstatus",0),("sensors/ledflipflop",0)]) # system subscribe this channel

def on_message(client, userdata, msg):
  print("msg.topic : ",msg.topic)
  # led on actions
  if (msg.payload.decode() == "Led ON" and msg.topic == "sensors/ledon"):
    print("Led On!")
  # led on actions
  elif (msg.payload.decode() == "Led OFF" and msg.topic == "sensors/ledoff"):
    print("Led Off!")
  # led on actions
  elif (msg.payload.decode() == "Led Status" and msg.topic == "sensors/ledstatus"):
    print("Led Status : Led ON")
  elif (msg.payload.decode() == "Start" and msg.topic == "sensors/ledflipflop"):
      print("Led Flip Flop")
  else:
      print("Command not found! -> ",msg.payload.decode())
  # client.disconnect()
    
client = mqtt.Client()
client.connect("localhost",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()