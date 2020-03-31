import datetime

import numpy as np
from matplotlib.figure import Figure
from numpy import random
import pylab as pl
from matplotlib import collections  as mc
from matplotlib.dates import DateFormatter

from app.classIntervalo import *


class Plot:
    def __init__(self):
        self.arrDatas = []
        self.labelsX = []
        self.labelsY = []
        self.lines  =[]
        self.colorLine = []
        self.datasAleatorias = []



    def geraDataAleatoria(self,num):
        for i in range(num):
            self.datasAleatorias.append(Intervalo.geraUmaDataAleatoria(None))

    def setLabelX(self):
        self.labelsX = self.datasAleatorias

    def setLabelY(self,listaLabels):
        self.labelsY = listaLabels
        # self.labelsY = ["Temperature", "Wind speed", "Humidity", "Rain", "Floor", "x", "k"]

    def setLines(self):
        self.lines =  [
                    [(0, 0), (1, 0)],
                    [(2, 1), (5, 1)],
                    [(2, 3), (3, 3)],
                    [(4, 3), (5, 3)],
                    [(5, 8), (15, 8)],
                    [(1, 2), (3, 2)]
        ]

    def setColorLine(self):
        for i in range(len(self.lines) + 1):
            self.colorLine.append((random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), 1))

    def includeSegment(self, xi,yi,xf,yf):
        self.lines.append([(xi,yi),(xf,yf)])


    def plotaWindow(self):

        lc = mc.LineCollection(self.lines,  linewidths=3)
        fig, axis = pl.subplots()
        pl.yticks(np.arange(len(self.labelsY)), self.labelsY)
        pl.xticks(np.arange(len(self.labelsX)), self.labelsX, rotation=90)
        axis.add_collection(lc)
        axis.autoscale()

        pl.grid(color='grey', linestyle=':', linewidth=0.15)
        pl.tight_layout()  # adjusts subplot params so that the subplot(s) fits in to the figure area.
        # pl.show()

    def plotaIntervalosWeb(self, lista_de_atributos,cabecalho):
        minX = 1000000000.0
        maxX = 0.0
        listaLegendasX = []
        for i in range(len(lista_de_atributos)):
            for intervalo in lista_de_atributos[i].listaDeIntervalosDeInteresse:
                ti = intervalo.t_i.toordinal()
                tf = intervalo.t_f.toordinal()

                minX = min(minX, ti)
                maxX = max(maxX, tf)
                self.includeSegment(ti, i, tf, i)
        self.setLabelY(cabecalho)
        print(self.lines)
        colors = ['r', 'g', 'b']
        fig = Figure()
        lc = mc.LineCollection(self.lines,colors=['r', 'g', 'b'], linewidths=3)
        labelsX = self.datasAleatorias
        fig, axis = pl.subplots()
        pl.yticks(np.arange(len(self.labelsY)), self.labelsY)

        arr = np.arange(minX,maxX,(maxX-minX)/10)
        for e in arr:
            listaLegendasX.append(date.fromordinal(int(e)))

        pl.xticks(np.arange(minX,maxX,(maxX-minX)/10), listaLegendasX, rotation=90)

        axis.add_collection(lc)
        axis.autoscale()
        axis.set_xlim(minX-5, maxX+10)

        x = [i[0] for j in self.lines for i in j]
        y = [i[1] for j in self.lines for i in j]
        axis.scatter(x, y, marker="|")


        pl.grid(color='grey', linestyle=':', linewidth=0.15)
        pl.tight_layout()  # adjusts subplot params so that the subplot(s) fits in to the figure area.
        fig.autofmt_xdate()
        return fig