import os, json, time
from datetime import datetime
import paho.mqtt.client as mqtt

print('test')

HIVEMQ_HOST = os.getenv('HIVEMQ_HOST', 'localhost')
HIVEMQ_PORT = int(os.getenv('HIVEMQ_PORT', 1883))

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    received_time = time.time()
    payload = json.loads(msg.payload.decode())
    sent_time = payload["timestamp"]
    sequence_number = payload["sequence_number"]
    delay =  received_time - sent_time
    readable_time = datetime.fromtimestamp(received_time).strftime("%H:%M:%S:%f")[:-3]

    print(f"[{readable_time}] Sequence: {sequence_number}, Delay: {delay * 1000:.3f}ms")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(HIVEMQ_HOST, HIVEMQ_PORT, 60)
client.loop_forever()
