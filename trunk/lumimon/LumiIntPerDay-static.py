#!/usr/bin/env python
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.dates as mdates
from datetime import datetime

datelist={'2009-11-15':(7,0.1),'2009-12-15':(7,0.15),'2010-01-15':(7,1),'2010-02-15':(7,1.5),'2010-03-05':(7,8.0),'2010-03-25':(7,8.8),'2010-04-09':(7,9.1),'2010-04-25':(7,9.5),'2010-05-04':(7,18),'2010-05-15':(7,18.5),'2010-06-27':(7,18.8),'2010-07-01':(7,35),'2010-07-16':(7,36.0),'2010-07-29':(7,36.8),'2010-08-01':(9,26.1),'2010-08-14':(9,26.3),'2010-08-20':(9,26.7),'2010-08-31':(9,26.1),'2010-09-01':(9,23.1),'2010-09-07':(9,23.6),'2010-09-15':(9,23.8),'2010-09-23':(9,23.9),'2010-09-29':(9,24),'2010-10-01':(9,46.01),'2010-10-15':(9,46.1),'2010-10-25':(9,46.5),'2010-10-31':(9,46.9),'2010-11-02':(9,68.9),'2010-11-15':(9,69.1),'2010-11-24':(9,69.8),'2010-11-29':(9,70),'2010-12-01':(9,110.0),'2010-12-07':(9,110.5),'2010-12-10':(9,110.7),'2010-12-18':(9,110.9),'2010-12-21':(9,111)}
keys=datelist.keys()
print keys
keys.sort()
values=[]
cms7values=[]
cms9values=[]
times=[]
for key in keys:
      (cms,lumiint) = datelist[key]
      values.append(lumiint)
      if (cms==7):
         cms7values.append(lumiint) 
      else:
         cms7values.append(0)
      if (cms==9):
         cms9values.append(lumiint)
      else: 
         cms9values.append(0)
      times.append(datetime.strptime(key,'%Y-%m-%d'))
months = mdates.MonthLocator()
days = mdates.DayLocator()
yearsFmt =  mdates.DateFormatter('%b')
dayFmt = mdates.DateFormatter('%d')
fontsize=5
fig = Figure()
canvas = FigureCanvas(fig)
ax = fig.add_subplot(111)
dates = range(times[0].toordinal(), times[-1].toordinal())
ax.plot(times,values,'rs-',linewidth=1.0,label='LHC delivered')
eff=0.9
ax.plot(times,[v*eff for v in values],'gs-',linewidth=1.0,label='CMS recorded')
ax.plot(times,[v*eff for v in cms7values],'bs-',linewidth=1.0,label='CMS recorded Y(7Tev)')
ax.plot(times,[v*eff for v in cms9values],'cs-',linewidth=1.0,label='CMS recorded Y(9Tev)')
ax.legend(loc=2,shadow=True)
ax.yaxis.grid(True)
ax.xaxis.grid(False)
ax.set_xlabel('Date',fontsize=15)
ax.set_ylabel('Integrated Luminosity [1/pb]',fontsize=15)
ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()
fig.savefig('LumiIntPerDay2010.png',facecolor='w',edgecolor='w',orientation='portrait')
