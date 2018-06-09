#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/25 20:50
# @Author  : Wendyltanpcy
# @File    : test_helper.py
# @Software: PyCharm
import math
import unittest

import src.model.MyDF
import src.controller.no_frameobj_helper


class TestHelper(unittest.TestCase):
    """
    Written all test codes here,currently only for frameobj_helper.py
    """

    def setUp(self):
        pass


    def test_row_into_list(self):
        result=(('1','2'),('A','B'))
        list = src.controller.no_frameobj_helper.row_into_list(result)
        self.assertEquals(list,[('1','2'),('A','B')])

    def test_check_if_valid(self):
        country_code='AE'
        self.assertTrue(src.controller.no_frameobj_helper.check_if_valid(country_code))

    def test_check_map_range_valid(self):
        continent = 'asia'
        self.assertFalse(src.controller.no_frameobj_helper.check_map_range_valid(continent))
        
    def test_distance(self,lat1,lng1,lat2,lng2):
        radlat1 = math.radians(lat1)
        radlat2 = math.radians(lat2)
        lat1=23.022
        lng1=113.121
        lat2=23.129
        lng2= 113.264
        distance=18.889
        a = radlat1 - radlat2
        b = math.radians(lng1) - math.radians(lng2)
        s = 2*math.asin(math.sqrt(math.pow(math.sin(a/2),2)+math.cos(radlat1)*math.cos(radlat2)*math.pow(math.sin(b/2),2)))
        earth_radius = 6378.137
        s = s*earth_radius
        self.assertEquals(s,distance);

    def test_top_k(self):
        self.assertFalse(103.84, 36.05, src.top_k(101.76, 36.63))
        
    def test_count_starbucks_quantity_for_df(self):
        country="CN"
        count= src.model.MyDF.count_stabucks_quantity_for_df()
        self.assertEqual(2735,count)


    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()
