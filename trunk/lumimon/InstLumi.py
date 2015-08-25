#!/usr/bin/env python
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

runLSlist={'1100:1':1,'1100:2':1.1,'1100:3':1.3,'1100:4':0.8,'1100:5':0.9,'1100:6':1.05,'1101:1':1,'1101:2':1.01,'1101:3':1.02,'1101:4':0.96}
keys=runLSlist.keys()
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
ax.set_ylabel('Integrated Luminosity [1/fb]',fontsize=15)
fig.autofmt_xdate()
fig.savefig('LumiIntPerRun.png',facecolor='w',edgecolor='w',orientation='portrait')
