#!/usr/bin/env python
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.dates as mdates
from datetime import datetime

datelist={'2009-11-15':0.1,'2009-12-15':0.15,'2010-01-15':1,'2010-02-15':1.5,'2010-03-05':8.0,'2010-03-25':8.8,'2010-04-09':9.1,'2010-04-25':9.5,'2010-05-04':18,'2010-05-15':18.5,'2010-06-27':18.8,'2010-07-01':35,'2010-07-16':36.0,'2010-07-29':36.8,'2010-08-01':26.1,'2010-08-14':26.3,'2010-08-20':26.7,'2010-08-31':26.1,'2010-09-01':23.1,'2010-09-07':23.6,'2010-09-15':23.8,'2010-09-23':23.9,'2010-09-29':24,'2010-10-01':46.01,'2010-10-15':46.1,'2010-10-25':46.5,'2010-10-31':46.9,'2010-11-02':68.9,'2010-11-15':69.1,'2010-11-24':69.8,'2010-11-29':70,'2010-12-01':110.0,'2010-12-07':110.5,'2010-12-10':110.7,'2010-12-18':110.9,'2010-12-21':111}
keys=datelist.keys()
keys.sort()
values=[]
times=[]
for key in keys:
      values.append(datelist[key])
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
ax.legend(loc=2,shadow=True)
ax.yaxis.grid(True)
ax.xaxis.grid(False)
ax.set_xlabel('Date',fontsize=15)
ax.set_ylabel('Integrated Luminosity [1/pb]',fontsize=15)
ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()
fig.savefig('LumiIntPerDay.png',facecolor='w',edgecolor='w',orientation='portrait')
