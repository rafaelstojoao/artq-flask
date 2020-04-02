#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.classIntervalo import *
from app.classDados import *
import numpy as np

def listaMedias(dados,lista_de_atributos):
    ret = """
        <table class='striped' >
        <tr>
        """
    for item in dados.getCabecalho():
        ret += "<td  ><b>"+str(item)+"</b> <br/></td>"

    ret += "</tr><tr >"
    indiceAtributo = -1
    for item in lista_de_atributos:
        indiceAtributo+=1
        if item.tipoValor == "Date":
            ret += "<td  >Date value</td>"
        #select = request.form.get('select-att')

        elif item.tipoValor == "Numeric":
            # item.showMe() #método que mostra todos os valores de um atributo
            ret += "<td><ul>" \
                   "<li>average: <b>"+str(item.getMedia())+ "</b></li> " \
                                                            "<li>std. deviation:<b>"+str(item.getDesvioPadrao())+"</b></li>" \
                    "<li><select class='input-field' name='select-att"+str(indiceAtributo)+"'>" \
                    "<option selected='selected' value='btw'> between std dev</option>" \
                    "<option value='blw'> below std dev</option>" \
                    "<option value='out'> out of std dev</option>" \
                    "<option value='abv'> above  std dev</option>" \
                    "</select></li>"\
                    "</ul></td>"
        elif item.tipoValor == "String":
            ret += "<td  >String value - ignored</td>"
        else:
            ret+="<td  ></td>"
    ret += """
        </tr>
        </table> <br />"""
    return ret




def buscaPontosdeInteresse(numDesvios,dados,arrayAtributos,arraySETUP_POIS):
    print('carregaDadosBD(buscaPontosdeInteresse)')


    for i in range(len(arrayAtributos)):
        arrayAtributos[i].listaTransacoesInteresse = []
        arrayAtributos[i].listaDeIntervalosDeInteresse = []
        if (arrayAtributos[i].qtdValores > 1):
            fp = open("dados/att_" + str(i) + "_POIs.pois", "w+")
            media = float(arrayAtributos[i].getMedia())
            desvPadrao = arrayAtributos[i].getDesvioPadrao()

            fp.write("\nMédia: "+str(media))
            fp.write("\nDesvio Padrão: "+str(desvPadrao))
            fp.write("\n"+str(arraySETUP_POIS[i]))
            fp.close()

    contalinhas =1

    for linha in dados.contentList[1:]:
        index = 0

        for i in linha:
            if (arrayAtributos[index].qtdValores > 1):
                fp = open("dados/att_"+str(index)+"_POIs.pois","w+")


                media = float(arrayAtributos[index].getMedia())
                desvPadrao = arrayAtributos[index].getDesvioPadrao()
                valorInicio = float(media)-float(numDesvios*desvPadrao)
                valorFim = float(media)+float(numDesvios*desvPadrao)

                # fp.write("\nMédia: "+str(media))
                # fp.write("\nDesvio Padrão: "+str(desvPadrao))
                #print(arraySETUP_POIS[index])

                valor = linha[index]
                # if (dados.tryReal(valor) == False):
                #     print('valor não numérico')

                # else:
                if(arraySETUP_POIS[index] == 'btw'):
                    if(valorInicio <= float(linha[index]) <= valorFim): # se o valor esta entre os desvios padrão [-,+]
                        arrayAtributos[index].listaTransacoesInteresse.append(contalinhas)
                        fp.write("\n" +str(contalinhas)+" [ "+str(linha[index])+" ] :"+str(linha))
                        if linha[dados.atribTemporal] not in arrayAtributos[index].listaDePontosTemporaisDeInteresse:
                            arrayAtributos[index].listaDePontosTemporaisDeInteresse.append(linha[dados.atribTemporal])

                elif (arraySETUP_POIS[index] == 'blw'):
                    if(valorInicio > float(linha[index])): # se o valor esta entre os desvios padrão [-,+]
                        arrayAtributos[index].listaTransacoesInteresse.append(contalinhas)
                        fp.write("\n" + str(contalinhas) + " [ " + str(linha[index]) + " ] :" + str(linha))
                        if linha[dados.atribTemporal] not in arrayAtributos[index].listaDePontosTemporaisDeInteresse:
                            arrayAtributos[index].listaDePontosTemporaisDeInteresse.append(linha[dados.atribTemporal])

                elif (arraySETUP_POIS[index] == 'abv'):
                    if(valorFim < float(linha[index])): # se o valor esta entre os desvios padrão [-,+]
                        arrayAtributos[index].listaTransacoesInteresse.append(contalinhas)
                        fp.write("\n" +str(contalinhas)+" [ "+str(linha[index])+" ] :"+str(linha))
                        if linha[dados.atribTemporal] not in arrayAtributos[index].listaDePontosTemporaisDeInteresse:
                            arrayAtributos[index].listaDePontosTemporaisDeInteresse.append(linha[dados.atribTemporal])

                elif (arraySETUP_POIS[index] == 'out'):
                    if(valorFim < float(linha[index]) or float(linha[index]) < valorInicio): # se o valor esta entre os desvios padrão [-,+]
                        arrayAtributos[index].listaTransacoesInteresse.append(contalinhas)
                        fp.write("\n" +str(contalinhas)+" [ "+str(linha[index])+" ] :"+str(linha))
                        if linha[dados.atribTemporal] not in arrayAtributos[index].listaDePontosTemporaisDeInteresse:
                            arrayAtributos[index].listaDePontosTemporaisDeInteresse.append(linha[dados.atribTemporal])
                fp.close()
            index += 1

        contalinhas += 1

    return



