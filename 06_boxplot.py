"""Boxplot: distribuição de salários por departamento."""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_boxplot.csv")
deptos = sorted(df["departamento"].unique())
dados = [df.loc[df["departamento"] == d, "salario"] for d in deptos]

fig, ax = plt.subplots(figsize=(9, 6))
ax.boxplot(dados, tick_labels=deptos, patch_artist=True, showmeans=True)
ax.set_title("Distribuição de salários por departamento")
ax.set_xlabel("Departamento")
ax.set_ylabel("Salário")
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("06_boxplot.png", dpi=150)
plt.show()
