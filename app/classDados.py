# encoding: utf-8

from datetime import *
from os.path import join

from app.classAtributo import Atributo
import csv
import pprint

class Dados:
    def __init__(self):
        self.arrayAtributos = []
        self.content        = ""
        self.formatedContent        = ""
        self.contentList    = []
        self.qtdAtributos   = 0
        self.cabecalho      = []
        self.atribTemporal = -1

    def __del__(self):
        self.arrayAtributos = []
        self.content        = ""
        self.formatedContent        = ""
        self.contentList    = []
        self.qtdAtributos   = 0
        self.cabecalho      = []
        self.atribTemporal = -1






##### AQUI é  O LIMITE

    def criaArrayDeAtributos(self,tam):
        for i in range(tam):
            # print(i)
            d = Atributo()
            self.arrayAtributos.append(d)

    def getCabecalho(self):
        return self.cabecalho

    def getQtdAtributos(self):
        return len(self.cabecalho)

    def setQtdAtributos(self):
        self.qtdAtributos = len(self.cabecalho)

    def setCcabecalho(self,header):
        self.cabecalho = list(header)


    def kindOfValue(self,val):
        if      (self.tryReal ( val)): return 1 #se valor quantitativo contínuo
        elif    (self.tryInt  ( val)): return 2 # se valor inteiro
        elif    (self.tryDate ( val)): return 3 # se data
        elif    (self.tryStr  ( val)): return 4 # se string
        else: return 0

    def tryInt(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def tryStr(self, s):
        try:
            str(s)
            return True
        except ValueError:
            return False

    def tryReal(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False


    def tryDate(self, datestr="", format="%d-%m-%Y"):
        from datetime import datetime
        try:
            datetmp = datestr.replace('/','-')
            d = datetime.strptime(datetmp, "%d-%m-%Y")
            return True
        except ValueError:
            return False

    def convertToDate(self,datestr):
        from datetime import datetime
        try:
            datetmp = datestr.replace('/', '-')
            d = datetime.strptime(datetmp, "%d-%m-%Y")
            return d
        except ValueError:
            return False

    def readFileCsv(self,inputFile):
        self.content = ""

        decoded_file = inputFile.read().decode('utf-8').splitlines()
        header = decoded_file[0].split(',')
        self.setCcabecalho(header)
        self.setQtdAtributos()
        self.criaArrayDeAtributos(self.getQtdAtributos())
        lista_de_atributos = self.arrayAtributos.copy()
        conteudo = csv.reader(decoded_file)
        iteracao = 1


        for row in conteudo:

            self.contentList.append(row)
            self.content += ', '.join(row)+'\n'

            if iteracao <= 2:
                iteracao+=1
                row1 = row


            for i in range(self.getQtdAtributos()):
                if (self.kindOfValue(row[i]) == 1):
                    lista_de_atributos[i].incluiValor(float(row[i]))  # ao incluir cada valor, as métricas são atualizadas.
                    lista_de_atributos[i].tipoValor = "Numeric"
                elif (self.kindOfValue(row[i]) == 2):
                    lista_de_atributos[i].incluiValor(float(int[i]))  # ao incluir cada valor, as métricas são atualizadas.
                    lista_de_atributos[i].tipoValor = "Numeric"
                elif (self.kindOfValue(row[i]) == 3):
                    lista_de_atributos[i].tipoValor = "Date"
                    self.atribTemporal = i
                elif (self.kindOfValue(row[i]) == 4):
                    lista_de_atributos[i].tipoValor = "String"
                else:
                    print('NaN')

                if (self.atribTemporal == -1):
                    self.insertTemporality(i)




        self.generateMetaData(i,lista_de_atributos)
        self.formatedContent = self.content.replace('\n', '<br/>').split('<br/>')
        return self.content, lista_de_atributos


    def insertTemporality(self,i):
        i += 1

        self.atribTemporal = i
        first = True
        for linha in self.contentList:
            if first:
                linha.insert(0, 'Date')
                first = False
            else:
                linha.insert(0, '2009/01/01')



    def generateMetaData(self,i,lista_de_atributos):
        f = open("dados/metaData.txt", "w+")

        f.write(' TEMPORAL FEATURE:' + str(self.atribTemporal) + '\n\n')

        f.write('atributos: ' + str(self.getCabecalho()) + '\n')
        for att in self.arrayAtributos:
            f.write(' -  count: ' + str(att.qtdValores) + ' - ')
            f.write(' sum: ' + str(att.getSomatorio()) + ' - ') if att.getQtdValores() > 1 else None
            f.write(' mean: ' + str(att.getMedia()) + ' - ') if att.getQtdValores() > 1 else None
            f.write(' stdD: ' + str(att.getDesvioPadrao()) + ' - ') if att.getQtdValores() > 1 else None
            f.write(' - ' + str(att.tipoValor) + ' ')
            f.write('\n')

        f.write('\n\n Dataset:\n')
        for linha in self.contentList:
            f.write(str(linha) + '\n')