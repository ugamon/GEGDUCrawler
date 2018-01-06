#encoding=utf-8

from unittest import TestCase
from datalayer import ItemModelBase


class TestItemModelBase(TestCase):
    def setUp(self):
        self.inst = ItemModelBase("1","short_desc","full_desc","today","12313 руб.")

    def test_instance_price(self):
        self.assertEqual("12313", self.inst.price)

    def test_instance_id(self):
        self.assertEqual("1", self.inst.id)

    def test_instance_short_desc(self):
        self.assertEqual("short_desc", self.inst.sdesc)

    def test_instance_full_desc(self):
        self.assertEqual("full_desc", self.inst.fdesc)

    def test_instance_full_date(self):
        self.assertEqual("today", self.inst.date)
