# encoding=utf-8

class ItemModelBase(object):
    def __init__(self,
                 _id=None,
                 # title= None,
                 short_description=None,
                 full_description=None,
                 date=None,
                 price=None,
                 ):

        self.id = None
        # self.title = None
        self.sdesc = None
        self.price = None
        self.date = None
        self.fdesc = None

        if id:
            self.id = _id

        # if title:
        #     self.title = self.__price_parse(self.__encode(title))

        if short_description:
            self.sdesc = self.__encode(short_description)

        if price:
            self.__price_parse(self.__encode(price), 'руб')

        if date:
            self.date = self.__encode(date)

        if full_description:
            self.fdesc = self.__encode(full_description)

    def __repr__(self):
        return "Base class for AVITO catalog item"

    def __str__(self):
        return "Base class for AVITO catalog item"

    def __encode(self, value, cust_encoding="cp1251"):
        def internal_encoding(_value):
            _value = value
            try:
                return _value.encode(cust_encoding)
            except Exception as e:
                return _value

        if isinstance(value, dict):
            return {internal_encoding(k): internal_encoding(v) for k, v in value.items()}
        elif isinstance(value, list):
            return [internal_encoding(k) for k, v in value]
        else:
            return internal_encoding(value)

    def __price_parse(self, value, delimeter):
        if delimeter in value:
            self.price = value.split(delimeter)[0].strip()
            # else:
            #     self.price = value
