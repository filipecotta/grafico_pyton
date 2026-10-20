"""Histograma: distribuição da idade dos clientes."""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_distribuicao.csv")
media, mediana = df["idade"].mean(), df["idade"].median()

fig, ax = plt.subplots(figsize=(9, 5))
ax.hist(df["idade"], bins=15, edgecolor="white")
ax.axvline(media, color="red", linestyle="--", label=f"Média: {media:.1f}")
ax.axvline(mediana, color="green", linestyle="-.", label=f"Mediana: {mediana:.1f}")
ax.set_title("Distribuição da idade dos clientes")
ax.set_xlabel("Idade")
ax.set_ylabel("Número de clientes")
ax.legend()
plt.tight_layout()
plt.savefig("08_distribuicao.png", dpi=150)
plt.show()
