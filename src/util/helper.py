#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 0:09
# @Author  : Wendyltanpcy
# @File    : helper.py
# @Software: PyCharm

"""
all help functions go into here
"""

import re
import random
import math
import time
import pycountry
import pandas as pd
from collections import Counter
from src import drawChart as dc


def row_into_list(result):
    """
    read raw result and put it in list
    :param result:
    :return:
    """
    list = []
    for row in result:
        list.append(row)
    return  list

def check_if_valid(country_code):
    '''
    check if country_code is valid
    :param country_code:
    :return:
    '''
    pattern = re.compile('^[A-Z]{2}$')
    result = re.match(pattern, country_code)
    if result:
        return True
    else:
        return False

def check_map_range_valid(continent):
    """
    check if map_country is valid
    :param continent:
    :return:
    """
    valid_range_list = ["world", "usa", "europe", "asia", "africa", "north america", "south america"]
    if continent.lower() in valid_range_list:
        return False
    else:
        return True

def get_seperate_list(raw_result):
    """
    seperate a n-dimension list into n list with group by each item
    ex: gen_seperate_list([[1,'b'],[2,'a']]) >>> [1,2],['b','a']
    :param raw_result:
    :return:
    """

    #get raw_result's item's count
    count = Counter(raw_result[0]).__len__()
    all = Counter(raw_result).__len__()
    i=0
    j=0

    while j < count:
        new_list = []
        while i < all:
            new_list.append(raw_result[i][j])
            i+=1
        yield(new_list)
        i = 0
        j += 1


def set_random_color_for_df(dataframe, column):
    """
    用于生成原有属性对应的随机rgb值，并插入原有的DataFrame中，返回DataFrame数据
    例如set_random_color(starbucks,Timezone)，用于生成不同时区对应不同颜色
    :param dataframe:原有的DataFrame数据
    :param column:根据的列名
    :return:带有“Rgb Value”的DataFrame数据
    """
    column_color = {}
    column_color_for_df = []
    column_color_df = {}
    for column_value in dataframe[column]:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_value = "rgb(" + str(r) + "," + str(g) + "," + str(b) + ")"
        if column_value not in column_color.keys() and rgb_value not in column_color.values():
            column_color[column_value] = rgb_value
    for column_value in dataframe[column]:
        column_color_for_df.append(column_color[column_value])
    column_color_df["Rgb Value"] = column_color_for_df
    color_df = pd.DataFrame(column_color_df)
    dataframe.insert(len(dataframe.columns),"Rgb Value",color_df)
    return dataframe

def count_stabucks_quantity_for_df(starbucks):
    """统计国家中starbucks数量，插入到原有的dataframe中返回"""
    country = {}
    country_name_for_df = []
    country_name_df = {}
    for country_name in starbucks["Country"]:
        if country_name not in country:
            country[country_name] = 1
        if country_name in country:
            country[country_name] = country[country_name] + 1
    for country_name in starbucks['Country']:
        country_name_for_df.append(country[country_name])
    country_name_df["Country Num"] = country_name_for_df
    num_df = pd.DataFrame(country_name_df)
    starbucks.insert(len(starbucks.columns), "Country Num", num_df)
    return starbucks

def change_alpha2_to_alpha3_for_df(starbucks):
    """原始数据中国家编码为alpha2不能用于画图，需要改为alpha3"""
    alpha_2_to_3 = {}
    country_code3_for_df = []
    country_code3_df = {}
    for c in list(pycountry.countries):
        alpha_2_to_3[c.alpha_2] = c.alpha_3
    for country_name in starbucks['Country']:
        country_code3_for_df.append(alpha_2_to_3[country_name])
    country_code3_df["Country Code"] = country_code3_for_df
    code_df = pd.DataFrame(country_code3_df)
    starbucks.insert(8,"Country Code",code_df)
    return starbucks

def timezone_statistics(starbucks):
    """统计每个时区中的店铺数量，返回timezone字典，字典键-值：时区名称-店铺数量"""
    timezone = {}
    for timezone_name in starbucks["Timezone"]:
        if timezone_name not in timezone:
            timezone[timezone_name] = 1
        if timezone_name in timezone:
            timezone[timezone_name] = timezone[timezone_name] + 1
    return timezone

