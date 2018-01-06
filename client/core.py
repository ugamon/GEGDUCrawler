from requests import get
#from config.routing import getRandomUrl
from client.utils import write_output_to_file
from config import Descriptor
import random
from time import sleep

class GetRawData(object):
    def __init__(self, url=None, max_retries=3, *args, **kwargs):
        self.status = None
        self.headers = None
        self.content = None
        self.raw = None
        self.success = False
        if url is None:
            url = Descriptor().get_url()

        self.max_retries = max_retries
        self.get(url, *args, **kwargs)

    @write_output_to_file
    def get(self, url, *params, **kwargs):
        while self.max_retries >= 0:

            if "max_retries" not in kwargs.keys():
                self.max_retries -= 1
            try:
                self.request_chameleon(4)
                resp = get(url, *params, **kwargs)
            except Exception as e:
                self.get(url, *params,**kwargs)
            else:
                self.success = True
                self.raw = resp.raw
                self.content = resp.text
                self.status = resp.status_code
                self.headers = resp.headers
                self.url = url
                print(self.url,self.headers,self.status)
                return self.content

    def request_chameleon(self, max_seconds=5):
        if not isinstance(max_seconds,int):
            self.request_chameleon(max_seconds=3)
        else:
            random_seed = random.randrange(0, max_seconds)
            sleep(random_seed)
            return True