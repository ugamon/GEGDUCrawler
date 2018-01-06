#encoding=utf-8
from copy import copy
from client import write_output_to_file
from client.utils import remove_all_symbols
from collections import *

SCENARIOS = [
    "//*/div/h3/a[@class='item-description-title-link']",
    "//div[@class='about']",
    "//div[@class='date c-2']"

]

class ContentFilters(object):
    def __repr__(self):
        return "class <<{clsname}>> is meant to be xpath scenarios dispatcher".format(clsname=ContentFilters.__name__)

    def __str__(self):
        return "class is used to get and change xpath scenarios"

    def __init__(self, filters):
        self.filters = deque()
        if filters:
            if isinstance(filters, list):
                for item in filters:
                    self.filters.append(item)
            else:
                raise ValueError("Filters parameter should be list() instance. Got {frmt} instead".format(frmt=type(filters)))

    def __add__(self, other):
        if other:
            if isinstance(other, str):
                return self.filters.append(other)
            else:
                raise ValueError("Other parameter should be str() instance, got {frmt} instead".format(frmt=type(other)))
        else:
            raise Exception

    def depth(self):
        return len(self.filters)

    def all(self):
        for scenario in self.filters:
            yield scenario

    def last(self, change=False):
        if change:
            return self.filters.pop()
        else:
            return self.filters[-1]

    def first(self, change=False):
        if change:
            return self.filters.popleft()
        else:
            return self.filters[0]


class ParseThePage(object):
    DEFAULT_PROPERTY = {
        "all_handler": True

    }

    def __init__(self, options=None, content=None, bucket=None, contentFilters=None):

        self._options = copy(ParseThePage.DEFAULT_PROPERTY)

        if not options:
            options = {}

        self._options.update(options)

        if content:
            self.data = content
        else:
            raise Exception("Content parameter must be not NULL. Expected html page template.")

        if contentFilters is None:
            self._filters = ContentFilters(SCENARIOS)
        else:
            if isinstance(contentFilters, ContentFilters):
                self._filters = contentFilters
            else:
                raise ValueError("Expected ContentFilter() instance. Got {0} instead".format(type(contentFilters)))

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

    def list_union_ref(self, _list):
        _number_of_columns = len(_list)
        while len(_list[0])>0:
            for i in range(0,_number_of_columns):
                value = remove_all_symbols(_list[i].pop().text






    def parse(self):
        from lxml import html
        tree = html.fromstring(self.data)

        bucket = []
        for xpath in self._filters.all():
            bucket.append(tree.xpath(xpath))
        # _titles_list = tree.xpath("//*/div/h3/a[@class='item-description-title-link']")
        # _prices_list = tree.xpath("//div[@class='about']")
        # _date_list = tree.xpath("//div[@class='date c-2']")
        # self.list_union(_titles_elements=_titles_list,_prices_elements=_prices_list,_date_elements=_date_list)

    def get_storage(self):
        return self.__bucket

