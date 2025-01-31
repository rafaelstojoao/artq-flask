# Este código é uma versão orientada a objetos do algoritmo de mineração de dados APRIORI
# Identifica padrões, gera candidatoes e constrói regras de associação

import numpy

class rule:
    def __init__(self):
        self.support    = 0.0
        self.confidence = 0.0
        self.lift       = 0.0
        self.X          = []
        self.Y          = []
        self.conviction = 0.0
        self.allItems   = []
        self.dataset    = []


    def printRule(self):
        print(self.X,'-->',self.Y,'sup: ',self.getSupport(),' conf:',self.getConfidence(), 'lift: ',self.lift, 'conviction: ',self.conviction)
        fpRules = open("dados/rules.rul","a+")
        fpRules.write(str(self.X)+'-->'+str(self.Y)+'sup: '+str(self.getSupport())+' conf:'+str(self.getConfidence())+ 'lift: '+str(self.lift)+ 'conviction: '+str(self.conviction)+"\n")

    def getConfidence(self):
        return self.confidence

    def getSupport(self):
        return self.support

    def setConfidence(self,conf):
        self.confidence = conf

    def setSupport(self,sup):
        self.support = sup



class itemset :
    def __init__(self):
        self.support    = 0.0
        self.counting   = 0
        self.items      = []

    def getitems(self):
        return self.items


    def setSupport(self,dataSetSize):
        self.suporte = self.counting / dataSetSize

    def getSupport(self):
        return self.suporte

    def getCounting(self):
        return self.counting

    def setCounting(self,count):
        self.counting = count

    def increaseCounting(self):
        self.counting =+ 1


