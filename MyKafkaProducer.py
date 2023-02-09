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
    producer.send_message("perception-decision", "perception-decision-371745272", {"extend":{"type":'3'},"query":"播放王心凌的爱你","sceneId":"A84","sn":"20230221175337102000365742","deviceId":"C86314209687","userId":"60750606","actualCreateTime":"2023-02-21 17:53:38"})
    time.sleep(2)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
