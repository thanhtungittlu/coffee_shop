from time import time
from kafka import KafkaProducer
import json, time
from config import config
from loguru import logger


def json_serializer(data):
    return data

sever_name = config.SERVER_KAFKA + ":" + config.PORT_KAFKA
# print("sever_name", sever_name)
logger.info(sever_name)
producer = KafkaProducer(
        bootstrap_servers = [sever_name], 
        value_serializer = json_serializer, 
    )

   
  
