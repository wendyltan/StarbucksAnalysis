#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 7:09
# @Author  : Wendyltanpcy
# @File    : MyDF.py
# @Software: PyCharm
import json
import os

import pycountry

import pandas as pd


class MyDataFrame():
    """
    我们的自定义dataframe类，用来包装常用的df操作以及pandas的dataframe
    """

    def __init__(self):
        self.table = None
        self.df = None

    def setTable(self,table):
        self.table = table

    def setDataFrame(self,dataframe):
        self.df = dataframe

    def addColumn(self, dataColumnName, newColumnName, insertList, insertDict, dataDict,
                            insertColumnNum):
        """
        easily contruct a new dataframe with one new column for u
        :param dataColumnName: your loop data column name
        :param newColumnName:  new column name that u want to insert to the dataframe
        :param insertList:  use to add as a value latter in insertDict
        :param insertDict:  dict that u want to transform into a dataframe
        :param dataDict:   your data as a dict
        :param insertColumnNum: which column will u want to insert into the old dataframe
        :return:
        """

        for column_value in self.df[dataColumnName]:
            insertList.append(dataDict[column_value])
        insertDict[newColumnName] = insertList
        df = pd.DataFrame(insertDict)
        self.df.insert(insertColumnNum, newColumnName, df)

    def constructSmallFrame(self,local_list):
        """
        构造一个特定的小型dataframe
        :param local_list:
        :return:
        """
        new_df = pd.DataFrame(columns=("City", "Store Name", "Latitude", "Longitude"))
        i = 0
        for x in local_list:
            print(x)
            lat = str(x[0])
            lng = str(x[1])
            # 对于原先为整型的数据，要还原成int，才能在starbucks中找到index。
            if x[0] % 1 == 0.0:
                lat = str(int(x[0]))
            if x[1] % 1 == 0.0:
                lng = str(int(x[1]))
            index = self.df[(self.df.Latitude == lat) & (self.df.Longitude == lng)].index.tolist()
            # 给df插入数据
            new_df.loc[i] = [str(self.df.iloc[index[0], 1]), str(self.df.iloc[index[0], 9]),
                         str(self.df.iloc[index[0], 3]), str(self.df.iloc[index[0], 4])]
            i += 1
        return new_df


    def change_alpha2_to_alpha3_for_df(self):
        """原始数据中国家编码为alpha2不能用于画图，需要改为alpha3"""
        alpha_2_to_3 = {}
        country_code3_for_df = []
        country_code3_df = {}
        for c in list(pycountry.countries):
            alpha_2_to_3[c.alpha_2] = c.alpha_3
        self.addColumn('Country',"Country Code",country_code3_for_df,country_code3_df,alpha_2_to_3,8)
        return self


    def grade_read(self):
        """读取评分记录的文件，如果没有则生成"""
        starbucks = self.df
        if not os.path.exists("starbucks.json"):
            save_log = {}
            for index,starbuck in starbucks.iterrows():
                index = str(index)
                save_log[index] = {}
                save_log[index]["Store Name"] = starbuck["Store Name"]
                # save_log[index]["Latitude"] = starbuck["Latitude"]
                # save_log[index]["Longitude"] = starbuck["Longitude"]
                save_log[index]["Grade"] = ""
                save_log[index]["N"] = 0
                save_log[index]["Special"] = False
            try:
                jsobj = json.dumps(save_log)
                fileobj = open("starbucks.json","w")
                fileobj.write(jsobj)
                print("Save Success!")
                fileobj.close()
            except:
                print("Save Error!")
        else:
            with open("starbucks.json","r") as fileobj:
                save_log = json.loads(fileobj.read())
                print("Read Success!")
        return save_log




    def count_number_to_dict(self,dataFrameColumnName):
        """
        count one column of dataframe and return data in this column as a dict
        :param dataFrame:  your dataframe
        :param dataFrameColumnName:  your dataFrame column name
        :return:
        """
        target = {}
        for column_name in self.df[dataFrameColumnName]:
            if column_name not in target:
                target[column_name] = 1
            if column_name in target:
                target[column_name] = target[column_name] + 1
        return target

    def count_stabucks_quantity_for_df(self):
        """统计国家中starbucks数量，插入到原有的dataframe中返回"""
        country = self.count_number_to_dict("Country")
        country_name_for_df = []
        country_name_df = {}
        self.addColumn('Country',"Country Num",country_name_for_df,country_name_df,country,len(self.df.columns))
        return self
