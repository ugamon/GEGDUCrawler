#encoding=utf-8
from copy import copy
from client import writeOutputToFile
from client.utils import remove_all_symbols

class ParseThePage(object):
    DEFAULT_PROPERTY = {
        "all_handler": True

    }

    def __init__(self, options=None, content=None, bucket=None):
        self._options = copy(ParseThePage.DEFAULT_PROPERTY)

        if not options:
            options = {}

        self._options.update(options)

        if content:
            self.data = content
        else:
            raise Exception("content shouldn't be just null")
        if bucket is None:
            self.__bucket = []
        else:
            self.__bucket = bucket

        self.parse()

    def list_union(self,_titles_elements=None,_prices_elements=None,_date_elements=None):
        if len(_prices_elements) > 0:
            _active_price = _prices_elements.pop()
            _active_title = _titles_elements.pop()
            _active_date = _date_elements.pop()
            self.__bucket.append({"title": remove_all_symbols(_active_title.text.encode('windows-1251')),
                                  "price": remove_all_symbols(_active_price.text.encode('windows-1251')),
                                  "date": remove_all_symbols(_active_date.text.encode('windows-1251'))})
            self.list_union(_titles_elements,_prices_elements,_date_elements)

    def parse(self):
        from lxml import html
        tree = html.fromstring(self.data)
        _titles_list = tree.xpath("//*/div/h3/a[@class='item-description-title-link']")
        _prices_list = tree.xpath("//div[@class='about']")
        _date_list = tree.xpath("//div[@class='date c-2']")
        self.list_union(_titles_elements=_titles_list,_prices_elements=_prices_list,_date_elements=_date_list)

    def get_storage(self):
        return self.__bucket