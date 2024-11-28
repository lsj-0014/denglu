import scrapy
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from estate.items import EstateItem


class LiveInPeaceSpider(scrapy.Spider):
    name = "peace"
    allowed_domains = ["fang.com"]
    estate_url = "https://zu.fang.com/house/"
    # 数据链接，假设我们要爬取20页，动态生成URL
    start_urls = ([f"https://zu.fang.com/house/i3{i}/" for i in range(1, 50)])
    def parse(self, response):
        # 使用 Selenium 启动 Chrome 浏览器，加载页面直到需要的数据元素出现
        chrome = Chrome()
        chrome.get(response.url)
        WebDriverWait(chrome, 60).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "title")))
        # 获取页面的源代码
        html = chrome.page_source
        chrome.quit()
        # 用 selenium 提供的页面代码替换掉 scrapy 中的 response body
        response = response.replace(body=html)
        # 根据页面结构，提取房产数据
        listings = response.xpath('//*[@id="listBox"]/div[4]/dl') # 根据页面的div结构提取每个房源信息
        for listing in listings:
            item = EstateItem()
            # 标题
            item['job_title'] = listing.xpath('./dd/p[1]/a/text()').get()
            # 租房方式
            item['job_way'] = listing.xpath('./dd/p[2]/text()[1]').get()
            # 户型
            item['job_house'] = listing.xpath('./dd/p[2]/text()[2]').get()
            # 面积
            item['job_area'] = listing.xpath('./dd/p[2]/text()[3]').get()
            # 朝向
            item['job_orientation'] = listing.xpath('./dd/p[2]/text()[4]').get()
            # # 地址
            item['job_address'] = listing.xpath('//*[@id="rentid_D09_1_06"]/a[1]/span/text()').get()
            item['job_address'] += listing.xpath('//*[@id="rentid_D09_1_06"]/a[2]/span/text()').get()
            item['job_address'] += listing.xpath('//*[@id="rentid_D09_1_06"]/a[3]/span/text()').get()
            # 价格
            item['job_price'] = listing.xpath('./dd/div[2]/p/span/text()').get()
            # 返回爬取的数据
            yield item
