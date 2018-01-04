from requests import get
#from config.routing import getRandomUrl
from client.utils import writeOutputToFile
from config import Descriptor
import random
from time import sleep

class GetData(object):
    def __init__(self,url=None,max_retries=3,*args,**kwargs):
        self.status = None
        self.headers = None
        self.content = None
        self.raw = None
        self.success = False
        if url is None:
            url = Descriptor().get_url()

        self.max_retries = max_retries
        self.__resilent(url,*args,**kwargs)

    @writeOutputToFile
    def __resilent(self, url, *params, **kwargs):
        while self.max_retries >= 0:
            _rand = random.randrange(2, 10)
            if "max_retries" not in kwargs.keys():
                self.max_retries -= 1
            try:
                sleep(_rand)
                resp = get(url,*params,**kwargs)
            except Exception as e:
                self.__resilent(url,*params,**kwargs)
            else:
                self.success = True
                self.raw = resp.raw
                self.content = resp.text
                self.status = resp.status_code
                self.headers = resp.headers
                self.url = url
                print(self.url,self.headers,self.status)
                return self.content

