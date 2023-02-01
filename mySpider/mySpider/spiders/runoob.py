import json

import scrapy


class RunoobSpider(scrapy.Spider):
    name = 'runoob'
    allowed_domains = ['runoob.com']
    start_urls = ['https://www.runoob.com/']

    def parse(self, response):
        course_dict = {}
        for courses in response.xpath("/html/body/div[4]/div/div[2]/div[contains(@class,'codelist codelist-desktop')]"):
            name = courses.xpath("./h2/text()").extract()[0].strip()
            course_dict[name] = []
            for course in courses.xpath("./a"):
                course_dict[name].append(
                    [course.xpath("./h4/text()").extract()[0].strip(), course.xpath("./@href").extract()[0].strip()])

        course_json = json.dumps(course_dict, ensure_ascii=False)
        print(course_json)
        open("courses.json", 'w', encoding="utf-8").write(course_json)
