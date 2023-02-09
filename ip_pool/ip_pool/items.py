# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class IpPoolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ip = scrapy.Field()
    address = scrapy.Field()
    source = scrapy.Field()
    type = scrapy.Field()

    def get_ip(self, ip_str):
        ip_index = ip_str.index("@")
        self["ip"] = ip_str[0:ip_index]

        type_index = ip_str.index("#", ip_index + 1)
        self["type"] = ip_str[ip_index + 1:type_index]

        try:
            self["address"], self["source"] = ip_str[type_index+1::].split()
        except Exception as e:
            print("get source ERREOR:" + str(e))
            self["address"] = ip_str[type_index+1::].split()
            self["source"] = " "
