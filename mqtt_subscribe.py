import paho.mqtt.client as mqtt
import time

mqtt_broker = "mqtt.eclipse.org"
mqtt_client = mqtt.Client("temperatureInside")
mqtt_client.connect(mqtt_broker)

def on_message(client, userdata, message):
    msg_payload = str(message.payload.decode("utf-8"))
    print("MQTT: just received " + msg_payload + " from topic " + message.topic)

mqtt.client.loop_start()
mqtt_client.subscribe("temperature3")
mqtt_client.on_message = on_message
time.sleep(30)
mqtt_client.loop_stop()