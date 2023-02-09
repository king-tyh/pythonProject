import scrapy
from ip_pool.items import IpPoolItem
from ip_pool.utils.mysql_util import Mysql_util
from ip_pool.utils.test_ip import check_proxy



class XsdailiSpider(scrapy.Spider):
    name = "xsdaili"
    allowed_domains = ["xsdaili.cn"]
    start_urls = ["https://www.xsdaili.cn/"]
    website=0
    def parse(self, response):
        path = "/html/body/div[5]/div/div[2]/div/div/div/div[2]/div/div[2]/div"
        mysql_util = Mysql_util()
        mysql_util.truncate_table(website=self.website)
        flag = False
        for page in response.xpath(path)[0:2]:
            a = page.xpath("./div[@class='title']/a")[0]
            title = a.xpath("./text()")[0].extract()
            href = a.xpath("./@href")[0].extract()
            print("正在获取" + title + " https://www.xsdaili.cn" + href)
            yield scrapy.Request("https://www.xsdaili.cn" + href, meta={'mysql_util': mysql_util, 'flag': flag}, callback=self.parse_page)
            flag = True

    def parse_page(self, response):
        ip_list = []
        mysql_util = response.meta['mysql_util']
        a = response.xpath("/html/body/div[5]/div/div[2]/div/div/div/div[2]/div/div[2]/div[2]/text()").extract()
        try:
            for ip in a[0:-2]:
                item = IpPoolItem()
                item.get_ip(ip.strip())
                if check_proxy(item["ip"]):
                    mysql_util.excute_sql(item,website=self.website)
        except Exception as e:
            mysql_util.rollback()
            print("excute_sql ERROR: " + str(e))
        else:
            mysql_util.commit()
        finally:
            if response.meta['flag']:
                mysql_util.close()





