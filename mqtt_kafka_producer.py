import paho.mqtt.client as mqtt
from pykafka import KafkaClient
from random import uniform
import time

mqtt_broker = "mqtt.eclipse.org"
mqtt_client = mqtt.Client("distanceToCyclist")
mqtt_client.connect(mqtt_broker)

kafka_client = KafkaClient(hosts="localhost:9092")
kafka_topic = kafka_client.topics['distanceToCyclist']
kafka_producer = kafka_topic.get_sync_producer()


while True:
    randNumber = uniform(20.0, 21.0)
    mqtt_client.publish("distanceToCylclist", randNumber)
    print("MQTT: just published " + str(randNumber) + " to topic distanceToCyclist")

    kafka_producer.produce(str(randNumber).encode('ascii'))
    print("KAFKA: just published " + str(randNumber) + " to topic distanceToCyclist")

    time.sleep(3)