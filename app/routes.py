from flask import render_template, request, make_response
from app import app, functions
from app.apriori import Apryori
from app.classDados import Dados
dados = Dados()
lista_de_atributos = []

janela_para_intervalo = 1460
janela_para_relacoes = 1460
minsup = 0.1
minconf = 80



@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Rafael'}
    return render_template('index.html', arquivo='Home', user=user)


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/apriori')
def apriori():
    apr = Apryori()
    dataset = apr.loadDataSetFromFile()
    apr.apriori(dataset,minsup,minconf)

    pat = functions.listaPadroes()
    reg = functions.listaRegras()
    return render_template('apriori.html', padroes=pat, regras=reg)



@app.route('/artqconfig', methods=['GET', 'POST'])
def artqconfig():
    global minconf
    global minsup
    global janela_para_relacoes
    global janela_para_intervalo

    if request.method == 'POST':

        req = request.form
        minsup = float(req.get("inpminsup"))
        minconf = float(req.get('inpminconf'))
        janela_para_relacoes = int(req.get('inprelwind'))
        janela_para_intervalo = int(req.get('inpintwind'))
        return render_template('artq.html', configOk=True, pms = minsup, pmc = minconf, prw = janela_para_relacoes, piw = janela_para_intervalo)


@app.route('/artq', methods=['GET', 'POST'])
def artq():
    global lista_de_atributos
    global dados
    if request.method == 'POST':
        lista_de_atributos = []
        del dados
        dados = Dados()
        arqDB = request.files['databaseForm']
        nomeArQ = request.files['databaseForm'].filename

        if nomeArQ.endswith('.csv'):
            conteudo, lista_de_atributos = dados.readFileCsv(arqDB)
            medias = functions.listaMedias(dados, lista_de_atributos)
            print(len(lista_de_atributos))
            return render_template('artq.html', conteudoArq=dados.content, medias=medias)

        else:
            conteudo = 'Arquivo inserido deve ser do tipo ".CSV"'
            return render_template('artq.html', conteudoArq=conteudo)

    elif dados.content != "":
        medias = functions.listaMedias(dados, lista_de_atributos)
        return render_template('artq.html', conteudoArq=dados.content, medias=medias)

    else:
        return render_template('artq.html')



@app.route("/intervalosInteresse.png")
def simple():
    from io import BytesIO
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from app.classPlot import Plot

    p = Plot()
    fig = p.plotaIntervalosWeb(lista_de_atributos,dados.cabecalho)
    canvas=FigureCanvas(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response



@app.route('/imprimirIntervalos')
def impIntervalos():
    global dados
    global lista_de_atributos
    inter = functions.listarIntervalosTemporais(lista_de_atributos,dados)
    arq = open("intervalos.txt","w")
    arq.write(inter)
    #print(inter)
    arq.close()
    return render_template('listaIntervalos.html', intervalos = inter)


@app.route('/poi', methods=['GET', 'POST'])
#@app.route('/poi')
def poi():
    global dados
    global lista_de_atributos
    arr_setup_pois = []

    for contadorAtributos in range(len(lista_de_atributos)):
        select = request.form.get('select-att'+str(contadorAtributos))
        arr_setup_pois.append(select)


    res = functions.buscaPontosdeInteresse(1, dados, lista_de_atributos,arr_setup_pois)
    poisResult = functions.listaPois(dados, lista_de_atributos,arr_setup_pois)
    inter = functions.geraIntervalos(lista_de_atributos,janela_para_intervalo)

    return render_template('poi.html', pois=poisResult)


@app.route('/intervalos')
def intervalos():
    global lista_de_atributos
    inter = functions.geraIntervalos(lista_de_atributos,janela_para_intervalo) # a janela para construção do intervalo deve ser passada como parâmetro
    return render_template('intervalos.html', intervalos = inter)


@app.route('/aia')
def aia():
    global lista_de_atributos

    print(lista_de_atributos)

    relations = functions.geraAIA(lista_de_atributos,janela_para_relacoes)
    # print(relations)
    return render_template('aia.html', relat = relations)