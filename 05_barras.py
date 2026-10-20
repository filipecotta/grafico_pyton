"""Barras agrupadas: vendas médias por categoria e região."""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_barras.csv")
tabela = df.pivot(index="categoria", columns="regiao", values="vendas_medias")

categorias = tabela.index
regioes = tabela.columns
x = np.arange(len(categorias))
largura = 0.8 / len(regioes)

fig, ax = plt.subplots(figsize=(10, 6))
for i, regiao in enumerate(regioes):
    ax.bar(x + i * largura - 0.4 + largura / 2, tabela[regiao],
           largura, label=regiao)

ax.set_xticks(x, categorias)
ax.set_title("Vendas médias por categoria e região")
ax.set_xlabel("Categoria")
ax.set_ylabel("Vendas médias")
ax.grid(axis="y", alpha=0.3)
ax.legend(title="Região")
plt.tight_layout()
plt.savefig("05_barras.png", dpi=150)
plt.show()
