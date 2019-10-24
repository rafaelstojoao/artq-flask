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
        self.contentList    = []
        self.qtdAtributos   = 0
        self.cabecalho      = []
        self.atribTemporal = -1

    def __del__(self):
        self.arrayAtributos = []
        self.content        = ""
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

    def readFileCsv(self,inputFile):
        self.content = ""
        decoded_file = inputFile.read().decode('utf-8').splitlines()
        header = decoded_file[0].split(',')
        self.setCcabecalho(header)
        self.setQtdAtributos()
        self.criaArrayDeAtributos(self.getQtdAtributos())
        lista_de_atributos = self.arrayAtributos.copy()
        conteudo = csv.reader(decoded_file)

        for row in conteudo:
            self.contentList.append(row)
            self.content += ', '.join(row)+'\n'
            for i in range(self.getQtdAtributos()):
                if (self.kindOfValue(row[i]) == 1):
                    lista_de_atributos[i].incluiValor(float(row[i]))  # ao incluir cada valor, as métricas são atualizadas.
                elif (self.kindOfValue(row[i]) == 2):
                    lista_de_atributos[i].incluiValor(float(int[i]))  # ao incluir cada valor, as métricas são atualizadas.
                elif (self.kindOfValue(row[i]) == 3):
                    lista_de_atributos[i].tipoValor = "Date"
                    self.atribTemporal = i
                elif (self.kindOfValue(row[i]) == 4):
                    lista_de_atributos[i].tipoValor = "String"
                else:
                    print('NaN')

        return self.content, lista_de_atributos
