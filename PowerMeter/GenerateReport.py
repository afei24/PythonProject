# -*- coding: UTF-8 -*-
import pymssql
import config
import os
import Report
from datetime import datetime, date, timedelta

MeterAddress = []
reportPath = config.savePath +'\\'+ config.dtCurrentMonth+'.csv'
meterDatas=[]

with pymssql.connect("DESKTOP-QUO241A\SQLEXPRESS", "sa", "admin123", "Decathlon_Blueeye") as conn:
    with conn.cursor() as cursor:
        cursor.execute('SELECT [Address] FROM MeterAddress ')
        row = cursor.fetchone()
        while row:
            MeterAddress.append(row[0])
            row = cursor.fetchone()

        createReport = Report.CreateReport(reportPath,MeterAddress)
        if not os.path.exists(reportPath):
            createReport.Create()
        else:
            for address in MeterAddress:
                meterData = [config.dtCurrentDay,int(address)]
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

