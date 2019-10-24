import calendar
from pprint import pprint
from datetime import date
import numpy as np
from numpy import random
import pylab as pl
from matplotlib import collections  as mc
from random import randint
from random import uniform
from app.classIntervalo import *

arrDatas = []

for i in range(16):
    arrDatas.append(Intervalo.geraUmaDataAleatoria(None)) #pontos temporais


#converter datas para ordinal
# plotar ordinal
#mas os textos que aparecem devem ser convertidos novamente em datas para facilitar entendimento
labelsX = arrDatas#["data1", "data2", "data3"]
labelsY = ["Temperature", "Wind speed", "Humidity", "Rain", "Floor","x","k"]

lines = [[(0, 0), (1, 0)],
         [(2, 1), (5, 1)],
         [(2, 3), (3, 3)],
         [(4, 3), (5, 3)],
         [(5, 8), (15, 8)],
         [(1, 2), (3, 2)]]
colorLine = []

for i in range(len(lines)+1):
    colorLine.append((random.uniform(0.0,1.0), random.uniform(0.0,1.0), random.uniform(0.0,1.0), 1))

lc = mc.LineCollection(lines, colors=colorLine, linewidths=3)
fig, axis = pl.subplots()

# pl.xticks([0.2, 1.4, 2.6, 5.8, 10.],
           # ["Jan\n2009", "Feb\n2009", "Mar\n2009", "Apr\n2009", "May\n2009"])
qtdDatas =len(arrDatas)

# pl.xticks(np.arange(12), calendar.month_name[1:13], rotation=45)
pl.yticks(np.arange(len(labelsY)),labelsY)
pl.xticks(np.arange(len(labelsX)),labelsX, rotation=90)

axis.add_collection(lc)
axis.autoscale()
# axis.margins(0.1)


pl.grid(color='grey', linestyle=':', linewidth=0.15)
pl.tight_layout() #adjusts subplot params so that the subplot(s) fits in to the figure area.
# pl.plot([1], marker=".")
# pl.plot([1,2,3], marker=mc.markers.CARETDOWNBASE)
pl.show()

#####AQUI 1
