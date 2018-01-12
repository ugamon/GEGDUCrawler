# encoding=utf-8
from selen.base import SeleniumBase

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


if __name__ == "__main__":
    inst = SeleniumBase()
    inst.start(r"https://www.avito.ru/moskva/noutbuki?user=1")
    el = inst.get_element_presented(xpaths['start'])
    el.click()
    for i in range(0, 100):
        title = inst.get_element_presented(xpaths['title']['xpath'])
        # date = inst.get_element_presented(xpaths['date']['xpath'])
        # price = inst.get_element_presented(xpaths['price']['xpath'])
        # maker = inst.get_element_presented(r"//div[@class='item-params']/span")
        # metro = inst.get_element_presented(r"//span[@class='item-map-address']/span")
        # full_desc = inst.get_element_presented(r"//div[@class='item-description-text']/p")

        title_value = safeStr(inst.get_webelement_attribute(title, xpaths['title']['value']))
        # date_value = inst.get_webelement_attribute(date, xpaths['date']['value'])
        # price_value = inst.get_webelement_attribute(price, xpaths['price']['value'])
        # maker_value = inst.get_webelement_attribute(maker, 'innerText')
        # metro_value = inst.get_webelement_attribute(metro, 'innerText')
        # full_desc_value = inst.get_webelement_attribute(full_desc, 'innerText')
        print(title_value)
        next = inst.get_element_presented(xpaths['next'])
        next.click()
