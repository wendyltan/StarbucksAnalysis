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
    labels = datalist1
    values = datalist2
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

def draw_map(starbucks,continent='world',export=False):
    """
    传入DataFrame的starbucks和洲名，在地图上标出所有点
    :param starbucks:至少包括城市，店名，经纬度
    :param continent:可选值[ "world" | "usa" | "europe" | "asia" | "africa" | "north america" | "south america"]
    :return:形成html文件，自动在浏览器打开
    """
    starbucks['text'] = starbucks['City'] + ',' + starbucks["Store Name"]
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




#Brand Store Number	Store Name	Ownership Type	Street Address	City
#State/Province	Country	Postcode	Phone Number	Timezone
#Longitude	Latitude

def draw_map_by_timezone(starbucks,export=False):
    starbucks = hp.set_random_color(starbucks, "Timezone")
    starbucks['text'] = starbucks["Store Name"] + ',' + starbucks["Timezone"]
    continent = "world"
    data = [dict(
        type='scattergeo',
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
            color=starbucks["Rgb Value"]
        ))]

    layout = dict(
        title='Starbucks in the ' + continent.title() + '<br>',
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

    fig = dict(data=data, layout=layout)
    if export:
        off.plot(fig, image='jpeg', image_width=1920, image_height=1080, image_filename=continent.title())
    else:
        off.plot(fig, filename=continent.title() + '.html')