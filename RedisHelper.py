import redis


class RedisHelper:
    def __init__(self):
        self.connection_pool = redis.ConnectionPool(host="ys-ai-dev-haier-new.redis.rds.aliyuncs.com", port=6379,
                                                    password="P!y^NR9H3irGsIO!")
        self.__conn = redis.Redis(connection_pool=self.connection_pool)  # 连接redis

    def publish(self, pub, msg):
        self.__conn.publish(pub, msg)  # 根据提供的频道进行消息发布
        return True

    def subscribe(self, sub):
        pub = self.__conn.pubsub()  # 打开收音机
        pub.subscribe(sub)  # 调频道
        pub.parse_response()  # 准备接收
        return pub


# 解析消息
def process_msg(message):
    print(message)


def subscribe():
    red = RedisHelper()  # 得到实例化对象
    while 1:
        data = red.subscribe("log-data-check-116090964").parse_response()  # 此时会处于一直订阅的状态有数据就会接收过来
        if data:
            process_msg(str(data[2], encoding="utf-8"))


if __name__ == "__main__":
    try:
        subscribe()
    except Exception as e:
        print(e)
