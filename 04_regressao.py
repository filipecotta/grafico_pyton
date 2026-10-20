"""Regressão linear: gasto mensal em função da renda mensal."""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_regressao.csv")
x, y = df["renda_mensal"], df["gasto_mensal"]

a, b = np.polyfit(x, y, 1)            # y = a*x + b
r2 = np.corrcoef(x, y)[0, 1] ** 2
xs = np.linspace(x.min(), x.max(), 100)

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(x, y, alpha=0.6, label="Dados")
ax.plot(xs, a * xs + b, color="red", linewidth=2,
        label=f"y = {a:.3f}x + {b:.1f}  (R² = {r2:.3f})")
ax.set_title("Regressão linear: renda x gasto mensal")
ax.set_xlabel("Renda mensal")
ax.set_ylabel("Gasto mensal")
ax.grid(alpha=0.3)
ax.legend()
plt.tight_layout()
plt.savefig("04_regressao.png", dpi=150)
plt.show()
