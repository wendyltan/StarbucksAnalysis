#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/17 15:23
# @Author  : Wendyltanpcy
# @File    : query.py
# @Software: PyCharm
import re

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from sqlalchemy import distinct

engine = create_engine('sqlite:///starbucks.db')
Session = sessionmaker(bind=engine)

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
    result_list = []
    for row in result:
        result_list.append(row)
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
    pattern = re.compile('^[A-Z]{2}$')
    if re.match(pattern, country_code):
        s = Session()
        count = func.count(table.city)
        result = s.query(table.city,count).filter(table.country==country_code).group_by(table.city).order_by(count.desc()).limit(times)
        result_list = []
        for row in result:
            result_list.append(row)
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

    #25600
    total_record = count_distinct_records_total(table.ownership_type,False)
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
    pattern = re.compile('^[A-Z]{2}$')
    if re.match(pattern,country_code):
        s = Session()
        result = s.query(table.city,table.store_number,table.store_name,table.street_address).filter(table.country==country_code).all()
        count = s.query(func.count(table.store_name)).filter(table.country==country_code).all()
        for row in count:
            count = row[0]
        # print("The count of the store in this country: ",count)
        # print("="*50)
        # print("The basic info is listed below:")
        # print("|city\t\t\t|storeNumber\t\t\t|storeName\t\t\t|streetAddress")
        basic_info = []
        for row in result:
            # print(row)
            basic_info.append(row)

        top_ten = select_city_from_country(table,10,country_code)
        # print("Top ten city info is listed below: ")
        # print(top_ten)
        # print("=" * 50)
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

