#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 0:09
# @Author  : Wendyltanpcy
# @File    : frameobj_helper.py
# @Software: PyCharm

"""
all help functions go into here
"""
import random
from fuzzywuzzy import fuzz
import pandas as pd
from src.helper import drawChart as dc
from src.model.MyDF import MyDataFrame
from src.controller.no_frameobj_helper import min_in_dict, distance, top_k


def set_random_color_for_df(my_frame_obj, column):
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
    for column_value in my_frame_obj.df[column]:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_value = "rgb(" + str(r) + "," + str(g) + "," + str(b) + ")"
        if column_value not in column_color.keys() and rgb_value not in column_color.values():
            column_color[column_value] = rgb_value
    my_frame_obj.addColumn(column, "Rgb Value", column_color_for_df, column_color_df, column_color, len(my_frame_obj.df.columns))
    return my_frame_obj


def set_timezone_color(my_frame_obj,timezone):
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
    my_frame_obj.addColumn("Timezone","Rgb Value",tz_color_for_df,tz_color_df,tz_rgb,len(my_frame_obj.df.columns))
    return my_frame_obj

def count_all_distance(aimlat,aimlng,my_frame_obj):
    """计算所有点到目标点的距离，保存为字典返回"""
    starbucks = my_frame_obj.df
    d_dict = {}
    latlist = list(starbucks["Latitude"])
    lnglist = list(starbucks["Longitude"])
    lat_lng = list(zip(latlist, lnglist))
    # 去除经纬度为空的数据
    for lat, lng in lat_lng:
        if lat == '' or lng == '':
            lat_lng.remove((lat, lng))
    # 开始计算所有数据，并保存在字典中，字典键-值：“（纬度，经度）”-距离,其实应该是“Index-(纬度，经度，距离)”好一点
    for lat, lng in lat_lng:
        lat = float(lat)
        lng = float(lng)
        local = (lat,lng)
        two_distance = distance(lat, lng, aimlat, aimlng)
        d_dict[local] = two_distance
    return d_dict

def show_info_in_map(aimlat,aimlng,my_frame_obj,local_list,t,isOpenHtml=False):
    """在地图上出查到到的点"""
    # 新建一个小的dataframe,只包含符合条件的Starbucks的数据
    df = my_frame_obj.constructSmallFrame(local_list)
    dc.draw_map(df, isOpen=isOpenHtml, size=12, newtitle=t, export=False,
                enter_la=aimlat, enter_lon=aimlng)


def keyword_select(keyword,k,aimlat,aimlng,my_frame_obj,isReturnList=False,isOpen=False):
    """包括完全匹配和部分匹配"""

    starbucks = my_frame_obj.df
    new_columns = starbucks.columns.tolist()
    match_df = pd.DataFrame(columns=new_columns)
    match_df_obj = MyDataFrame()
    match_list = []
    i = 0
    # 第4次迭代，需求3.2，i>0完全匹配
    for index, starbuck in starbucks.iterrows():
        if keyword in starbuck["Store Name"]:
            match_df.loc[i] = starbuck
            lat_lng = (starbuck["Latitude"], starbuck["Longitude"])
            match_list.append(lat_lng)
            i += 1
    if i > 0:
        # listb.insert(0,str(i)+"个。")
        # listb.insert(0,"完全匹配的最多有")
        # listb.insert(0,keyword)
        # listb.insert(0,"关键词为")
        if  i < k:
            print("关键词为"+keyword+"完全匹配的最多有"+str(i)+"个。")
        match_df_obj.setDataFrame(match_df)
        all_d_dict = count_all_distance(aimlat,aimlng,match_df_obj)
        match_list = top_k(all_d_dict, k, isReturnList=True)
        show_info_in_map(aimlat,aimlng,my_frame_obj,match_list,t="4.3 top-k查询+关键词（完全匹配）",isOpenHtml=isOpen)
    # 第4次迭代，需求3.2，i=0进行相似度查询
    if i == 0:
        select_dict_temp = {}
        select_dict = {}
        # 计算keyword和所有店铺名的相似度
        for index, starbuck in starbucks.iterrows():
            ratio = fuzz.token_sort_ratio(keyword, starbuck["Store Name"])
            if ratio == 0:
                continue
            if starbuck["Latitude"] == '' or starbuck["Longitude"] == '':
                continue
            select_dict_temp[index] = [ratio]
        temp = 0.0
        for index, list in sorted(select_dict_temp.items(), key=lambda x: x[1][0], reverse=True):
            if i == 0:
                temp = float(list[0])
                d = distance(aimlat, aimlng, float(starbucks.loc[index]["Latitude"]),
                             float(starbucks.loc[index]["Longitude"]))
                select_dict[index] = (list[0], d)
                i += 1
            else:
                d = distance(aimlat, aimlng, float(starbucks.loc[index]["Latitude"]),
                             float(starbucks.loc[index]["Longitude"]))
                select_dict[index] = (list[0], d)
                if float(list[0]) == float(temp):
                    continue
                else:
                    temp = float(list[0])
                    i += 1
            if i >= k:
                break
        # 现在select_dict 的键-值为“index in starbucks - （相似度，距离）”
        # i重新置为0，返回k个相似度查询结果
        i = 0
        for index, RD in sorted(select_dict.items(), key=lambda value: (value[1][0], value[1][1]), reverse=True):
            # print(RD[0],RD[1],index)
            match_df.loc[i] = starbucks.loc[index]
            # listb.insert(0,match_df.loc[i]["Store Name"])
            if i == 0:
                print("关键词为"+keyword+"模糊匹配结果如下：")
                # listb.insert(0,"关键词为"+keyword+"模糊匹配结果如下：\n")
            print(match_df.loc[i]["Store Name"])
            lat_lng = (match_df.loc[i]["Latitude"],match_df.loc[i]["Longitude"])
            match_list.append(lat_lng)
            i += 1
            if i >= k:
                break
        match_df_obj.setDataFrame(match_df)
        all_d_dict = count_all_distance(aimlat, aimlng, match_df_obj)
        match_list = top_k(all_d_dict, k, isReturnList=True)
        show_info_in_map(aimlat, aimlng, my_frame_obj, match_list, t="4.3 top-k+关键词查询（部分匹配）",isOpenHtml=isOpen)

    if isReturnList:
        return match_list


def change_to_matchdict(KorRlist,my_frame_obj,save_log):
    """传入包含经纬度的list,在数据集中查找对应的index"""
    match_dict = {}
    starbucks = my_frame_obj.df
    i = 1
    for local in KorRlist:
        lat = str(local[0])
        lng = str(local[1])
        # 对于原先为整型的数据，要还原成int，才能在starbucks中找到index。
        if local[0] % 1 == 0.0:
            lat = str(int(local[0]))
        if local[1] % 1 == 0.0:
            lng = str(int(local[1]))
        index = starbucks[(starbucks.Latitude == lat) & (starbucks.Longitude == lng)].index.tolist()
        index_in_starbucks = str(index[0])
        match_dict[i] = {}
        match_dict[i]["index"] = index_in_starbucks
        match_dict[i]["Store Name"] = starbucks.loc[index[0]]["Store Name"]
        match_dict[i]["Grade"] = save_log[index_in_starbucks]["Grade"]
        match_dict[i]["Special"] = save_log[index_in_starbucks]["Special"]
        i += 1
    return match_dict


