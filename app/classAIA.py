from datetime import *
from random import randint
import numpy as np
import time

from app.classIntervalo import Intervalo





class Aia:

    def __init__(self,janelaRelacao):
        self.janela = janelaRelacao
        self.arrayPontosTemporaisTimestamp = []
        self.timestampIntervalo = Intervalo()
        self.arrayIntervalosOrdenados = []
        lifetime = [] #é a lista de todas as datas onde os intervalos temporais se inciam
        self.fpRelacoes = open("dados/RelacoesTemporais.csv", "a+")

    def constroiTimeStamp(self,arrayDeTempos): # analisa todos os tempos dos intervalos e unifica em um lifetime
        self.arrayPontosTemporaisTimestamp = arrayDeTempos
        np.unique(self.arrayPontosTemporaisTimestamp).tolist() # numpy.unique remove os elementos duplicados (ja ordena tb)
        self.timestampIntervalo.t_i = arrayDeTempos[0]
        self.timestampIntervalo.t_f = arrayDeTempos[len(arrayDeTempos)-1]

    def listaRelacoesPossiveis(self):
        print("starts, overlaps, meets, before, finishes, equal, during")

    def geraUmaDataAleatoria(self,dataSeed = date.today(),range = 900):
        novaData = date.fromordinal(dataSeed.toordinal() + randint(-range, range))  # hoje + 45 dias</pre>
        return novaData

    def identificaRelacao(self,i1,i2):
        rel =""
        if  (   i1.t_i == i2.t_i
            and i1.t_f == i2.t_f   ):
            rel = "EQUAL"
            print("equal(1,2)")

        elif(   i1.t_i == i2.t_i
            and i1.t_f < i2.t_f    ):
            rel = "STARTS"
            print("starts(1,2)")

        elif(   i1.t_f == i2.t_f
            and i1.t_i > i2.t_i    ):
            rel = "FINISHES"
            print("finishes(1,2)")

        elif(   i1.t_f == i2.t_i   ):
            rel = "MEETS"
            print("meets(1,2)")

        elif(   i1.t_f <  i2.t_i   ):
            rel = "BEFORE"
            print("before(1,2)")

        elif(   i1.t_i < i2.t_i
            and i1.t_f >  i2.t_i
            and i1.t_f <  i2.t_f   ):
            rel = "OVERLAPS"
            print("overlaps(1,2)")

        elif(   i1.t_i > i2.t_i
            and i1.t_f < i2.t_f    ):
            rel = "DURING"
            print("during(1,2)")

        else:
            rel = "NONE"
            print("No relation for you!")
        # fpRelacoes.write(str(rel)+"("+str(int1.atributoTag)+","+str(int2.atributoTag)+")")

        if  (rel != "NONE"):
            if(i1.atributoTag == i2.atributoTag and rel == "EQUAL"):
                return
            else:
                self.fpRelacoes.write(str(rel)+"("+str(i1.atributoTag)+";"+i2.atributoTag+"),")

        return rel



    def executaAIA(self):
        i1 = Intervalo()
        i2 = Intervalo()



        for int in self.arrayIntervalosOrdenados:#para cada um dos intervalos
            # self.fpRelacoes.write("\n Data selecionada -------"+str(date.fromordinal(int[0])))
           # self.fpRelacoes.write("\n")
            print("Data selecionada",date.fromordinal(int[0]))
            i1.t_i = date.fromordinal(int[0])
            i1.t_f = date.fromordinal(int[1])
            i1.atributoTag = int[2]
            #procurar todos os intervalos que se iniciem em até 1 janela após ele.
            selecao = [elem for elem in self.arrayIntervalosOrdenados if (elem[0] >= int[0] and (elem[0]-self.janela) <= int[0]) ]
            for s in selecao:
                # fpRelacoes.write("("+str(date.fromordinal(int[0]))+", ")
                print(date.fromordinal(s[0]))
                i2.t_i = date.fromordinal(s[0])
                i2.t_f = date.fromordinal(s[1])
                i2.atributoTag = s[2]
                self.identificaRelacao(i1,i2)

            self.fpRelacoes.write("\n")
        self.fpRelacoes.close()


    def date(datestr="", format="%Y-%m-%d"):
        from datetime import datetime
        if not datestr:
            return datetime.today().date()
        return datetime.strptime(datestr, format).date()



    def ordenaIntervalos(self,arrayIntervalos):
        tempIntevarlosOrdenados = []
        tags = []
        for inter in arrayIntervalos:
            ti = inter.t_i.toordinal()
            tf = inter.t_f.toordinal()
            ttag = inter.atributoTag
            tempIntevarlosOrdenados.append([ti,tf,ttag])

        # a função sorted permite ordenar um array multidimensional por uma coluna deterinada
        self.arrayIntervalosOrdenados = sorted(tempIntevarlosOrdenados, key=lambda x: x[0]) #lambda é uma função anônima inline que retorna x[0]

        for i in range(len(self.arrayIntervalosOrdenados)):
            print(date.fromordinal(self.arrayIntervalosOrdenados[i][0]),date.fromordinal(self.arrayIntervalosOrdenados[i][1]))

    #a partir de aqui é preciso verificar se não se trata do mesmo intervalo (muitos equals) e tb conferir qual a relação da AIA presente

#
# start = time.time()
# aia = Aia(1145)
# # aia.listaRelacoesPossiveis()
#
#
#
# arrayIntervalos = []
#
# for i in range(10):
#     i1 = Intervalo()
#     dtRand = aia.geraUmaDataAleatoria()
#     dtRand2 = aia.geraUmaDataAleatoria(dtRand,79)
#
#     if(dtRand < dtRand2):
#         i1.t_i = dtRand
#         i1.t_f = dtRand2
#
#     else:
#         i1.t_i = dtRand2
#         i1.t_f = dtRand
#
#     arrayIntervalos.append(i1)
#
#
#
# aia.ordenaIntervalos(arrayIntervalos)
# aia.executaAIA()

#
#
#
#
#
#
# oldIntervalo = arrayIntervalos[0]
# for int in arrayIntervalos:
#     aia.identificaRelacao(oldIntervalo,int)
#     oldIntervalo = int
#
#
# print("Tempo total de execução: %.3f segundos " %(time.time() - start))
# #for i in range(190):
# #    arrayDatas.append(aia.geraUmaDataAleatoria())
#
#
# #aia.constroiTimeStamp(arrayDatas)
# #aia.executaAIA()
#
#
# #RAfael Stoffalette JOão
