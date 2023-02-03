import json

import scrapy


class XsdailiSpider(scrapy.Spider):

    name = 'xsdaili'
    allowed_domains = ['xsdaili.cn']
    start_urls = ['https://www.xsdaili.cn/']

    def parse(self, response):
        url_dict = {}
        for url in response.xpath("/html/body/div[5]/div/div[2]/div/div/div/div[2]/div/div[2]")[0:2]:
            name = courses.xpath("./h2/text()").extract()[0].strip()
            course_dict[name] = []
            for course in courses.xpath("./a"):
                course_dict[name].append(
                    [course.xpath("./h4/text()").extract()[0].strip(), course.xpath("./@href").extract()[0].strip()])

        course_json = json.dumps(course_dict, ensure_ascii=False)
        print(course_json)
        open("courses.json", 'w', encoding="utf-8").write(course_json)
