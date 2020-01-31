#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:37:35 2020

@author: prajwal
"""
#Problem 1 
import numpy as np
import matplotlib.pyplot as plt 

mu1, sigma1 =  -10, 5 
sample_size = 1000

sample1 = np.random.normal(mu1, sigma1, sample_size)

mu2, sigma2 = 10, 5 
sample2 = np.random.normal(mu2, sigma2, sample_size)

#('full', 'same', 'valid')
sum_of_distributions = np.convolve(sample1, sample2, 'same')

#Draw histogram plot
plt.hist(sum_of_distributions)

#Estimation of mean and stan
n, bins = np.histogram(sum_of_distributions)
midpoints = 0.5 *(bins[1:] + bins[:-1])

mean = np.average(midpoints, weights = n)
variance = np.average((midpoints-mean)**2, weights = n)