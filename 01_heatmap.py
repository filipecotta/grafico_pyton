"""Mapa de calor: movimento de clientes por dia da semana e horário."""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_heatmap.csv")

ordem_dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
tabela = df.pivot_table(index="dia_semana", columns="horario",
                        values="movimento_clientes", aggfunc="mean")
tabela = tabela.reindex(ordem_dias)
# ordena as colunas de horário cronologicamente
tabela = tabela[sorted(tabela.columns, key=lambda h: int(h.split(":")[0]))]

fig, ax = plt.subplots(figsize=(10, 6))
im = ax.imshow(tabela.values, cmap="YlOrRd", aspect="auto")
ax.set_xticks(range(len(tabela.columns)), tabela.columns)
ax.set_yticks(range(len(tabela.index)), tabela.index)

for i in range(tabela.shape[0]):
    for j in range(tabela.shape[1]):
        ax.text(j, i, f"{tabela.values[i, j]:.0f}", ha="center", va="center", fontsize=9)

fig.colorbar(im, ax=ax, label="Movimento de clientes")
ax.set_title("Movimento de clientes por dia da semana e horário")
ax.set_xlabel("Horário")
ax.set_ylabel("Dia da semana")
plt.tight_layout()
plt.savefig("01_heatmap.png", dpi=150)
plt.show()
