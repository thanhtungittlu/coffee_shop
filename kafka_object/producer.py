from time import time
from kafka import KafkaProducer
import json, time
from config import config



def json_serializer(data):
    return data

sever_name = config.SERVER_KAFKA + ":" + config.PORT_KAFKA

producer = KafkaProducer(
        bootstrap_servers = [sever_name], 
        value_serializer = json_serializer, 
    )

   
  
