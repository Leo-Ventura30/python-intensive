import pandas as pd
import plotly.express as px
# dropna() elimina linhas com campos vazios
clients_table = pd.read_csv(r"ClientesBanco.csv",
                            encoding="latin1").drop("CLIENTNUM", axis=1).dropna()

# visualizar informaçoes da tabela
# print(clients_table.info())

# base de calculos correlativos de dados comuns
# print(clients_table.describe())

print(clients_table["Categoria"].value_counts())


def grafico_categoria(coluna, tabela):
    fig = px.histogram(tabela, x=coluna, color="Idade")
    fig.show()


category_clients = clients_table["Categoria"].to_frame()
age_clients = clients_table["Idade"].to_frame().sort_values("Idade")
for coluna in age_clients:
    print(age_clients)
    grafico_categoria(coluna, age_clients)
