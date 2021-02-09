import pandas as pd

table_sells = pd.read_excel("./Vendas.xlsx")

table_faturation = table_sells[["ID Loja",
                                "Valor Final"]].groupby("ID Loja").sum().sort_values("Valor Final", ascending=False)

print(table_faturation)
