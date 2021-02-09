import smtplib
import email.message
import pandas as pd

table_sells = pd.read_excel("./Vendas.xlsx")

table_billings = table_sells[["ID Loja",
                              "Valor Final"]].groupby("ID Loja").sum().sort_values("Valor Final", ascending=False)

table_quantity = table_sells[["ID Loja",
                              "Quantidade"]].groupby("ID Loja").sum()
ticket_average = (table_billings["Valor Final"] /
                  table_quantity["Quantidade"]).to_frame().rename(columns={0: "Ticket Medio"})

table_complete = table_billings.join(table_quantity).join(ticket_average)
