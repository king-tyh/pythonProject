import random

import pymysql

class Mysql_util():
    def __init__(self):
        self.db = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database='stock')

        self.cursor = self.db.cursor()
#{"ip":ip,"address":address,"type":type,"source":''}
    def excute_sql(self, item):
        sql = "INSERT INTO `stock`(`code`,`name`,`link`,`forum`,`money_stream`,`data`,`price`,`range`,`increment`," \
              "`turnover`,`turnvolume`,`amplitude`,`highest`,`lowest`,`begin`,`history`,`volume_rate`,`turnover_rate`," \
              "`pe_rate`,`market_rate`) values('{}', '{}', '{}', '{}','{}','{}', '{}', '{}', '{}','{}','{}', " \
              "'{}', '{}', '{}','{}','{}', '{}', '{}', '{}','{}')"\
            .format(item["code"] , item["name"] , item["link"] , item["forum"] , item["money_stream"] , item["data"] ,
                    item["price"] , item["range"] , item["increment"] , item["turnover"] , item["turnvolume"] ,
                    item["amplitude"] , item["highest"] , item["lowest"] , item["begin"] , item["history"] , item["volume_rate"] ,
                    item["turnover_rate"] , item["pe_rate"] , item["market_rate"])
        self.cursor.execute(sql)

    def truncate_table(self, website):
        self.cursor.execute("DELETE FROM `ip_pool` WHERE `website`={}".format(website))
        self.commit()
        print("##############################\n清空历史表成功!!!!!\n##############################")

    def get_ip(self):
        self.cursor.execute("SELECT `ip` FROM `ip_pool`")
        return self.cursor.fetchall()


    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()

    def close(self):
        self.cursor.close()
        self.db.close()
