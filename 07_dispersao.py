"""Gráfico de dispersão: altura x peso, colorido por sexo."""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_dispersao.csv")

fig, ax = plt.subplots(figsize=(8, 6))
for sexo, grupo in df.groupby("sexo"):
    ax.scatter(grupo["altura_cm"], grupo["peso_kg"], alpha=0.7, label=sexo)

ax.set_title("Altura x peso")
ax.set_xlabel("Altura (cm)")
ax.set_ylabel("Peso (kg)")
ax.grid(alpha=0.3)
ax.legend(title="Sexo")
plt.tight_layout()
plt.savefig("07_dispersao.png", dpi=150)
plt.show()
