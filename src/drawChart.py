#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/18 15:22
# @Author  : Wendyltanpcy
# @File    : drawChart.py
# @Software: PyCharm
import plotly.graph_objs as go
import  plotly.offline as off
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

def drawWorldMap(locations,shown_value,cover_text,title):
    # df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')
    # print(df)
    data = [dict(
        type='choropleth',
        locations=locations,
        z=shown_value,
        text=cover_text,
        colorscale=[[0, "rgb(5, 10, 172)"], [0.35, "rgb(40, 60, 190)"], [0.5, "rgb(70, 100, 245)"], \
                    [0.6, "rgb(90, 120, 245)"], [0.7, "rgb(106, 137, 247)"], [1, "rgb(220, 220, 220)"]],
        autocolorscale=False,
        reversescale=True,
        marker=dict(
            line=dict(
                color='rgb(180,180,180)',
                width=0.5
            )),
        colorbar=dict(
            autotick=False,
            tickprefix='$',
            title=title),
    )]

    layout = dict(
        title=title,
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection=dict(
                type='Mercator'
            )
        )
    )

    fig = dict(data=data, layout=layout)
    off.plot(fig, validate=False, filename=title+'.html')

def drawCountryMap():
    pass