import scrapy
from stock.items import StockItem
from stock.utils.mysql_util import Mysql_util
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class EastmoneySpider(scrapy.Spider):
    name = "eastmoney"
    allowed_domains = ["eastmoney.com"]
    start_urls = ["http://quote.eastmoney.com/center/gridlist.html#hs_a_board"]


    # 实例化⼀个浏览器对象
    def __init__(self):
        # 防止网站识别selenium
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument("--headless")
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('-ignore-certificate-errors')
        options.add_argument('-ignore -ssl-errors')
        self.bro = webdriver.Chrome(chrome_options=options)
        self.wait = WebDriverWait(self.bro, 10)
        super().__init__()


    def parse(self, response):
        path = "//*[@id='table_wrapper-table']/tbody/tr"
        mysql_util = Mysql_util()
        for item in response.xpath(path):
            td_list = item.xpath("./td")[1:-1]
            item = StockItem()
            item["code"] = td_list[0].xpath("./a/text()")[0].extract()
            item["name"] = td_list[1].xpath("./a/text()")[0].extract()
            item["link"] = td_list[1].xpath("./a/@href")[0].extract()
            item["forum"] = td_list[2].xpath("./a[1]/@href")[0].extract()
            item["money_stream"] = td_list[2].xpath("./a[2]/@href")[0].extract()
            item["data"] = td_list[2].xpath("./a[3]/@href")[0].extract()
            item["price"] = td_list[3].xpath("./span/text()")[0].extract()
            item["range"] = td_list[4].xpath("./span/text()")[0].extract()
            item["increment"] = td_list[5].xpath("./span/text()")[0].extract()
            item["turnover"] = td_list[6].xpath("./text()")[0].extract()
            item["turnvolume"] = td_list[7].xpath("./text()")[0].extract()
            item["amplitude"] = td_list[8].xpath("./text()")[0].extract()
            item["highest"] = td_list[9].xpath("./span/text()")[0].extract()
            item["lowest"] = td_list[10].xpath("./span/text()")[0].extract()
            item["begin"] = td_list[11].xpath("./span/text()")[0].extract()
            item["history"] = td_list[12].xpath("./text()")[0].extract()
            item["volume_rate"] = td_list[13].xpath("./text()")[0].extract()
            item["turnover_rate"] = td_list[14].xpath("./text()")[0].extract()
            item["pe_rate"] = td_list[15].xpath("./text()")[0].extract()
            item["market_rate"] = td_list[16].xpath("./text()")[0].extract()
            mysql_util.excute_sql(item)
        mysql_util.commit()
        mysql_util.close()

    def closed(self, spider):
        print("closed bro=====================")
        self.bro.quit()



