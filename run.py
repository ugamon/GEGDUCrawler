# encoding=utf-8
from client import GetRawData, ParseThePage
from config import Descriptor
from os import path
import os
from selen import base

xpaths = {

    "start": r"//h3/a[@class='item-description-title-link']",
    "next": r"//div/a[contains(.,'Следующее →')]",

    # "title": {"xpath": "//h1/span[@class='title-info-title-text']", "value": "innerText"},
    "title": {"xpath": "//div[@class='item-view']", "value": "outerText"},
    "date": {"xpath": "//div[@class='title-info-metadata-item']", "value": "innerText"},
    "price": {"xpath": "//span[@class='price-value-string js-price-value-string']", "value": "innerText"},

}


def safeStr(obj):
    try:
        return str(obj)
    except UnicodeEncodeError:
        return obj.encode('ascii', 'ignore').decode('ascii')


if __name__ == '__main__':

    # for url in Descriptor(max_depth=5).get_url():
    #     resp = GetRawData(url=url,
    #                       interval=10,
    #
    #                       headers={
    #                           "Content-Type": "text/html;charset=utf-8",
    #                           "user-agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
    #                       })
    #     with open("log.txt", 'a+') as f:
    #         f.write(resp.content.encode() + "\n"+">>>>>>>>>>>>>>" )
    #
    #     inst = ParseThePage(resp.content).output(r'samples\datafile.csv')

    inst = base.SeleniumBase()
    inst.start(r"https://www.avito.ru/moskva/noutbuki?user=1")
    el = inst.get_element_presented(xpaths['start'])
    el.click()
    for i in range(0, 2000):
        title = inst.get_element_presented(xpaths['title']['xpath'])
        # date = inst.get_element_presented(xpaths['date']['xpath'])
        # price = inst.get_element_presented(xpaths['price']['xpath'])
        # maker = inst.get_element_presented(r"//div[@class='item-params']/span")
        # metro = inst.get_element_presented(r"//span[@class='item-map-address']/span")
        # full_desc = inst.get_element_presented(r"//div[@class='item-description-text']/p")

        title_value = inst.get_webelement_attribute(title, xpaths['title']['value'])
        # date_value = inst.get_webelement_attribute(date, xpaths['date']['value'])
        # price_value = inst.get_webelement_attribute(price, xpaths['price']['value'])
        # maker_value = inst.get_webelement_attribute(maker, 'innerText')
        # metro_value = inst.get_webelement_attribute(metro, 'innerText')
        # full_desc_value = inst.get_webelement_attribute(full_desc, 'innerText')
        with open('sample.txt', 'a+') as f:
            f.write(title_value.encode('utf-8') + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

        next = inst.get_element_presented(xpaths['next'])
        next.click()
