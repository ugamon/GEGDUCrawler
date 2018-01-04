from unittest import TestCase
from client import GetData

class TestClient(TestCase):

    def test_Content(self):
        resp = GetData(headers={
            "Content-Type": "text/html;charset=utf-8",
            # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            # "accept-encoding":"gzip, deflate, br",
            # "accept-language":"en-US,en;q=0.9",
            # "cache-control":"no-cache"
        })
        self.assertNotIsInstance(resp.content, bytes)
