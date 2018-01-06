#encoding=utf-8
from client.parse import ParseThePage
# from client.parse import ContentFilters
import unittest
from unittest import TestCase
from copy import copy

html_template = "<html><head><div>test</div></head></html>"

class TestParseThePage(TestCase):

    def test_initiation(self):
        _html_template = copy(html_template)
        self.inst = ParseThePage(content=_html_template)
        self.inst.parse()
        self.assertEqual(self.inst.get_storage(), [])


# class TestContentFilters(TestCase):
#
#     @unittest.expectedFailure
#     def test_initiation_fail(self):
#         inst = ContentFilters('sample')
#         self.assertEqual(inst.filters, 'sample')
#
#     def test_initiation_success(self):
#         inst = ContentFilters(['first'])
#         self.assertEqual(inst.filters, ['first'])
#
#     def test_adding_values(self):
#         inst = ContentFilters(['first'])
#         inst+'second'
#         self.assertEqual(inst.filters, ['first', 'second'])
#
#     def test_yield_values(self):
#         inst = ContentFilters(['first', 'second', 'third', 'forth'])
#         _temp = []
#         for i in inst.all():
#             _temp.append(i)
#         self.assertEqual(['first', 'second', 'third', 'forth'], _temp)
#
#     def test_depth(self):
#         inst = ContentFilters(['first', 'second', 'third', 'forth'])
#         self.assertEqual(inst.depth(), 4)
#
#     def test_last_with_change(self):
#         inst = ContentFilters(['first', 'second', 'third', 'forth'])
#         _before = copy(inst.filters)
#         result = inst.last(True)
#         _after = inst.filters
#         assert _before > _after
#         self.assertEqual("forth", result)
#
#     def test_last_without_change(self):
#         inst = ContentFilters(['first', 'second', 'third', 'forth'])
#         _before = copy(inst.filters)
#         result = inst.last()
#         _after = inst.filters
#         assert _before == _after
#         self.assertEqual("forth", result)
#
#     def test_first_with_change(self):
#         inst = ContentFilters(['first', 'second', 'third', 'forth'])
#         _before = copy(inst.filters)
#         result = inst.first(True)
#         _after = inst.filters
#         assert len(_before) > len(_after)
#         self.assertEqual("first", result)
#
#     def test_first_without_change(self):
#         inst = ContentFilters(['first', 'second', 'third', 'forth'])
#         _before = copy(inst.filters)
#         result = inst.first()
#         _after = inst.filters
#         assert len(_before) == len(_after)
#         self.assertEqual("first", result)