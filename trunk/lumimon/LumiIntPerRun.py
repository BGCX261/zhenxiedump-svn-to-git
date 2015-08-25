#!/usr/bin/env python
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

runlist={1102:9.1,1106:9.2,1307:9.3,1508:9.4,1600:9.5,1730:9.6,1800:9.7,1900:9.8,2100:9.9,2200:9.95}
keys=runlist.keys()
keys.sort()
values=[]
runs=[]
for key in keys:
      runs.append(key)
      values.append(runlist[key])
fig = Figure()
canvas = FigureCanvas(fig)
ax = fig.add_subplot(111)
ax.plot(runs,values,'rs-',linewidth=1.0,label='LHC delivered')
eff=0.9
ax.plot(runs,[v*eff for v in values],'gs-',linewidth=1.0,label='CMS recorded')
ax.legend(loc=2,shadow=True)
ax.yaxis.grid(True)
ax.xaxis.grid(False)
ax.set_xlabel('Run',fontsize=15)
ax.set_ylabel('Integrated Luminosity [1/pb]',fontsize=15)
fig.autofmt_xdate()
fig.savefig('LumiIntPerRun.png',facecolor='w',edgecolor='w',orientation='portrait')
