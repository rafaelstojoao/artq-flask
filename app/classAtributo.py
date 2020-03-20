#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt
from app.classIntervalo import *
# from intervalo import *
from app.classPlot import Plot
class Atributo:
    def __init__(self):
        self.arrayDeValores = []
        self.qtdValores     = 0
        self.somaTorio      = 0.0
        self.variancia      = 0.0
        self.media          = 0.0
        self.desvioPadrao   = 0.0
        self.listaTransacoesInteresse = []
        self.listaDePontosTemporaisDeInteresse = []
        self.listaDeIntervalosDeInteresse = []
        self.tipoValor = ""
        self.atributoTemporal = -1

    def getTipo(self):
        return self.tipoValor

    def showMe(self):
        print('\n-------------------------------------\n')
        print('\n Type:'    + self.getTipo())
        print('\n Sum:'     + str(self.getSomatorio()))
        print('\n var:'     + str(self.getVariancia()))
        print('\n mean:'    + str(self.getMedia()))
        print('\n std:'     + str(self.getDesvioPadrao()))
        print('\n qtd:'     + str(self.getQtdValores()))
        #print('\n vals:'    + str(self.getArraydeValores()))


    def criaArrayDeAtributos(tam, arrayAtt):
        for i in range(tam):
            d = Atributo()
            arrayAtt.append(d)

    def incluiValor(self,valor):

        self.arrayDeValores.append(valor)
        self.setQtdValores(self.getQtdValores() + 1)
        self.setSomatorio(self.getSomatorio() + valor)
        self.setMedia()
        self.setVariancia()
        self.setDesvioPadrao()



    def setSomatorio(self,sum):
            self.somaTorio = sum
            return

    def getSomatorio(self):
        return round(self.somaTorio,3)

    def setQtdValores(self,qtd):
        self.qtdValores = qtd
        return

    def getQtdValores(self):
        return self.qtdValores

    def getArraydeValores(self):
        for i in range(len(self.arrayDeValores)):
            print(self.arrayDeValores[i])


    def setMedia(self):
        if self.qtdValores >=1:
            self.media = self.somaTorio / self.qtdValores
        else:
            self.media= 0.0

    def getMedia(self):

        return round(self.media,3)

    def setVariancia(self):
        somaQuadrada = 0.0
        for elem in self.arrayDeValores:
            somaQuadrada += abs(elem - self.getMedia()) ** 2
        self.variancia = somaQuadrada / (self.getQtdValores())


    def getVariancia(self):
        self.setVariancia()
        return self.variancia

    def setDesvioPadrao(self):
        if self.qtdValores >= 1:
            self.desvioPadrao = sqrt(self.getVariancia())
        else:
            self.desvioPadrao = 0.0

    def getDesvioPadrao(self):
        return round(self.desvioPadrao,3)


    def listaIntervalos(self):
        print('Atributo tem:%s intervalos' % len(self.listaDeIntervalosDeInteresse))

        for inter in self.listaDeIntervalosDeInteresse:
            print("intervalo[%s,%s] contendo %s pontos"%(inter.t_i, inter.t_f, len(inter.listaDePontosTemporais)))

        return




    def setIntervals(self,janela):
        self.listaDeIntervalosDeInteresse = []
        # for ponto in self.listaDePontosTemporaisDeInteresse:
        # self.listaDeIntervalosDeInteresse = Intervalo.setIntervals(janela, self.listaDePontosTemporaisDeInteresse)




    def setIntervals2(self, janela):
        self.listaDeIntervalosDeInteresse = []

        print('atributo.setIntervalos chamado')
        arrayIntervalos = []

        for ponto in self.listaDePontosTemporaisDeInteresse:
            print('POnto temporal: ' + str(ponto))

            if (len(arrayIntervalos) == 0):
                # # inter = Intervalo()
                # inter.t_f = inter.t_i = ponto
                # inter.listaDePontosTemporais.append(ponto)
                # arrayIntervalos.append(inter)
                print('aqui')

            else:
                inseriu = False

                for intervalo in arrayIntervalos:  # para cada intervalo de interesse no array de intervalos do atributo
                    print('if ('+ str(intervalo.t_i)+ ' <= '+ str(ponto)+ ' and ponto <= ' +str(intervalo.t_f)+'):')
                    if (intervalo.t_i <= ponto and ponto <= intervalo.t_f):
                        intervalo.listaDePontosTemporais.append(ponto)

                    else:
                        diferenca = abs(intervalo.t_i - ponto)

                        if (diferenca.days < janela and intervalo.t_i > ponto):  # temos um novo ponto de inicio
                            intervalo.t_i = ponto
                            intervalo.listaDePontosTemporais.append(ponto)
                            inseriu = True
                            break

                        else:
                            diferenca = abs(intervalo.t_f - ponto)

                            if (diferenca.days < janela and intervalo.t_f < ponto):  # temos um novo ponto de termino
                                intervalo.t_f = ponto
                                intervalo.listaDePontosTemporais.append(ponto)
                                inseriu = True
                                break
                if (inseriu):
                    inseriu = False

                else:
                    print('aqui2')
                    # inter = Intervalo()
                    # inter.t_f = inter.t_i = ponto
                    # inter.listaDePontosTemporais.append(ponto)
                  # arrayIntervalos.append(inter)

        self.listaDeIntervalosDeInteresse = arrayIntervalos
        return

