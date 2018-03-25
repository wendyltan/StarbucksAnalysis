#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/25 20:50
# @Author  : Wendyltanpcy
# @File    : test.py
# @Software: PyCharm
import unittest
from src.util import helper as hp
class TestMain(unittest.TestCase):
    """
    Written all test codes here,currently only for helper.py
    """

    def setUp(self):
        pass


    def test_row_into_list(self):
        result=(('1','2'),('A','B'))
        list = hp.row_into_list(result)
        self.assertEquals(list,[('1','2'),('A','B')])

    def test_check_if_valid(self):
        country_code='AE'
        self.assertTrue(hp.check_if_valid(country_code))

    def test_check_map_range_valid(self):
        continent = 'asia'
        self.assertFalse(hp.check_map_range_valid(continent))


    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()