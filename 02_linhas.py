"""Gráfico de linhas: evolução das vendas ao longo do tempo, por loja."""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_linhas.csv", parse_dates=["data"]).sort_values("data")

fig, ax = plt.subplots(figsize=(11, 5))
for loja, grupo in df.groupby("loja"):
    ax.plot(grupo["data"], grupo["vendas"], marker="o", markersize=3,
            linewidth=1.2, label=loja)

ax.set_title("Evolução das vendas por loja")
ax.set_xlabel("Data")
ax.set_ylabel("Vendas")
ax.grid(alpha=0.3)
ax.legend(title="Loja")
fig.autofmt_xdate()
plt.tight_layout()
plt.savefig("02_linhas.png", dpi=150)
plt.show()
