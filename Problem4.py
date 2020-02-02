#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 19:47:21 2020

@author: prajwal
"""
#Problem 4 
import matplotlib.pyplot as plt
import numpy as np 
mean = [-5, 5]
cov = [[20, 0.8],[0.8,30]]
n = 10000
x, y = np.random.multivariate_normal(mean, cov, n).T

estimated_mean_x = sum(x)/n
estimated_mean_y = sum(y)/n

#check if n or n-1
var_x = 1/n*sum((x-estimated_mean_x)*(x-estimated_mean_x))
var_y = 1/n*sum((y-estimated_mean_y)*(y-estimated_mean_y))
    
cov_xy = 1/n*sum((x-estimated_mean_x)*(y-estimated_mean_y))
estimated_cov_matrix = [[var_x, cov_xy],[cov_xy, var_y]]
