# artq
artq-flask repo


{% extends "layout.html" %}
{% block content %}

<div>
    <h1>ART-Q</h1>
    <p>O crescente volume de dados gerados constantemente demanda de técnicas cada vez mais eficientes para a aquisição
        de informações úteis. O presente estudo objetiva a definição e construção de um novo método para refinar o
        processo de mineração de regras de associação ao incorporar o aspecto temporal de forma explícita, associado a
        dados quantitativos contínuos. Cada ponto temporal em que uma característica (atributo) assume um valor de
        interesse dependente da distribuição de probabilidade que a representa. Os pontos temporais são, então,
        componentes de um intervalo de interesse da característica. As relações temporais entre os intervalos de
        interesse das características são mapeadas por meio do uso da Álgebra Intervalar de Allen. Padrões podem ser
        identificados e regras de associação construídas no conjunto resultante de relações temporais de interesse. Até
        o presente momento, os experimentos resultaram regras estruturalmente semelhantes àquelas geradas pela mineração
        de regras de associação tradicional. Entretanto, as regras são diretamente relacionadas aos intervalos temporais
        associados aos dados. O que evidencia que a técnica é capaz de gerar regras de associação com uma nova semântica
        que expressa quais as relações entre a duração e ocorrência eventos importantes presentes na base de dados. Ao
        mesmo passo em que é capaz de lidar com dados quantitativos contínuos sem a necessidade da tarefa de discretizar
        os dados. Em termos de eficiência computacional, a nova estratégia não implicou em acréscimos consideráveis para
        o tempo de execução do processo de mineração de regras de associação. Esta nova estratégia tem o potencial de
        refinar o processo de mineração de regras de associação em dados quantitativos contínuos, pois o aspecto da
        temporalidade, que resulta em regras diferentes (com novas informações) daquelas geradas pelo emprego da
        estratégia tradicional.
</p>
    <br />
    <h1>Abstract</h1>
    <p>Data mining techniques are important components in the process of knowledge discovering, and play a key role in data analysis strategies. Due to this it has been the focus of many recent studies. However, this process can be adversely affected under certain conditions such as considering categorical values instead of originally raw data. Beside that far too little attention has been paying to the temporal information associated to the data, which can reveals lots of implicit information as well. This paper describes the design and implementation of a new method to deal with quantitative continuous data in association rules miner process, specially when considering explicit temporal information associated to the data. Taken together, the obtained results suggest that the analysis of data can be potentially increased by the adoption of temporal aspects and the raw data in the process. Moreover drawing association rules shows that it can be better understood by the human expert.</p>


    <span><b>Keywords: </b> Datamining, association rules, temporal association rules, quantiative continuous data</span>

<br />
    <span>Lookup in the whole content <a href="filehere" target="_blank">here</a></span>
</div>

{% endblock %}