import time, json, os
import paho.mqtt.client as mqtt
from datetime import datetime

# Environment variables
BROKER = os.getenv("BROKER", "10.0.0.241")
PORT = int(os.getenv("PORT", 1883))
TOPIC = os.getenv("TOPIC", "test/topic")
DELAY = float(os.getenv("DELAY", 10))  # Default delay is 10 seconds

client = mqtt.Client()
client.connect(BROKER, PORT)

sequence_number = 0

while True:
    # Get the Unix timestamp (in seconds since epoch)
    timestamp = time.time()

    # Create a human-readable timestamp with hours, minutes, seconds, and milliseconds
    human_readable_timestamp = datetime.now().strftime('%H:%M:%S.') + f"{int((timestamp % 1) * 1000):03}"

    # Create the message including both timestamps
    message = {
        "sequence_number": sequence_number,
        "timestamp": timestamp
    }

    # Publish the message
    client.publish(TOPIC, json.dumps(message))

    # Print the message sent
    print(f"[{human_readable_timestamp}] Sent: {message}")

    # Increment the sequence number
    sequence_number += 1

    # Wait for the delay before sending the next message
    time.sleep(DELAY)