def listaPois(dados,lista_de_atributos,arr_setup_pois):
    cont = ""
    poi = open('pois.txt','w+')
    for at in range(len(lista_de_atributos)):
      if dados.cabecalho[at] != 'Data':
        cont += "<div class='poisDiv'><ul>" \
                "<li><h5>Attribute: "+ dados.cabecalho[at]+"</h5></li>" \
                                                       "<li> Setup: "
        poi.write(str(cont))
        if(arr_setup_pois[at] == 'btw'):
            cont += " Between starndard deviation</li>"
        elif (arr_setup_pois[at] == 'blw'):
            cont += " Below starndard deviation</li>"
        elif (arr_setup_pois[at] == 'abv'):
            cont += " Above starndard deviation</li>"
        elif (arr_setup_pois[at] == 'out'):
            cont += " Out of starndard deviation</li>"

        cont+="<br/>"

        print(len(lista_de_atributos[at].listaTransacoesInteresse))
        try:
            for i in range(len(lista_de_atributos[at].listaTransacoesInteresse)):
                poi.write("<li>["+str(lista_de_atributos[at].listaTransacoesInteresse[i])+", "+str(lista_de_atributos[at].listaDePontosTemporaisDeInteresse[i])+"]</li>")
                cont += "<li> "+str(lista_de_atributos[at].listaTransacoesInteresse[i])+"   -   "+str(lista_de_atributos[at].listaDePontosTemporaisDeInteresse[i])+"</li>"
        except:
            print('not accessible')

        cont += "</ul></div>"


    return cont

def geraIntervalos(lista_de_atributos, janela):
    i = 0
    d = Dados()
    for at in lista_de_atributos:
        if at.qtdValores >1:
            arrayIntervalos = []

            for pontoTemporal in at.listaDePontosTemporaisDeInteresse:
                ponto = d.convertToDate(pontoTemporal)

                if (len(arrayIntervalos) == 0):
                    inter = Intervalo()
                    inter.t_f = inter.t_i = ponto
                    inter.atributoTag = "att_" + str(i + 1)
                    inter.listaDePontosTemporais.append(ponto)
                    arrayIntervalos.append(inter)

                else:
                    inseriu = False

                    for intervalo in arrayIntervalos:  # para cada intervalo de interesse no array de intervalos do atributo
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
                        inter = Intervalo()
                        inter.t_f = inter.t_i = ponto
                        inter.listaDePontosTemporais.append(ponto)
                        inter.atributoTag = "att_"+str(i+1)
                        arrayIntervalos.append(inter)
            i+=1
            at.listaDeIntervalosDeInteresse = sorted(arrayIntervalos, key=lambda x: x.t_i)
            fpintevalos = open("dados/att_" + str(i) + "_INTERVALOS_interesse.int", "w+")

            for int in at.listaDeIntervalosDeInteresse:
                fpintevalos.write(str(int.atributoTag)+","+str((int.t_i).strftime('%Y/%m/%d'))+","+str((int.t_f).strftime('%Y/%m/%d'))+"\n")
                #fpintevalos.write(str((int.t_i).strftime('%Y/%m/%d')) + "," + str((int.t_f).strftime('%Y/%m/%d')) + "\n")
            fpintevalos.close()

    return



