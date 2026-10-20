"""Gráfico de frequência: quantidade de chamados por tipo de atendimento."""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_frequencia.csv")
freq = df["tipo_atendimento"].value_counts()

fig, ax = plt.subplots(figsize=(8, 5))
barras = ax.bar(freq.index, freq.values)
ax.bar_label(barras)
ax.set_title("Frequência de chamados por tipo de atendimento")
ax.set_xlabel("Tipo de atendimento")
ax.set_ylabel("Quantidade")
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("09_frequencia.png", dpi=150)
plt.show()
