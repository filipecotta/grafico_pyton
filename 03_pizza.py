"""Gráfico de pizza: participação de cada canal no faturamento."""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_pizza.csv")

fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(df["faturamento"], labels=df["canal_venda"], autopct="%1.1f%%",
       startangle=90, counterclock=False,
       wedgeprops={"edgecolor": "white"})
ax.set_title("Faturamento por canal de venda")
plt.tight_layout()
plt.savefig("03_pizza.png", dpi=150)
plt.show()
