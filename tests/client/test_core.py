#encoding=utf-8
from client.core import GetRawData
from unittest import TestCase


class TestGetRawData(TestCase):

    def setUp(self):
        self.inst = GetRawData("https://www.samplesite.com/")

    def test_get_content(self):
        self.assertIsNotNone(self.inst.content)
