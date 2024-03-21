import plotly.express as px # Importa biblioteca gráfica
from utils import format_number, equipe_com_maior_faturamento
import pandas as pd
import streamlit as st


def exibir_receita_e_grafico(df):
    # Remova o símbolo 'R$', os espaços em branco e os pontos
    # Substituir todas as ocorrências de uma sub-string dentro de uma string. Ele retorna uma nova string com as substituições feitas
    df['Valor Pago'] = df['Valor Pago'].str.replace('R$', '').str.replace('.', '').str.strip().astype(float)

    # Agora você pode calcular a soma da receita total
    receita_total = df['Valor Pago'].sum()

    # Formate a receita total como uma string de moeda
    receita_total_formatada = format_number(receita_total)

    # Exiba a receita total
    st.metric('Receita Total', receita_total_formatada)

    # Adicione um espaço de 10 linhas antes do gráfico
    for _ in range(5):
        st.write("")

    # Agrupe os dados pela coluna 'Meio de Propaganda' e calcule a soma de 'Valor Pago' para cada grupo
    df_grouped = df.groupby('Meio de Propaganda')['Valor Pago'].sum().reset_index()

    # Retorne o DataFrame agrupado
    return df_grouped


#---------------------------------------------------------------------------------------------------------#

def exibir_receita_equipes(df):
    # Exiba a equipe com o maior faturamento
    # Exibir uma métrica
    # Label = Define o rótulo da métrica como o valor da variável
    
    equipe, faturamento = equipe_com_maior_faturamento(df)
    st.metric(label=equipe, value=format_number(faturamento))

    # Defina a ordem correta dos meses
    ordem_meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

    # Converta 'Mês' para um tipo categórico com a ordem correta dos meses
    df['Mês'] = pd.Categorical(df['Mês'], categories=ordem_meses, ordered=True)

    # Agora, quando você agrupa e plota os dados, os meses devem aparecer na ordem correta
    # Transformando os dados e remodulando 
    df_grouped_mes = df.groupby(['Equipe', 'Mês'])['Valor Pago'].sum().reset_index()
    df_pivot = df_grouped_mes.pivot(index='Mês', columns='Equipe', values='Valor Pago')

    #Titulo receita Equipes
    st.subheader("Receita Equipes")

    # Crie um gráfico de linha com streamlit
    st.line_chart(df_pivot)

    # Retorne o DataFrame pivot
    return df_pivot