def listarIntervalosTemporais(lista_de_atributos,dados):
    html = ""
    for i in range(len(lista_de_atributos)):
        html += "<div class='intervaloDiv'><h1>Atributo: "+str(dados.cabecalho[i])+"</h1><ul>"
        for interval in lista_de_atributos[i].listaDeIntervalosDeInteresse:
            html += "<li>"+str((interval.t_i).strftime('%d/%m/%Y'))+","+str((interval.t_f).strftime('%d/%m/%Y'))+"</li>"
        html += "</ul></div>"

    return  html


def geraAIA(lista_de_atributos,janela):
    from app.classAIA import Aia
    aia = Aia(janela)
    # aia = Aia(15)
    todosIntervalos = []

    for i in range(len(lista_de_atributos)):
        if lista_de_atributos[i].listaDeIntervalosDeInteresse:
            for int in lista_de_atributos[i].listaDeIntervalosDeInteresse:
                todosIntervalos.append(int)  # aqui está uma lista com TODOS os intervalos e suas tags identificadoras
            # fpintevalos = open("dados/att_" + str(i) + "_INTERVALOS_interesse.int", "r")

    aia.ordenaIntervalos(todosIntervalos)
    aia.executaAIA()
    import csv



    inputFile = "dados/RelacoesTemporais.csv"
    with open(inputFile) as decoded_file:
        linhas = csv.reader(decoded_file)

        conteudo = ""
        for row in linhas:
            if row != " ":
                conteudo += ', '.join(row) + '<br/>'

    return conteudo


def listaPadroes():
    import csv
    inputFile = "dados/padroes.patt"
    with open(inputFile,'w+') as decoded_file:
        linhas = csv.reader(decoded_file)

        conteudo = ""
        for row in linhas:
            if row != " ":
                conteudo += ' '.join(row) + '<br/>'

    return conteudo

def listaRegras():

    import csv
    inputFile = "dados/rules.rul"
    with open(inputFile) as decoded_file:
        linhas = csv.reader(decoded_file)

        conteudo = ""
        for row in linhas:
            if row != " ":
                conteudo += str(row) + '<br/>'

    return conteudo

# def geraAIA2(lista_de_atributos):
#     import time
#     from app.classAIA import Aia
#
#     start = time.time()
#     aia = Aia(1145)
#     # aia.listaRelacoesPossiveis()
#
#
#     matrizIntervalos = []
#     html = ""
#
#     for i in range(len(lista_de_atributos)):
#         if lista_de_atributos[i].listaDeIntervalosDeInteresse:
#             arrayIntervalos = aia.ordenaIntervalos(lista_de_atributos[i].listaDeIntervalosDeInteresse)
#             matrizIntervalos.append(arrayIntervalos)
#
#     for i in range(len(lista_de_atributos)):
#         arrayIntervalos = matrizIntervalos[i] #pega todos os  intervalos do atributo na posicao i
#         restoIntervalos = np.arange(len(matrizIntervalos))!=i # pega todos os intervalos dos outros atributos
#
#         for interResto in restoIntervalos:
#             rel = aia.identificaRelacao(arrayIntervalos,interResto)
#             print(rel)
#
#         html += "<div class='intervaloDiv'>" \
#                 "<h1>Atributo "+str(i)+"</h1>"\
#                 "<ul>"




    print("Tempo total de execução: %.3f segundos " % (time.time() - start))
    return html