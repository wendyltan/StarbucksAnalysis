import unittest
from src.helper import query


class TestQuery(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_number_of_country(self):
        self.assertEqual("13609", query.get_number_of_country().result_list[1])

    def test_get_country_store_info(self):
        self.assertFalse("", query.get_country_store_info("AE"))
        self.assertEquals(" ", query.get_country_store_info("CN"))


    def test_count_distinct_records_total(self):
        s1=(("1","2"),("1","2"))
        count1= query.count_distinct_records_total(s1, True)
        self.assertEqual(1,count1)
        s2=(("1","2"),("3","4"))
        count2= query.count_distinct_records_total(s2, True)
        self.assertFalse(1,count2)

    def tearDown(self):
        pass

