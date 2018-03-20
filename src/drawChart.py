#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/18 15:22
# @Author  : Wendyltanpcy
# @File    : drawChart.py
# @Software: PyCharm
import plotly.graph_objs as go
import  plotly.offline as off
import plotly.plotly as py
import pandas as pd


def gen_Bar(datalist1,datalist2,title):

    trace = [go.Bar(
        x=datalist1,
        y=datalist2,
    )]

    layout = go.Layout(
        title=title,
    )

    fig = go.Figure(data=trace, layout=layout)
    off.plot(fig, filename=title+'.html')
    print("success!")

def gen_Scatter(datalist1,datalist2,title):
    trace = [go.Scatter(
        x=datalist2,
        y=datalist1,
        mode='markers',
    )]


    off.plot(trace, filename=title+'.html')
def gen_Pie(datalist1,datalist2,title):
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
    off.plot(fig,filename=title+'.html')
    print("success!")

def draw_map(starbucks,continent):
    """
    传入DataFrame的starbucks和洲名，在地图上标出所有点
    :param starbucks:至少包括城市，店名，经纬度
    :param continent:可选值【 "world" | "usa" | "europe" | "asia" | "africa" | "north america" | "south america"】
    :return:形成html文件，自动在浏览器打开
    """
    starbucks['text'] = starbucks['City'] + ',' + starbucks["Store Name"]
    country = continent

    data = [dict(
        type='scattergeo',
        locationmode='World',
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
            title='Starbucks in the World<br>',
            geo=dict(
                scope=country,
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
    off.plot(fig)#,image='jpeg')
