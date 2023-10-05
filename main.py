import pandas as pd

#Nome da Planilha
arquivo_excel = 'Qrcode.xlsx'

# Carregue o arquivo Excel em um DataFrame do pandas
df = pd.read_excel(arquivo_excel)

# Filtre as linhas onde a coluna 'Estado' (suponha que esse seja o nome da coluna com 'MG') contém 'MG'
df_mg = df[df['Localidade'] == 'MG']

# Filtrar as linhas com base na coluna 'Modelo Maquina' que contenham 'UL152'
filtro = df_mg['Modelo Maquina'].str.contains('UL152', case=False)

# Crie um novo DataFrame com as linhas que atendem ao filtro
df_ul152 = df_mg[filtro]

# Crie um novo arquivo Excel com as linhas filtradas
arquivo_saida = 'dados_mg_ul152.xlsx'
df_ul152.to_excel(arquivo_saida, index=False)

print(f"As linhas com 'MG' e 'UL152' foram salvas em '{arquivo_saida}'")
