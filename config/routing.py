import copy
from random import randint
class Descriptor(object):
    DEFAULT_OPTIONS = {
        "site": r"https://www.avito.ru",
        "router": [
            r"moskva/noutbuki",
        ]
    }

    def __init__(self, options=None, max_depth=1):
        self._options = copy.copy(Descriptor.DEFAULT_OPTIONS)

        if options is None:
            options = {}
        elif not isinstance(options,dict):
            print("{message}")
            options = {}
        else:
            self._options.update(options)

        if max_depth>1:
            _bs = self._options["router"][0]
            self._options["router"] = ["{uri}?q={page_num}".format(page_num=page_num, uri=_bs) for page_num in range(1, max_depth)]

    def get_url(self):
        try:

            if isinstance(self._options["router"],list):
                if self._options['site'].endswith('/'):
                    base_url = self._options['site']
                else:
                    base_url = self._options['site']+'/'
                return [base_url+res for res in self._options["router"]]

        except KeyError as e:
            raise Exception

def getRandomUrl(instance=None):
    if not isinstance(instance, Descriptor):
       instance = Descriptor()

    url_list = list(instance.router.keys())
    random_index = randint(0, len(url_list)-1)

    random_resource_key = url_list[random_index]

    return r'{base_url}/{resource}'.format(base_url=instance.site, resource=instance.router[random_resource_key])