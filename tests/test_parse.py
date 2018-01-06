# from client import parse, GetRawData
# from unittest import TestCase
#
# class TestParser(TestCase):
#
#
#     def setUp(self):
#         resp = GetRawData(url="https://google.com",
#                           headers={
#             "Content-Type": "text/html;charset=utf-8",
#
#         })
#         self.inst = parse.ParseThePage(content=resp.content)
#
#     def test_content(self):
#         result = self.inst.get_storage()
#         self.assertEqual([], result)
#
#
