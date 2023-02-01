#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import sys
from kafka import KafkaConsumer


class MyKafkaConsumer(object):

    def __init__(self, KafkaServerList=None, GroupID='ai-terminal', ClientId="consumer-1", Topics=None,
                 api_version=(2, 0, 2)):
        """
        :param KafkaServerList: kafka hosts(list)
        :param GroupID: groupId(str)
        :param ClientId: clientId(str)
        :param Topics: topics,(list)
        :param api_version: kafka版本(tuple), 例: 2.0.2为 api_version=(2, 0, 2)
        """
        if KafkaServerList is None:
            KafkaServerList = []
        if Topics is None:
            Topics = []
        self._kwargs = {
            "bootstrap_servers": KafkaServerList,
            "client_id": ClientId,
            "group_id": GroupID,
            "enable_auto_commit": False,
            "auto_offset_reset": "earliest",
            "api_version": api_version,
            "key_deserializer": lambda m: None if (m is None) else str(m, "utf-8"),
            "value_deserializer": lambda m: json.loads(str(m, "utf-8")),
        }

        try:
            self._consumer = KafkaConsumer(**self._kwargs)
            self._consumer.subscribe(topics=Topics)
        except Exception as err:
            print("Consumer init failed, %s" % err)

    def consume_msg(self, macs=None):
        """ 手动拉取消息 """
        if macs is None:
            macs = []
        try:
            while True:
                data = self._consumer.poll(max_records=100)  # 拉取消息，字典类型
                if data:
                    for key in data:
                        consumerrecords = data.get(key)  # 返回的是ConsumerRecord对象，可以通过字典的形式获取内容。
                        for consumerrecord in consumerrecords:
                            # 临时过滤中间日志
                            if consumerrecord.value.get("response").get("retCode") == "10000":
                                continue

                            mac = consumerrecord.value.get('reqHeader').get('deviceid')
                            if mac is None:
                                reqBody = consumerrecord.value.get('reqBody')
                                if reqBody is not None:
                                    mac = reqBody.get('deviceid')

                            # 判断是不是需要的mac
                            if mac not in macs:
                                continue
                            elif consumerrecord is not None:
                                # 消息消费逻辑
                                message = {
                                    "Topic": consumerrecord.topic,
                                    "Partition": consumerrecord.partition,
                                    "Offset": consumerrecord.offset,
                                    "Key": consumerrecord.key,
                                    "Value": consumerrecord.value
                                }
                                self.process_msg(message)
                                # 消费逻辑执行完毕后在提交偏移量
                            else:
                                print("%s consumerrecord is None." % str(key))
                    self._consumer.commit()

        except Exception as err:
            print(err)

    # 解析消息的方法
    @staticmethod
    def process_msg(message):
        print(message["Value"])


def main():
    try:
        print("创建kafkaConsumer")
        consumer = MyKafkaConsumer(KafkaServerList=['alikafka-pre-cn-tl32ravm3007-1-vpc.alikafka.aliyuncs.com:9092',
                                                    'alikafka-pre-cn-tl32ravm3007-2-vpc.alikafka.aliyuncs.com:9092',
                                                    'alikafka-pre-cn-tl32ravm3007-3-vpc.alikafka.aliyuncs.com:9092'],
                                   Topics=['log-data-check'],
                                   GroupID='ai-terminal',
                                   ClientId="consumer-1",
                                   api_version=(2, 0, 2))
        macs = ["04FA83E453DA", "2C37C540A667", "04E2292209EC", "04E2292209F0"]
        consumer.consume_msg(macs)
    except Exception as err:
        print(err)


if __name__ == "__main__":
    try:
        main()
    finally:
        sys.exit()
