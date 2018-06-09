#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/17 15:23
# @Author  : Wendyltanpcy
# @File    : query.py
# @Software: PyCharm

"""
Do basic data query from db.
After getting the Dataframe data structure,this script is useless.
"""
from pandas import DataFrame
from sqlalchemy import func
from sqlalchemy import distinct

import src.controller.no_frameobj_helper
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
    result_list = src.controller.no_frameobj_helper.row_into_list(result)
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

    if src.controller.no_frameobj_helper.check_if_valid(country_code):
        s = Session()
        count = func.count(table.city)
        result = s.query(table.city,count).filter(table.country==country_code).group_by(table.city).order_by(count.desc()).limit(times)
        result_list = src.controller.no_frameobj_helper.row_into_list(result)
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

    if src.controller.no_frameobj_helper.check_if_valid(country_code):
        s = Session()
        basic = s.query(table.city,table.store_number,table.store_name,table.street_address).filter(table.country==country_code).all()
        count = s.query(func.count(table.store_name)).filter(table.country==country_code).all()
        for row in count:
            count = row[0]

        basic_info = src.controller.no_frameobj_helper.row_into_list(basic)
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
        result_list = src.controller.no_frameobj_helper.row_into_list(result)
        return result_list
    elif range == 'country' and src.controller.no_frameobj_helper.check_if_valid(country_code):
        #返回某个国家的店铺位置信息
        city_count = func.count(table.city)
        store_city_count = s.query(table.city,city_count).filter(table.country==country_code).group_by(table.city).order_by(city_count.desc()).all()
        store_position = s.query(table.store_name,table.city,table.longitude,table.latitude).filter(table.country==country_code)\
        .group_by(table.store_name).all()

        count = src.controller.no_frameobj_helper.row_into_list(store_city_count)
        position = src.controller.no_frameobj_helper.row_into_list(store_position)
        return count,position

    else:
        print("Invalid parameters!")

    s.close()


def get_dataFrame(table):
    """
    combine all data in database into dataframe format
    'basically this function fuck up everything!'
    But we still get the data out from the db,right?
    :param table:
    :return:
    """
    s = Session()
    result = s.query(table.store_name,table.city,table.store_number,table.brand,\
                     table.ownership_type,table.street_address,table.country,table.postcode,table.phone_number,\
                     table.longitude,table.latitude,table.timezone,table.stateprovince).all()
    result_list = src.controller.no_frameobj_helper.row_into_list(
        src.controller.no_frameobj_helper.get_seperate_list(result))
    starbucks = {}
    starbucks["Store Name"] = result_list[0]
    starbucks["City"] = result_list[1]
    starbucks["Store Number"] = result_list[2]
    starbucks["Brand"] = result_list[3]
    starbucks["Ownership Type"] = result_list[4]
    starbucks["Street Address"] = result_list[5]
    starbucks["Country"] = result_list[6]
    starbucks["Postcode"] = result_list[7]
    starbucks["Phone Number"] = result_list[8]
    starbucks["Longitude"] = result_list[9]
    starbucks["Latitude"] =result_list[10]
    starbucks["Timezone"] = result_list[11]
    starbucks["State/Province"]=result_list[12]

    dataframe = DataFrame(starbucks)

    s.close()
    return dataframe







