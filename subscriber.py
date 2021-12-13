"""
Four Sensors;
1th sensors : Turn on the led.
2th sensors : Turn off the led.
3th sensors : give information about led status such on or off
4th sensors : flip-flop led animation
"""
import paho.mqtt.client as mqtt # lib
import time

# This is the Subscribers
def on_connect(client, userdata, flags, rc):
  print("Subscriber server started successfully.")
  client.subscribe([("sensors/ledon",0),("sensors/ledoff",0),("sensors/ledstatus",0),("sensors/ledflipflop",0)]) # system subscribe this channel

led_status = False
# check and return
def on_message(client, userdata, msg):
  global led_status
  # led on actions
  if (msg.payload.decode() == "Led ON" and msg.topic == "sensors/ledon"):
    led_status = True
    print("Led now On.")
  # led on actions
  elif (msg.payload.decode() == "Led OFF" and msg.topic == "sensors/ledoff"):
    print("Led now Off.")
  # led on actions
  elif (msg.payload.decode() == "Led Status" and msg.topic == "sensors/ledstatus"):
    if not led_status:
          led_status = False
    if led_status:
      print("Led Status : Led ON")
    else:
      print("Led Status : Led Off")
  elif (msg.payload.decode() == "Start" and msg.topic == "sensors/ledflipflop"):
    print("Flip-Flop started.")
    for amount in range(5):
      if led_status:
        led_status = not led_status
        print("Led On")
      else:
        led_status = not led_status
        print("Led Off")
      time.sleep(1)
    print("flip-flop finished.")
  else:
      print("Command not found! -> ",msg.payload.decode())
  # client.disconnect()
    
client = mqtt.Client()
client.connect("localhost",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()