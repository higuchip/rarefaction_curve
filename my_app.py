import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px


st.title("Gerador de Curva de Rarefação 🌿")

st.write("## Apresentação")

st.write(
    "Bem vindo! Meu nome é [Pedro Higuchi](https://www.linkedin.com/in/pedro-higuchi-4085a81b/), Engenheiro Florestal, Doutor em Ciências Florestais pela Universidade Federal de Lavras e, atualmente, Professor Associado, da Universidade do Estado de Santa Catarina,  onde leciono no Curso de Engenheira Florestal."
)

st.write(
    "Aqui apresento um aplicativo para gerar **Curvas de Rarefação**, que é uma importante ferramenta analítica, para quem trabalha com inventários da biodiversidade."
)


st.write("## Contextualização")

st.write(
    "O número de espécies (riqueza) representa uma das dimensões da diversidade e é uma das mais importantes propriedades de um ecossistema."
)

st.write(
    "A sua determinação permite inferências ecológicas relevantes e pode subsidiar inúmeras aplicações práticas, tais como em Estudos de Impactos Ambientais, Gestão de Unidades Conservação,eo Manejo Sustentável de Recursos Naturais. No vídeo abaixo, faço uma breve apresentação sobre o tema."
)

st.write("## Instrução de uso")
st.write("### 1. Preparação do arquivo de entrada:")

st.write(
    "O arquivo de entrada deve estar no formato csv e conter duas colunas: 'especies' (sem acento) e 'n'. A coluna deve ser preenchida com a relação das espécies e a coluna 'n', com o número total de indivíduos para cada espécie."
)
st.write("Exemplo:")

st.write(
    pd.DataFrame(
        {
            "Especies": [
                "Araucaria angustifolia",
                "Podocarpus lambertti",
                "Myrcia oblongata",
                "Ilex paraguariensis",
            ],
            "n": [10, 20, 30, 40],
        }
    )
)

st.write("### 2. Inserir arquivo:")

dados = st.file_uploader("Escolha o arquivo csv", type={"csv", "txt"})
if dados is not None:
    df = pd.read_csv(dados, delimiter=";")
    df_long = df.reindex(df.index.repeat(df.n))
    sp_shuffle = []
    for i in range(100):
        sp_shuffle.append(((~df_long.sample(frac=1)["Especies"].duplicated()).cumsum()))
    mean_rarefy_curve = np.mean(sp_shuffle, axis=0)

    fig = px.line(
        x=np.arange(len(df_long)),
        y=mean_rarefy_curve,
        title="Curva de rarefação pelo método de aleatorização (n=100)",
        labels={
            "x": "Número de indivíduos",
            "y": "Riqueza (S)",
        },
        template="plotly_white",
    )

    st.plotly_chart(fig, use_container_width=True)

st.write("## Método utilizado")
st.write(
    "A curva é construída a partir da contagem acumulativa de espécies, por meio de 100 aleatorização de todos os indivíduos existentes no arquivo de entrada. Desta forma, cada valor no Eixo y representa uma média de número de espécies para n individuos obtidos da aleatorização citada."
)

st.write("## Contato")
st.write(
    "Em caso de dúvidas ou outras informações entre em [contato] (https://www.linkedin.com/in/pedro-higuchi-4085a81b/)."
)


@st.cache(allow_output_mutation=True)
def Pageviews():
    return []


pageviews = Pageviews()
pageviews.append("dummy")

try:
    st.markdown("Contador: {}".format(len(pageviews)))
except ValueError:
    st.markdown("Contador: {}".format(1))
