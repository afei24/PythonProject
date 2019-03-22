#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import csv
import config

class CreateReport:
    #create or update report

    def __init__(self,path,meterAddress):
        self.path = path
        self.meterAddress = meterAddress

    def Create(self):
        if os.path.exists(self.path):
            return
        else:
            with open(self.path, 'w',newline='') as f:
                writer = csv.DictWriter(f, config.headers)
                writer.writeheader()

    def Update(self,datas):
        if not os.path.exists(self.path):
            return
        else:
            with open(self.path, 'a', newline='') as f:
                writer = csv.writer(f)
                for data in datas:
                    writer.writerow(data)