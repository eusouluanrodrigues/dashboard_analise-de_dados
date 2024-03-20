# Aqui você formata um numero 


from dataset import df
import pandas as pd

def format_number(value, prefix =''):
   
    for unit in ['','mil']:
        if value < 1000:
            return f'{prefix} {value:,.2f} {unit}'.replace(",", "x").replace(".", ",").replace("x", ".")
        value /= 1000
    return f'{prefix} R${value:,.2f} milhões'.replace(",", "x").replace(".", ",").replace("x", ".")


#--------------------------------------------------------------------------------------------#

# Descobre a equipe com maior FATURAMENTO


def equipe_com_maior_faturamento(df):
    # Agrupe os dados pela coluna 'Equipe' e calcule a soma de 'Valor Pago' para cada grupo
    df_grouped_equipe = df.groupby('Equipe')['Valor Pago'].sum()

    # Encontre a equipe com o maior faturamento
    equipe_maior_faturamento = df_grouped_equipe.idxmax()
    faturamento_maior_equipe = df_grouped_equipe.max()

    return equipe_maior_faturamento, faturamento_maior_equipe


#----------------------------------------------------------------------------------------------#


