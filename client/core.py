from requests import get
#from config.routing import getRandomUrl
from client.utils import write_output_to_file
from config import Descriptor
import random
from time import sleep

class GetRawData(object):
    def __init__(self, url=None, max_retries=3, interval=5, routing=None, *args, **kwargs):
        self.status = None
        self.headers = None
        self.content = None
        self.raw = None
        self.success = False
        if url is None:
            if routing and isinstance(routing, Descriptor):
                url = routing.get_url()
            else:
                raise ValueError("Routing parameter should be Descriptor() type.")

        if not isinstance(url, str):
            raise ValueError("url should be string.")

        if isinstance(interval, int):
            self._interval = interval
        else:
            self._interval = 5

        self.max_retries = max_retries

        self.__get(url, *args, **kwargs)

    def __get(self, url, *params, **kwargs):
        print(url)
        while self.max_retries >= 0:

            if "max_retries" not in kwargs.keys():
                self.max_retries -= 1
            try:
                self.request_chameleon(self._interval, 3)
                resp = get(url, *params, **kwargs)
            except Exception as e:
                print(e)
                self.__get(url, *params, **kwargs)
            else:
                self.success = True
                self.raw = resp.raw
                self.content = resp.text
                self.status = resp.status_code
                self.headers = resp.headers
                self.url = url
                print(self.url,self.headers,self.status)
                return self.content

    def request_chameleon(self, max_seconds, min_seconds=0):
        if not isinstance(max_seconds, int):
            self.request_chameleon(max_seconds=3)
        else:
            random_seed = random.randrange(min_seconds, max_seconds)
            sleep(random_seed)
            return True