def min_in_dict(dict_name):
    """前提条件：字典的键为数值。取键值最小的数据返回"""
    min_num = -1
    for num in dict_name.keys():
        if min_num == -1:
            min_num = num
        if num < min_num:
            min_num = num
    min_item_value = dict_name.pop(min_num)
    return min_num, min_item_value

def set_timezone_color(starbucks,timezone):
    """设置时区的颜色，并作为一列数据插入dataframe中。然后调用draw_map，实现直接根据点的颜色画图"""
    # 由于数据值大的和小的之间间隔太大，而且在数据值小的地方比较密集，所以采用了直接赋值的方法

    rgb_value = {
        20: "rgb(0,248,255)",
        50: "rgb(10,217,255)",
        100: "rgb(20,186,255)",
        200: "rgb(31,155,255)",
        500: "rgb(41,124,255)",
        800: "rgb(51,93,225)",
        1500:"rgb(61,62,255)",
        3000:"rgb(71,31,255)",
        4890: "rgb(81,0,255)",
    }
    # tz_rgb字典，键-值:时区-RGB
    tz_rgb = {}
    min_num, rgb_color = min_in_dict(rgb_value)
    for key, item in sorted(timezone.items(), key=lambda item: item[1], reverse=False):
        if item <= min_num:
            tz_rgb[key] = rgb_color
        if item > min_num:
            while True:
                min_num, rgb_color = min_in_dict(rgb_value)
                if float(item) < min_num:
                    tz_rgb[key] = rgb_color
                    break
                else:
                    continue
    tz_color_for_df = []
    tz_color_df = {}
    for timezone in starbucks["Timezone"]:
        tz_color_for_df.append(tz_rgb[timezone])
    tz_color_df["Rgb Value"] = tz_color_for_df
    color_df = pd.DataFrame(tz_color_df)
    starbucks.insert(len(starbucks.columns), "Rgb Value", color_df)
    return starbucks

def distance(lat1,lng1,lat2,lng2):
    """已知两点经纬度，计算距离"""
    radlat1 = math.radians(lat1)
    radlat2 = math.radians(lat2)
    a = radlat1 - radlat2
    b = math.radians(lng1) - math.radians(lng2)
    s = 2*math.asin(math.sqrt(math.pow(math.sin(a/2),2)+math.cos(radlat1)*math.cos(radlat2)*math.pow(math.sin(b/2),2)))
    earth_radius = 6378.137
    s = s*earth_radius
    if s < 0:
        return -s
    else:
        return s

def top_k(aimlat,aimlng,starbucks,k=1,isShowInfo=True,isReturnTime=False):
    """实现需求的Top—k函数"""
    startime = time.time()
    latlist = list(starbucks["Latitude"])
    lnglist = list(starbucks["Longitude"])
    lat_lng = list(zip(latlist, lnglist))
    k_key = str(k)
    # 去除经纬度为空的数据
    for lat,lng in lat_lng:
        if lat == '' or lng == '':
            lat_lng.remove((lat,lng))
    k_list = []
    while k > 0:
        MinDistance = -1
        for lat,lng in lat_lng:
            lat = float(lat)
            lng = float(lng)
            two_distance = distance(lat,lng,aimlat,aimlng)
            if MinDistance == -1:
                MinDistance = two_distance
                Minlat = lat
                Minlng = lng
            if two_distance < MinDistance:
                MinDistance = two_distance
                Minlat = lat
                Minlng = lng
        k_list.append((Minlat,Minlng))
        lat_lng.remove((str(Minlat),str(Minlng)))
        k -= 1
    if isShowInfo:
        # 新建一个小的dataframe,只包含符合条件的Starbuck的数据
        df = pd.DataFrame(columns=("City", "Store Name", "Latitude", "Longitude"))
        i = 0
        for x in k_list:
            print(x)
            index = starbucks[(starbucks.Latitude == str(x[0])) & (starbucks.Longitude == str(x[1]))].index.tolist()
            # 给df插入数据
            df.loc[i] = [str(starbucks.iloc[index[0],1]),str(starbucks.iloc[index[0],9]),
                         str(starbucks.iloc[index[0],3]),str(starbucks.iloc[index[0],4])]
            i += 1
        # print(df.head())
        dc.draw_map(df,isOpen=False,size=15,newtitle="2.1 k points around the location",export=False)
    endtime = time.time()
    t = endtime - startime
    print("K="+k_key+"的查询时延：%.3f%s" % (t, 's'))
    if isReturnTime:
        t = round(t, 3)
        return t

