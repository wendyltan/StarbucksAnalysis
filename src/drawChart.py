#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/18 15:22
# @Author  : Wendyltanpcy
# @File    : drawChart.py
# @Software: PyCharm
"""
functions in this script deal with map or chart drawing
"""
import plotly.graph_objs as go
import plotly.offline as off
from src.util import helper as hp


def gen_Bar(datalist1,datalist2,title,export=False):
    """
    绘制条形图
    :param datalist1:
    :param datalist2:
    :param title:
    :param export:
    :return:
    """

    trace = [go.Bar(
        x=datalist1,
        y=datalist2,
    )]

    layout = go.Layout(
        title=title,
    )

    fig = go.Figure(data=trace, layout=layout)
    if export:
        off.plot(fig,image='jpeg',image_filename=title)
    else:
        off.plot(fig, filename=title+'.html')

def gen_Scatter(datalist1,datalist2,title,export=False):
    """
    绘制散点图
    :param datalist1:
    :param datalist2:
    :param title:
    :param export:
    :return:
    """
    trace = [go.Scatter(
        x=datalist2,
        y=datalist1,
        mode='markers',
    )]

    fig = go.Figure(data=trace)
    if export:
        off.plot(fig,image='jpeg',image_filename=title)
    else:
        off.plot(fig, filename=title+'.html')

def gen_Pie(datalist1,datalist2,title,export=False):
    """
    绘制饼图
    :param datalist1:
    :param datalist2:
    :param title:
    :param export:
    :return:
    """
    labels = datalist1
    values = datalist2
    #一些颜色列表
    colors = ['#FEBFB3', '#E1396C', '#96D38C', '#D0F9B1']

    layout = go.Layout(
        title=title,
    )

    trace = [go.Pie(labels=labels, values=values,
                   hoverinfo='label+percent', textinfo='value',
                   textfont=dict(size=20),
                   marker=dict(colors=colors,
                               line=dict(color='#000000', width=2)))]
    fig = go.Figure(data = trace,layout=layout)
    if export:
        off.plot(fig,image='jpeg',image_filename=title)
    else:
        off.plot(fig, filename=title+'.html')



def draw_map(starbucks,continent='world',export=False,isTimeZone=False):
    """
    传入DataFrame的starbucks和洲名，在地图上标出所有点
    :param starbucks:星巴克的所有列数据
    :param continent:可选值[ "world" | "usa" | "europe" | "asia" | "africa" | "north america" | "south america"]
    :return:形成html文件，自动在浏览器打开
    尽量重用和抽象代码避免累赘
    """

    #是否根据时区筛选
    if not isTimeZone:
        starbucks['text'] = starbucks['City'] + ',' + starbucks["Store Name"]
        use_color = 'rgb(141, 211, 199)'
    else:
        starbucks['text'] = starbucks["Store Name"] + ',' + starbucks["Timezone"]
        starbucks = hp.set_random_color_for_df(starbucks, "Timezone")
        use_color = starbucks["Rgb Value"]

    #判断地图范围参数是否有效
    if hp.check_map_range_valid(continent):
        print("Please enter valid range name!")
    else:
        data = [dict(
            type='scattergeo',
            #locationmode='USA-states',貌似没有用，不像文档所述
            lon=starbucks['Longitude'],
            lat=starbucks['Latitude'],
            text=starbucks['text'],
            mode='markers',
            marker=dict(
                size=3,
                opacity=0.8,
                reversescale=True,
                autocolorscale=False,
                symbol='circular',
                color=use_color
            ))]

        layout = dict(
                title='Starbucks in the '+ continent.title() + '<br>',
                geo=dict(
                    scope=continent,
                    showcountries=True,
                    countrycolor="rgb(0,0,0)",
                    showland=True,
                    landcolor="rgb(250, 250, 250)",
                    subunitcolor="rgb(217, 217, 217)",
                    countrywidth=0.5,
                    subunitwidth=0.5
                ),
            )

        fig = dict(data=data,layout=layout)
        if export:
            off.plot(fig, image='jpeg',image_width=1920,image_height=1080, image_filename=continent.title())
        else:
            off.plot(fig, filename=continent.title() + '.html')

#Brand Store Number Store Name  Ownership Type  Street Address  City
#State/Province Country Postcode    Phone Number    Timezone
#Longitude  Latitude


def draw_map_by_country(starbucks):
    data = [dict(
        type='choropleth',
        locations=starbucks['Country Code'],
        z=starbucks['Country Num'],
        text=starbucks['Country'],
        colorscale=[[0, "rgb(5, 10, 172)"],  [0.5, "rgb(70, 100, 245)"],[0.7, "rgb(106, 137, 247)"],
                    [1, "rgb(220, 220, 220)"]],
        # colorscale = [[0,"rgb(139,0,0)"],[0.0006,"rgb(250,0,0)"],[0.06,"rgb(255,48,48)"],[1,"rgb(255,255,255)"]],
        autocolorscale=False,
        reversescale=True,
        marker=dict(
            line=dict(
                color='rgb(255,255,255)',
                width=0.25
            )),
        colorbar=dict(
            title='Quantity'),
    )]

    layout = dict(
        title='Starbucks In The World<br/>',
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection=dict(
                type='Mercator'
            )
        )
    )

    fig = dict(data=data, layout=layout)
    off.plot(fig, filename='requirement3.html')

