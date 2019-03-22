# -*- coding: UTF-8 -*-
import pymssql
import config
import os
import Report
from datetime import datetime, date, timedelta
import codecs

MeterAddress = []
MeterName = []
reportPath = config.savePath +'\\'+ config.dtCurrentMonth+'.csv'
meterDatas=[]

with pymssql.connect("DESKTOP-QUO241A\SQLEXPRESS", "sa", "admin123", "Decathlon_Blueeye",charset='utf8') as conn:
    with conn.cursor() as cursor:
        cursor.execute('SELECT [Address],[Name] FROM MeterAddress ')
        row = cursor.fetchone()
        while row:
            MeterName.append(row[1])
            MeterAddress.append(row[0])
            row = cursor.fetchone()

        createReport = Report.CreateReport(reportPath,MeterAddress)
        print(MeterName)
        if not os.path.exists(reportPath):
            createReport.Create()
        else:
            for i in range(0,len(MeterAddress)):
                name = MeterName[i]
                address = MeterAddress[i]
                meterData = [config.dtCurrentDay,name]
                for timeRange in config.timeRanges:
                    sql = "SELECT TOP 1  PwTotal  FROM DLT_10H_F1_0001FF00 WHERE [Address]='%s' and ([CreateTime]<'%s' or [CreateTime]='%s') order by CreateTime desc" % \
                          (address, timeRange[0], timeRange[0])
                    cursor.execute(sql)
                    row = cursor.fetchone()
                    lastPwTotal = row[0]

                    sql = "SELECT TOP 1  PwTotal  FROM DLT_10H_F1_0001FF00 WHERE [Address]='%s' and ([CreateTime]<'%s' or [CreateTime]='%s') order by CreateTime desc" % \
                          (address, timeRange[1], timeRange[1])
                    cursor.execute(sql)
                    row = cursor.fetchone()
                    currentPwTotal = row[0]
                    meterData.append(str(float(currentPwTotal)-float(lastPwTotal)))

                meterDatas.append(meterData)

print(meterDatas)
createReport.Update(meterDatas)

