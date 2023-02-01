import time

from kafka import KafkaProducer
import json


class MyKafkaProducer(object):
    def __init__(self, KafkaServerList=None, api_version=(2, 0, 2)):
        """
        :param KafkaServerList: kafka hosts(list)
        :param GroupID: groupId(str)
        :param api_version: kafka版本(tuple), 例: 2.0.2为 api_version=(2, 0, 2)
        """
        if KafkaServerList is None:
            KafkaServerList = []
        self._kwargs = {
            "bootstrap_servers": KafkaServerList,
            "api_version": api_version,
            "key_serializer": lambda k: json.dumps(k).encode(),
            "value_serializer": lambda v: json.dumps(v).encode(),
        }

        try:
            self._producer = KafkaProducer(**self._kwargs)
        except Exception as err:
            print("Producer init failed, %s" % err)

    def send_message(self, topic, key, message):
        self._producer.send(topic=topic, key=key, value=message)


def main():
    producer = MyKafkaProducer(KafkaServerList=['alikafka-pre-cn-tl32ravm3007-1-vpc.alikafka.aliyuncs.com:9092',
                                                'alikafka-pre-cn-tl32ravm3007-2-vpc.alikafka.aliyuncs.com:9092',
                                                'alikafka-pre-cn-tl32ravm3007-3-vpc.alikafka.aliyuncs.com:9092'])
    data = {'msg': '你好 kafka!'}
    producer.send_message("log-data-check", "2log-data-check-", "{'msg':'add','code':1,'data':{'domainCode':'panelVoiceFusion','nlpModel':'ref328'}}")
    time.sleep(2)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