class Apryori:

    def __init__(self):
        self.minSup     = 0.0
        self.minConf    = 0.0
        self.arq        = ""
        self.dataset    = []
        self.listadePadroes     = []
        self.listadeCandidatos  = []
        self.listRules          = []
        fpRules = open("dados/rules.rul","w+")
        self.fpPat = open("dados/padroes.patt","w+")

    def loadDataSetFromFile(self):
        import csv
        data =[]
        with open('dados/RelacoesTemporais.csv') as csvfile:
            data = list(csv.reader(csvfile))
            self.dataset = sorted(data)

        print(len(self.dataset))
        print(self.dataset)
        return self.dataset


    def loadDataSet(self):
       print('Dataset Loaded')
       return [['A','B','C'],
               ['A','B','C','D', 'E'],
               ['A','C','D'],
               ['A','C','D','E'],
               ['A','B','C','D']]
        # return [['leite','pão'],['pão','manteiga'],['cerveja'],['leite','pão','manteiga'],['pão']  ]

    def combinaItens(self,elem,listaCombinar):
        combinados =[]
        print('combinar')
        print(elem)
        print('com')
        print(listaCombinar)
        for item in listaCombinar:
            combinados.append([elem,item])
        return combinados


    def aprioriGen(self,i):
        if(i == 0):
            print('generating Cand1')
            itemsTam1 = []
            for transaction in self.dataset:
                for item in transaction:
                     if item not in itemsTam1 and item != '':
                        itemsTam1.append(item)
            itemsTam1.sort()
            listaCandidatostemp = []
            for item in itemsTam1: #é preciso transformar cada item em um candidato.
                if item != "":
                    cand  = itemset()
                    cand.items = [item]
                    listaCandidatostemp.append(cand)
            self.listadeCandidatos.append(listaCandidatostemp)

        elif len(self.listadePadroes[i - 1]) <= 1:
            print('Não se pode construir mais candidatos')
            self.listadeCandidatos.append([])
            return
        else:
            print('\n\n generating Cand_' + str(i + 1))

            listaPadroes =[]
            listaCandidatos = []
            for padrao in self.listadePadroes[i-1]:
                listaPadroes.append(padrao.items)

            for i in range(len(listaPadroes)):
                padrao = listaPadroes[i]
                resto = listaPadroes[i+1:]

                for itset in resto:
                    L1 = padrao[:-1]
                    L2 = itset[:-1]

                    if L1 == L2:
                        candidato = sorted(list(set(padrao) | set(itset)))
                        # if(len(candidato) >= 10):
                        #     print(candidato)
                        cand = itemset()
                        cand.items =candidato
                        listaCandidatos.append(cand)
            self.listadeCandidatos.append(listaCandidatos)
            return



    def validaCandidatos(self,i):
        print('Validando candidatos de tamanho: ' + str(i+1))
        print('minsup: '+str(self.minSup))
        # fp = open("./dados/padroes.patt", "a+")
        if i==0: # se são itens unitários para verificar
            for reg in self.dataset:
                for cand in self.listadeCandidatos[i]:
                    if set(cand.items).intersection(reg):
                         cand.counting += 1
            listaPadroes = []

            for cand in self.listadeCandidatos[i]:
                cand.suporte = cand.counting/self.tamanhoDataset
                print( cand.counting)
                print( cand.suporte )
                print( self.tamanhoDataset )
                if(cand.suporte >= self.minSup):
                    print('candidato validado')
                    print(str(cand))
                    listaPadroes.append(cand)
                    # fp.write(str(cand.items) + ' suporte: ' + str(cand.suporte) + "\n")
                    print(str(cand.items) + ' suporte: ' + str(cand.suporte) + "\n")

            return listaPadroes

        else:
            for reg in self.dataset:
                for cand in self.listadeCandidatos[i]:

                    if self.sublist(cand.items,reg):
                        cand.counting+=1

            listaPadroes = []
            for cand in self.listadeCandidatos[i]:
                cand.suporte = cand.counting / self.tamanhoDataset
                if (cand.suporte >= self.minSup):
                    listaPadroes.append(cand)
                    #fp.write(str(cand.items) + ' suporte: ' + str(cand.suporte) + "\n")
            return listaPadroes

    def sublist(self, lst1, lst2):
        condBool = True
        for elem in lst1:
            if elem not in lst2:
                condBool = False
        return condBool

    def geraRegra(self,itset):
        listaRegras = []
        tamItemset = len(itset.items)
        for i in range(0,tamItemset-1):
            R =rule()
            R.X = itset.items[:i+1]
            R.Y = itset.items[i+1:]
            listaRegras.append(R)
        return listaRegras



    def printRules(self):
        for rul in self.listRules:
            print(str(rul.X) + '--> ' + str(rul.Y))


    def estimateSupport(self,listitems):
        count =0
        for reg in self.dataset:
            if (set(listitems).intersection(reg) == set(listitems)):
                count += 1
        return count/self.tamanhoDataset

    def validateRule(self,ruleSetCandidate):
        listValidRules = []

        for rule in ruleSetCandidate:
            itemsRule = itemset()
            itemsRule.items = sorted(numpy.unique(rule.X + list(set(rule.Y) - set(rule.X))))
            rule.allItems = itemsRule
            rule.setSupport(self.estimateSupport(itemsRule.items))

            X = itemset()
            Y = itemset()

            X.items = rule.X
            Y.items = rule.Y

            X.support = self.estimateSupport(X.items)
            Y.support = self.estimateSupport(Y.items)

            #confidence measure:  sup(XUY)/sup(X)
            rule.setConfidence(round(rule.getSupport()/X.support,3))

            if rule.getConfidence() >= self.minConf:
                listValidRules.append(rule)

                # set lift
                try:
                    rule.lift = round(rule.getSupport() / (Y.support * X.support),3)
                except ZeroDivisionError:
                    rule.lift = 0.0

                try:
                    rule.conviction = round((1.0 - Y.support) / (1.0 - rule.confidence),3)
                except ZeroDivisionError:
                    rule.conviction = 0.0

        return listValidRules

    def generateRules(self):
        print('Generating rules')
        ciclos = len(self.listadePadroes)
        print(ciclos)
        for i in range(1,ciclos):
            regrasValidadas =[]
            padroes = self.listadePadroes[i]
            for itset in padroes:
                listaRegras = self.geraRegra(itset)
                regrasValidadas+=self.validateRule(listaRegras)
            self.listRules+= regrasValidadas



    def   apriori(self,dataset,minsup=None,minconf=None):
        self.dataset = dataset
        self.tamanhoDataset = len(self.dataset)
        self.minSup  = minsup
        self.minConf = minconf

        i = 0
        self.aprioriGen(0)
        print('candidatos de tamanho: '+str(i+1))
        # for itemsetCandidato in self.listadeCandidatos[0]:
        #      print(itemsetCandidato.items)


        while (self.listadeCandidatos[i]):
            self.listadePadroes.append(self.validaCandidatos(i))

            # print('padrões: ')
            # if(len(self.listadePadroes[i][1].items) >= 8):
            #     fp = open("padroes.patt","a+")

            for padrao in self.listadePadroes[i]:
                print(str(padrao.items)+' suporte: '+str(padrao.suporte))
                self.fpPat.write(str(padrao.items)+' suporte: '+str(padrao.suporte)+"\n")
            i += 1
            self.aprioriGen(i)
            # for cand in self.listadeCandidatos[i]:
            #     print(cand.items)

        self.generateRules()

        for regra in self.listRules:
            regra.printRule()
        self.fpPat.close()


# if __name__ == '__main__':
#     apr = Apryori()
#     # dataset = apr.loadDataSetFromFile()
#     dataset = apr.loadDataSet()
#
#     apr.apriori(dataset,0.025,0.8)
