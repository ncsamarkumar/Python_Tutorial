#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 23:33:21 2020

@author: ncsamarkumar
"""


Height = float(input("Please enter your Height in Meters"))

Weight = int(input("Please enter your Weight in Kilograms"))

BMI = (Weight/(Height*Height))*100

print("Your BMI is : "+str(BMI))