# subscriber.py
import runpy
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # subscribe, which need to put into on_connect
    # if reconnect after losing the connection with the broker, it will continue to subscribe to the raspberry/topic topic
    client.subscribe("raspberry/topic")

# the callback function, it will be triggered when receiving messages
def on_message(client, userdata, msg):
    #print("invoke")
    msg = (f"{msg.topic} {msg.payload}")
    print(msg)
    if (msg=="raspberry/topic b'arbaz'"):
        runpy.run_path(path_name='/home/pi/Desktop/new_bulb.py')
    elif (msg=="raspberry/topic b'arbaz1'"):
        runpy.run_path(path_name='/home/pi/Desktop/new_bulb1.py')
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# set the will message, when the Raspberry Pi is powered off, or the network is interrupted abnormally,
#it will send the will message to other clients
client.will_set('raspberry/status', '{"status": "Off"}')


# create connection, the three parameters are broker address, broker port number, and keep-alive time respectively
client.connect("broker.emqx.io", 1883, 60)

# set the network loop blocking, it will not actively end the program before calling disconnect() or the program crash
client.loop_forever()
#raspberry/topic b'arbaz'
