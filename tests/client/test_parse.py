#encoding=utf-8
from client.parse import ParseThePage
from client.parse import ContentFilters
import unittest
from unittest import TestCase
from copy import copy
from config import Descriptor
from client import GetRawData
import os

html_template = "<html><head><div>test</div></head></html>"

class TestParseThePage(TestCase):

    def test_initiation(self):
        _html_template = copy(html_template)
        inst = ParseThePage(content=_html_template).parse()
        self.assertEqual(inst.get_storage(), [])

    def test_if_working(self):
        url = Descriptor().get_url()
        raw_data = GetRawData(url=url,
                              headers={
                                  "Content-Type": "text/html;charset=utf-8",
                                  "user-agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
                              },

                              interval=3)
        assert raw_data.success
        inst = ParseThePage(raw_data.content)
        self.assertGreater(len(inst.get_storage()), 0)

    def test_if_working_output(self):
        url = Descriptor().get_url()
        raw_data = GetRawData(url=url,
                              headers={
                                  "Content-Type": "text/html;charset=utf-8",
                                  "user-agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
                              },

                              interval=3)
        assert raw_data.success
        _filename = "sample_test.csv"
        inst = ParseThePage(raw_data.content).output(_filename)

        with open(_filename) as f:
            _number_of_lines = sum(1 for _ in f)

        self.assertEqual(len(inst.get_storage()), _number_of_lines)


class TestContentFilters(TestCase):

    @unittest.expectedFailure
    def test_initiation_fail(self):
        inst = ContentFilters('sample')
        self.assertEqual(inst.filters, 'sample')

    def test_initiation_success(self):
        inst = ContentFilters([('first', 'first')])
        self.assertEqual(inst.first(), ('first', 'first'))

    def test_adding_values(self):
        inst = ContentFilters([('first', 'first')])
        inst+(('attr', 'second'))
        self.assertEqual(inst.last(), ('attr', 'second'))

    def test_yield_values(self):
        inst = ContentFilters([('first', 'first')])
        _temp = []
        for i in inst.all():
            _temp.append(i)
        self.assertEqual([('first', 'first')], _temp)

    def test_depth(self):
        inst = ContentFilters([('first', 'first')])
        self.assertEqual(inst.depth(), 1)

    def test_last_with_change(self):
        inst = ContentFilters([('first', 'first')])
        _before = copy(inst.filters)
        result = inst.last(True)
        _after = inst.filters
        assert _before > _after
        self.assertEqual(('first', 'first'), result)

    def test_last_without_change(self):
        inst = ContentFilters([('first', 'first')])
        _before = copy(inst.filters)
        result = inst.last()
        _after = inst.filters
        assert _before == _after
        self.assertEqual(('first', 'first'), result)

    def test_first_with_change(self):
        inst = ContentFilters([('first', 'first')])
        _before = copy(inst.filters)
        result = inst.first(True)
        _after = inst.filters
        assert len(_before) > len(_after)
        self.assertEqual(('first', 'first'), result)

    def test_first_without_change(self):
        inst = ContentFilters([('first', 'first')])
        _before = copy(inst.filters)
        result = inst.first()
        _after = inst.filters
        assert len(_before) == len(_after)
        self.assertEqual(('first', 'first'), result)