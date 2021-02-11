
import pandas as pd

table_sells = pd.read_excel("./Vendas.xlsx")

table_billings = table_sells[["ID Loja",
                              "Valor Final"]].groupby("ID Loja").sum().sort_values("Valor Final", ascending=False)

table_quantity = table_sells[["ID Loja",
                              "Quantidade"]].groupby("ID Loja").sum()
ticket_average = (table_billings["Valor Final"] /
                  table_quantity["Quantidade"]).to_frame().rename(columns={0: "Ticket Medio"})

table_complete = table_billings.join(table_quantity).join(ticket_average)
all_stores = (table_sells["ID Loja"]).unique()

for store in all_stores:
    unique_store = table_sells.loc[table_sells["ID Loja"] == store, [
        "ID Loja", "Quantidade", "Valor Final"]]
    unique_store = unique_store.groupby("ID Loja").sum()
    unique_store["Ticket medio"] = unique_store["Valor Final"] / \
        unique_store["Quantidade"]
    print(unique_store)
