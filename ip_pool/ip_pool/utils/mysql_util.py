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
    def excute_sql(self, ip, website):
        sql = "INSERT INTO `ip_pool`(`ip`,`address`,`type`,`source`,`website`) values('{}', '{}', '{}', '{}','{}')"\
            .format(ip["ip"], ip["address"],ip["type"],ip["source"],website)
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
