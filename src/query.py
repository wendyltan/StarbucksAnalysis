#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/17 15:23
# @Author  : Wendyltanpcy
# @File    : query.py
# @Software: PyCharm

from sqlalchemy import func
from sqlalchemy import distinct
from src.util import helper as hp
from src import Session

def get_number_of_country(table,times):
    '''
    获得全球范围内前n的国家
    :param table:
    :param times:
    :return:
    '''
    s = Session()
    #the store count of country
    count = func.count(table.country)
    #select top n of country and their store numbers
    result = s.query(table.country,count).group_by(table.country).order_by(count.desc()).limit(times)
    result_list = hp.row_into_list(result)
    s.close()
    return result_list

def select_city_from_country(table,times,country_code):
    '''
    获得指定国家前n的城市信息
    :param table:
    :param times:
    :param country_code:
    :return:
    '''

    if hp.check_if_valid(country_code):
        s = Session()
        count = func.count(table.city)
        result = s.query(table.city,count).filter(table.country==country_code).group_by(table.city).order_by(count.desc()).limit(times)
        result_list = hp.row_into_list(result)
        s.close()
        return result_list
    else:
        print("Invalid country code!")

def get_ownership_percentage(table):
    '''
    获得全球范围内的所有种类占比
    :param table:
    :return:
    '''
    s = Session()
    count = func.count(table.ownership_type)
    result = s.query(table.ownership_type, count).group_by(table.ownership_type).order_by(count.desc()).all()

    # total_record = count_distinct_records_total(table.ownership_type,False)
    result_list = []
    for k,v in result:
        percent = v
        # percent = '%.2f%%' % (v / total_record * 100)
        result_dict = (k,percent)
        result_list.append(result_dict)
    s.close()
    return result_list

def get_country_store_info(table,country_code):
    '''
    获得指定城市的基本信息
    :param table:
    :param country_code:
    :return:
    '''

    if hp.check_if_valid(country_code):
        s = Session()
        basic = s.query(table.city,table.store_number,table.store_name,table.street_address).filter(table.country==country_code).all()
        count = s.query(func.count(table.store_name)).filter(table.country==country_code).all()
        for row in count:
            count = row[0]

        basic_info = hp.row_into_list(basic)
        top_ten = select_city_from_country(table,10,country_code)

        s.close()
        result_list = [count,basic_info,top_ten]

        return result_list
    else:
        print("Invalid country code!(ex: 'AE')")

def count_distinct_records_total(table_row,count_distinct=True):
    '''
    获得不重复的列结果集
    :param table_row:
    :param count_distinct:
    :return:
    '''

    s = Session()
    if count_distinct:
        result = s.query(func.count(distinct(table_row)))
    else:
        result = s.query(func.count(table_row))
    count=0
    for row in result:
        count = row[0]

    s.close()
    return count

def get_position(table,range='world',country_code=None):

    s = Session()

    if range == 'world':
        #返回世界范围的店铺位置信息
        result = s.query(distinct(table.store_name),table.city,table.longitude,table.latitude).all()
        result_list = hp.row_into_list(result)
        return result_list
    elif range == 'country' and hp.check_if_valid(country_code):
        #返回某个国家的店铺位置信息
        city_count = func.count(table.city)
        store_city_count = s.query(table.city,city_count).filter(table.country==country_code).group_by(table.city).order_by(city_count.desc()).all()
        store_position = s.query(table.store_name,table.city,table.longitude,table.latitude).filter(table.country==country_code)\
        .group_by(table.store_name).all()

        count = hp.row_into_list(store_city_count)
        position = hp.row_into_list(store_position)
        return count,position

    else:
        print("Invalid parameters!")

    s.close()






