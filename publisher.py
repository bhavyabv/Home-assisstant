import json
import time
import paho.mqtt.client as mqtt

BROKER_HOST = "localhost"        # mosquitto in Docker
BROKER_PORT = 1883
TOPIC = "home/bhavyabv-2025/sensor"

student_name = "Bhavya B V"      # <-- use = and quotes
unique_id = "42130082"

client = mqtt.Client()
client.connect(BROKER_HOST, BROKER_PORT, 60)

while True:
    payload = {
        "student_name": "Bhavya B V",
        "unique_id": "42130082",
        "temperature": 25,
        "humidity": 60,
        "light": 1
    }
    client.publish(TOPIC, json.dumps(payload))
    print("Published:", payload)
    time.sleep(5)
