import scrapy
from ip_pool.ip_pool.utils.mysql_util import Mysql_util
from ip_pool.ip_pool.utils.test_ip import check_proxy
# from ip_pool.ip_pool.utils.mysql_util import Mysql_util
# from ip_pool.ip_pool.utils.test_ip import check_proxy


class XsdailiSpider(scrapy.Spider):
    name = "getip"
    allowed_domains = ["89ip.cn"]
    url = "https://www.89ip.cn/index_{}.html/"
    start_urls = []
    for i in range(1, 7):
        start_urls.append(url.format(i))
    website = 1
    mysql = Mysql_util()
    mysql.truncate_table(website=website)
    mysql.close()

#/html/body/meta"utf-8"/div[3]/div[1]/div/div[1]/table/tbody/tr[1]
    def parse(self, response):
        path = "/html/body//table[@class='layui-table']/tbody/tr"
        mysql = Mysql_util()
        for page in response.xpath(path):
            ip = page.xpath("./td[1]/text()")[0].extract().strip() + ":" + page.xpath("./td[2]/text()")[0].extract().strip()
            address = page.xpath("./td[2]/text()")[0].extract().strip()
            type = page.xpath("./td[3]/text()")[0].extract().strip()
            if check_proxy(ip):
                ip = {"ip":ip,"address":address,"type":type,"source":''}
                mysql.excute_sql(ip,website=self.website)
        mysql.commit()
        mysql.close()
