from client import parse, GetData
from unittest import TestCase
from config import Descriptor
class TestParser(TestCase):
    def setUp(self):
        for url in Descriptor(max_depth=1).get_url():
            resp = GetData(url=url,
                           headers={
                               "Content-Type": "text/html;charset=utf-8",
                               # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                               # "accept-encoding":"gzip, deflate, br",
                               # "accept-language":"en-US,en;q=0.9",
                               # "cache-control":"no-cache"
                           })
            self.inst = parse.ParseThePage(content=resp.content)

    def test_content(self):
        pass


