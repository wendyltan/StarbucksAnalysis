#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 9:10
# @Author  : Wendyltanpcy
# @File    : no_frameobj_helper.py
# @Software: PyCharm
import json
import math
import re
import time
from collections.__init__ import Counter

from src.helper import drawChart as dc


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


def distance(lat1,lng1,lat2,lng2):
    """计算两点间距离,单位为km"""
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


def top_k(d_dict,k=1,isReturnList=False,isReturnTime=False):
    startime = time.time()
    k_list = []
    k_key = str(k)
    for local,d in sorted(d_dict.items(),key=lambda x : x[1]):
        k_list.append(local)
        k -= 1
        if k == 0 :
            break
    endtime = time.time()
    runtime = endtime - startime
    print("K="+k_key+"的查询时延：%.3f%s" % (runtime, 's'))
    runtime = round(runtime,3)
    if isReturnList and isReturnTime:
        return k_list,runtime
    else:
        if isReturnList:
            return k_list
        if isReturnTime:
            return runtime


def top_r(d_dict,r,isReturnList=False,isReturnTime=False):
    startime = time.time()
    r_key = str(r)
    r_list = []
    for local,d in d_dict.items():
        if d < r:
            r_list.append(local)
    endtime = time.time()
    runtime = endtime-startime
    print("R="+r_key+"的查询时延：%.3f%s" %(runtime,'s'))
    runtime = round(runtime,3)
    if isReturnList and isReturnTime:
        return r_list,runtime
    else:
        if isReturnList:
            return r_list
        if isReturnTime:
            return runtime


def show_query_delay(d_dict,k,KorR,st=-1,isOpenHtml=False):
    x_k = []
    y_time = []
    if KorR.upper() == "K":
        if k <= 500:
            for x in range(1, k + 1):
                t = top_k(d_dict, x, isReturnTime=True)
                x_k.append(x)
                y_time.append(t)
        else:
            for x in range(1, k + 1, 35):
                t = top_k(d_dict, x, isReturnTime=True)
                x_k.append(x)
                y_time.append(t)
    if KorR.upper() == "R":
        if k <= 500:
            for x in range(1, k + 1):
                t = top_r(d_dict, x, isReturnTime=True)
                x_k.append(x)
                y_time.append(t)
        else:
            for x in range(1, k + 1, 15):
                t = top_r(d_dict, x, isReturnTime=True)
                x_k.append(x)
                y_time.append(t)
    if st != -1:
        et = time.time()
        runtime = et-st
        print("总运行时间为：%.3f%s" % (runtime, 's'))
    title = "随着" + KorR.upper() + "值得增长查询时延的变化"
    # 折线图
    dc.draw_line_plot(x_k, y_time, title , isOpen=isOpenHtml)
    # 散点图
    # dc.gen_Scatter(y_time,x_k,"随着K值得增长查询时延的变化",isOpen=isOpenHtml)


def grade_save(save_log):
    """将评分记录写入文件中保存下来"""
    try:
        jsobj = json.dumps(save_log)
        fileobj = open("starbucks.json","w")
        fileobj.write(jsobj)
        print("Change Success!")
        fileobj.close()
    except:
        print("Change Error!")


def score(save_log,index_in_starbucks,grade):
    """一次店铺评分功能"""
    i = str(index_in_starbucks)
    g = str(grade)
    # 未曾输入过评分（需求5.1.1）
    if save_log[i]["Grade"] == "":
        if float(g) > 10 or float(g) < 0:
            print("请输入客观的评分！")
            return
        save_log[i]["Grade"] = g
        save_log[i]["N"] += 1
        if float(save_log[i]["Grade"]) >= 8:
            save_log[i]["Special"] = True
        if float(save_log[i]["Grade"]) < 8:
            save_log[i]["Special"] = False
    # 已经输入过评分，暂时当前评分的平均值（需求5.1.2和需求5.1.3）
    else:
        # print(str(save_log[i]["Store Name"]) + "的平均评分为：%.1f" % (float(save_log[i]["Grade"])))
        if float(g) > 10 or float(g) < 0:
            print("请输入客观的评分！")
            return
        average_grade = (float(save_log[i]["Grade"]) * float(save_log[i]["N"]) + float(g)) \
                        /(float(save_log[i]["N"]) + 1)
        save_log[i]["Grade"] = round(average_grade,2)
        save_log[i]["N"] += 1
        if float(save_log[i]["Grade"]) >= 8:
            save_log[i]["Special"] = True
        if float(save_log[i]["Grade"]) < 8:
            save_log[i]["Special"] = False