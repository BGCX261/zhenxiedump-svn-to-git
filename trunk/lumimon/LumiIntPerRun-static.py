#!/usr/bin/env python
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

runlist={1102:1,1106:2,1307:3,1508:4,1600:5,1730:6,1800:7,1900:8,2100:9,2200:15,2300:18}
keys=runlist.keys()
keys.sort()
values=[]
runs=[]
for key in keys:
      runs.append(key)
      values.append(runlist[key])
fig = Figure()
canvas = FigureCanvas(fig)
ax = fig.add_subplot(111,title='CMS RUN1')
ax.plot(runs,values,'rs-',linewidth=1.0,label='LHC delivered')
eff=0.9
ax.plot(runs,[v*eff for v in values],'gs-',linewidth=1.0,label='CMS recorded')
ax.legend(loc=2,shadow=True)
ax.yaxis.grid(True)
ax.xaxis.grid(False)
ax.set_xlabel('Run',fontsize=15)
ax.set_ylabel('Integrated Luminosity [1/fb]',fontsize=15)
fig.autofmt_xdate()
fig.savefig('LumiIntPerRun-cmsrun1.png',facecolor='w',edgecolor='w',orientation='portrait')
