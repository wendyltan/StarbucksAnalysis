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

def dataFrame_Construct(oldDataFrame,dataColumnName,newColumnName,insertList,insertDict,dataDict,insertColumnNum):
    """
    easily contruct a new dataframe with one new column for u
    :param oldDataFrame:  your old dataframe name
    :param dataColumnName: your loop data column name
    :param newColumnName:  new column name that u want to insert to the dataframe
    :param insertList:  use to add as a value latter in insertDict
    :param insertDict:  dict that u want to transform into a dataframe
    :param dataDict:   your data as a dict
    :param insertColumnNum: which column will u want to insert into the old dataframe
    :return:
    """

    for column_value in oldDataFrame[dataColumnName]:
        insertList.append(dataDict[column_value])
    insertDict[newColumnName] = insertList
    df = pd.DataFrame(insertDict)
    oldDataFrame.insert(insertColumnNum, newColumnName,df)
    return oldDataFrame


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

    return dataFrame_Construct(dataframe,column,"Rgb Value",column_color_for_df,column_color_df,column_color,len(dataframe.columns))

def count_stabucks_quantity_for_df(starbucks):
    """统计国家中starbucks数量，插入到原有的dataframe中返回"""
    country = count_number_to_dict(starbucks,"Country")
    country_name_for_df = []
    country_name_df = {}

    return dataFrame_Construct(starbucks,'Country',"Country Num",country_name_for_df,country_name_df,country,len(starbucks.columns))

def count_number_to_dict(dataFrame,dataFrameColumnName):
    """
    count one column of dataframe and return data in this column as a dict
    :param dataFrame:  your dataframe
    :param dataFrameColumnName:  your dataFrame column name
    :return:
    """
    target = {}
    for column_name in dataFrame[dataFrameColumnName]:
        if column_name not in target:
            target[column_name] = 1
        if column_name in target:
            target[column_name] = target[column_name] + 1
    return target

def change_alpha2_to_alpha3_for_df(starbucks):
    """原始数据中国家编码为alpha2不能用于画图，需要改为alpha3"""
    alpha_2_to_3 = {}
    country_code3_for_df = []
    country_code3_df = {}
    for c in list(pycountry.countries):
        alpha_2_to_3[c.alpha_2] = c.alpha_3

    return dataFrame_Construct(starbucks,'Country',"Country Code",country_code3_for_df,country_code3_df,alpha_2_to_3,8)

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
        5000: "rgb(81,0,255)",
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

    return dataFrame_Construct(starbucks,"Timezone","Rgb Value",tz_color_for_df,tz_color_df,tz_rgb,len(starbucks.columns))

def distance(lat1,lng1,lat2,lng2):
    """
    caculate the distance accoring to two points' position
    :param lat1:
    :param lng1:
    :param lat2:
    :param lng2:
    :return:
    """
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
    """
    return the top-k points accoring to the position u enter
    :param aimlat: the latitude u enter
    :param aimlng: the longitude u enter
    :param starbucks: starbucks is a dataframe
    :param k: the number of points u want to search
    :param isShowInfo: whether or not show info and draw map
    :param isReturnTime:  whether or not return time
    :return:
    """
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
    Minlat = None
    Minlng = None
    while k > 0:
        MinDistance = -1
        for lat,lng in lat_lng:
            lat = float(lat)
            lng = float(lng)
            #caculate the distance between points in dataframe and your aim point
            two_distance = distance(lat,lng,aimlat,aimlng)
            if MinDistance == -1 or (two_distance < MinDistance):
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
        #drawmap
        dc.draw_map(df,isOpen=False,size=12,newtitle="2.1 k points around the location",export=False,enter_la=aimlat,enter_lon=aimlng)
    endtime = time.time()
    #caculate consume time
    t = endtime - startime
    print("K="+k_key+"的查询时延：%.3f%s" % (t, 's'))

    if isReturnTime:
        t = round(t, 3)
        return t

