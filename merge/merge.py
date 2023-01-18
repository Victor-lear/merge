# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 13:39:06 2023

@author: victor
"""
import sys
import pymongo
from pymongo import MongoClient
import os
import time
from datetime import datetime
import numpy
conn_2= MongoClient("mongodb://admin:bmwee8097218@140.118.122.115:30415/") 
sdb = conn_2['AP_test']
scollection = sdb["Controller4"]
scursor=scollection.find().sort("_id",-1).limit(90)
sdata=[d for d in scursor]
data=[d for d in range(45)]
data_2=[d for d in range(45)]
for i in range(45):
    data[i]=sdata[i]
    data_2[i]=sdata[i+45]
########################################

apname_2=[d for d in range(len(data_2))]
for i in range(len(data)):
    for j in range(len(data_2)):
        if(data[i]['ap_name']==data_2[j]['ap_name']):
            data[i]['channel_busy']=data_2[j]['channel_busy']
            break
print(data[0]['ap_name'])
print(data[0]['channel_busy'])

