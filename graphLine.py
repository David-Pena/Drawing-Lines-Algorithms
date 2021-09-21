# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 17:15:40 2021

@author: David Peña, Sebastián Matute, Alejandro Ponce
"""

from matplotlib import pyplot as plt
import math
import time

'''
    Only implementation that uses for loop
'''
def basicImplementation(x1, y1, x2, y2, color):
    y = 0.0
    
    for x in range(x2):
        y = y1 + (x-x1)*(y2-y1) / (x2-x1)
        drawPixel(x, round(y), color)

'''
    Same as code above but using while instead of for loop
'''
def basicImplementation2(x1, y1, x2, y2, color):
    y = 0.0
    x = x1
    while x <= x2:
        y=(y1+(x-x1)*(y2-y1))/(x2-x1)
        drawPixel(x, round(y), color)
        x += 1

def improvingImplementation(x1, y1, x2, y2, color):
    m = y = 0.0
    dx = dy = x = 0
    dx = x2 - x1
    dy = y2 - y1
    m = dy / dx
    y = y1 + .5
    
    x = x1
    while x <= x2:
        drawPixel(x, math.floor(y), color)
        y = y + m
        x += 1

def incrementalImplementation(x1, y1, x2, y2, color):
    Xincrease = Yincrease = x = y = 0.0
    dx = dy = step = k = 0
    dx = x2 - x1
    dy = y2 - y1
    step = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    Xincrease = dx / step
    Yincrease = dy / step
    x = x1
    y = y1
    drawPixel(round(x), round(y), color)
    
    k = 1
    while k <= step:
        x += Xincrease
        y += Yincrease
        drawPixel(round(x), round(y), color)
        k += 1

def bresenhamImplementation(x1, y1, x2, y2, color):
    m = 2 * (y2 - y1)
    slope_error = m - (x2 - x1)
    y = y1
    
    x = x1
    while x<=x2:
        drawPixel(x, y, color)
        # add slope to increment angle formed
        slope_error += m
        # if slope reached limit, we
        # increment y and update slope error
        if slope_error >= 0:
            y += 1
            slope_error = slope_error - 2 * (x2 - x1)
        x += 1

def drawPixel(x, y, color):
    plt.plot(x, y, marker=".", color=color)
    
def clockRuntime(name, func, *args):
    start = 0
    end = 0
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    result = end - start
    
    runtimeList.append([name, result])

    print(f"Runtime of {name} was: {end - start:0.15f} nanoseconds")
    
    plt.show()
    
def getFaster(arr):
    lowest = 99999
    title = ''
    for el in arr:
        if el[1] < lowest:
            lowest = el[1]
            title = el[0]
            
    print(f"\nThe fastest implementation was: {title} with a runtime of: {lowest} nanoseconds")

if __name__ == '__main__':
    runtimeList = []
    
    print("\nPresented by: David Peña, Sebastián Matute, & Alejandro Ponce\n")
    
    clockRuntime('BASIC IMPLEMENTATION', basicImplementation, 1, 1, 500, 500, 'red')
    clockRuntime('BASIC IMPLEMENTATION (USING WHILE)', basicImplementation2, 1, 1, 500, 500, 'darkred')
    clockRuntime('IMPROVED IMPLEMENTATION', improvingImplementation, 1, 1, 500, 500, 'blue')
    clockRuntime('INCREMENTAL IMPLEMENTATION', incrementalImplementation, 1, 1, 500, 500, 'lightblue')
    clockRuntime('BRESENHAM IMPLEMENTATION', bresenhamImplementation, 1, 1, 500, 500, 'lightyellow')
    
    getFaster(runtimeList)

    
    