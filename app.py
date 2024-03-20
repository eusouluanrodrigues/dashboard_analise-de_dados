import streamlit as st
import plotly.express as px
import pandas as pd
from dataset import  df
from graficos import exibir_receita_e_grafico, exibir_receita_equipes

#----------------------------------------------------------------#

# Configurando a página no formato landing page
st.set_page_config(layout="wide")

# Adicionando título ao dashboard
st.title("Dashboard Call Center :telephone:")

#Adicionando abas para melhorar a visualização dos dados
aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Equipes'])

#--------------------------------------------------------------#

# Enquanto estiver na aba1 execute o df: dataframe que importamos do nosso dataset.py
with aba1:
    st.dataframe(df)

# Na segunda sera mostrado a receita total que vou faturada / receita por produtos vendidos
with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        df_grouped = exibir_receita_e_grafico(df)
        st.bar_chart(df_grouped.set_index('Meio de Propaganda'))

    with aba3:
       
       st.subheader('Equipe com maior Faturamento')
       df_pivot = exibir_receita_equipes(df)



