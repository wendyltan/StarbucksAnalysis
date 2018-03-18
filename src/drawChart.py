#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/18 15:22
# @Author  : Wendyltanpcy
# @File    : drawChart.py
# @Software: PyCharm
import plotly.graph_objs as go
import  plotly.offline as off
import numpy as np

def gen_Bar(datalist1,datalist2,title):

    trace = [go.Bar(
        x=datalist1,
        y=datalist2,
        text = datalist2,
    )]

    layout = go.Layout(
        title=title,
    )

    fig = go.Figure(data=trace, layout=layout)
    off.plot(fig, filename=title)
    print("success!")

def gen_Scatter(datalist1,datalist2):
    trace = [go.Scatter(
        x=datalist2,
        y=datalist1,
        mode='markers',
    )]


    off.plot(trace, filename='scatter-plot-with-colorscale.html')
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
    off.plot(fig,filename=title)
    print("success!")