#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date
from random import randint

class Intervalo:
    def __init__(self):
        self.t_i = ""
        self.t_f = ""
        self.listaDePontosTemporaisAleatorios = []
        self.listaDePontosTemporais = []
        self.listaDeIntervalos = []
        self.hj = date.today()
        self.arrayIntervalosOrdenados = []
        self.atributoTag = ""


    def incluiPonto(self,ponto):
        if(self.t_i > ponto):
            self.t_i = ponto
        elif(self.t_f < ponto):
            self.t_f = ponto
        self.listaDePontosTemporais.append(ponto)


    def get_inicio(self):
        return self.t_i


    def get_Fim(self):
        return self.t_f


    def get_ListadePontosTemporais(self):
        return self.listaDePontosTemporais






    # a partir de aqui é preciso verificar se não se trata do mesmo intervalo (muitos equals) e tb conferir qual a relação da AIA presente




    def imprimeIntervalos(self):
        print("\n Intervalo: ", self.t_i, self.t_f)
        print('Tamanho do intervalo'+ str(len(self.listaDePontosTemporais)))

        for i in range(len(self.listaDePontosTemporais)):
            print(self.listaDePontosTemporais[i])



    def constroiIntervalos(self,janelaParaIntervalo):

      for ponto in self.listaDePontosTemporaisAleatorios:
        if (len(self.listaDeIntervalos) == 0):
            inter = Intervalo()
            inter.t_f = inter.t_i = ponto
            inter.listaDePontosTemporais.append(ponto)
            self.listaDeIntervalos.append(inter)

        else:

            inseriu = False

            for intervalo in self.listaDeIntervalos:  # para cada intervalo de interesse no array de intervalos do atributo

                if (intervalo.t_i <= ponto and ponto <= intervalo.t_f):
                    intervalo.listaDePontosTemporais.append(ponto)

                else:

                    diferenca = abs(intervalo.t_i - ponto)

                    if (
                            diferenca.days < janelaParaIntervalo and intervalo.t_i > ponto):  # temos um novo ponto de inicio
                        intervalo.t_i = ponto
                        intervalo.listaDePontosTemporais.append(ponto)
                        inseriu = True
                        break

                    else:
                        diferenca = abs(intervalo.t_f - ponto)

                        if (
                                diferenca.days < janelaParaIntervalo and intervalo.t_f < ponto):  # temos um novo ponto de termino
                            intervalo.t_f = ponto
                            intervalo.listaDePontosTemporais.append(ponto)
                            inseriu = True
                            break
            if (inseriu):
                inseriu = False

            else:
                inter = Intervalo()
                inter.t_f = inter.t_i = ponto
                inter.listaDePontosTemporais.append(ponto)
                self.listaDeIntervalos.append(inter)




    def geraUmaDataAleatoria(self):
        hj = date.today()
        novaData = date.fromordinal(hj.toordinal() + randint(-900, 900))  # hoje + 45 dias</pre>
        return novaData