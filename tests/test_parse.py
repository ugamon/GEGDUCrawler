from client import parse, GetRawData
from unittest import TestCase

class TestParser(TestCase):
    def setUp(self):
        resp = GetRawData(headers={
            "Content-Type": "text/html;charset=utf-8",
            # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            # "accept-encoding":"gzip, deflate, br",
            # "accept-language":"en-US,en;q=0.9",
            # "cache-control":"no-cache"
        })
        self.inst = parse.ParseThePage(content=resp.content)

    def test_content(self):
        pass


