# -*- coding: utf-8 -*-
from datetime import datetime, date, timedelta
import calendar

savePath=r'C:\PythonProjects'

# get current hours and last hours
t = datetime.today()
dtCurrentDay = str(t.year)+'-'+str(t.month)+'-'+str(t.day)
dtCurrent = str(t.year)+'-'+str(t.month)+'-'+str(t.day)+' '+str(t.hour)+':00:00'
dtLastHour = str(t.year)+'-'+str(t.month)+'-'+str(t.day)+' '+'00:00:00'
LastHour = '0:00'
CurrentHour = '0:59'
if t.hour > 0:
    dtLastHour = str(t.year)+'-'+str(t.month)+'-'+str(t.day)+' '+str(t.hour-1)+':00:00'
    LastHour =str(t.hour-1)+ ':00'
    CurrentHour = str(t.hour-1)+ ':59'
dtCurrentMonth = str(t.year)+'年'+str(t.month)+'月报表'

headers = [r'日期',r'电表编号']
for i in range(0,24):
    headers.append(str(i)+':00-'+str(i)+':59')

timeRanges = []
for i in range(0,24):
    timeRanges.append([str(t.year)+'-'+str(t.month)+'-'+str(t.day)+' '+str(i)+':00:00',
                    str(t.year)+'-'+str(t.month)+'-'+str(t.day)+' '+str(i)+':59:59'])

datePowers = []
monthRange = calendar.monthrange(t.year,t.month)
for i in range(1,monthRange[1]+1) :
    datePowers.append(str(t.year)+'-'+str(t.month)+'-'+str(i))
