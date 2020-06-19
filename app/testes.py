conjUnicos = list()


with open('../dados/RelacoesTemporais.csv','r') as f:
    linhas = f.readlines()
    for posLinha, l in enumerate(linhas):
        l = l.replace(' ','')
        elementosLinha = l.split(',')

        for posItem,e in enumerate(elementosLinha):
            if e not in conjUnicos and e != '' and e != '\n':
                 conjUnicos.append(e)



txt = "@relation RELACOES\n"

txt2 = ','.join(conjUnicos)+'\n'
for rel in conjUnicos:
    txt += "@attribute " + str(rel) + " {TRUE,FALSE}\n"

txt += "\n@data\n"

for l in linhas:
    matches = []
    l = l.replace(',\n','\n')
    l = l.replace(' ','')
    elementosLinha = l.split(',')
    conjElementosLinha = set(elementosLinha)

    for item in conjUnicos:
        if item in conjElementosLinha:
            matches.append('TRUE')
        else:
            matches.append('FALSE')


    txt += ','.join(map(str, matches))+'\n'
    txt2 +=','.join(map(str, matches))+'\n'



print(len(conjUnicos))
with open('../dados/relacoes.arff', 'w') as w:
    w.write(txt)
with open('../dados/relacoesBIN.csv', 'w') as w:
    w.write(txt2)