import streamlit as st
import matplotlib.pyplot as plt
import math
import random

st.title("Renkli Kalp Çizimi ❤️")

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor("black")
fig.patch.set_facecolor("black")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(120):
    angle = i * (math.pi * 2) / 120

    x = 16 * (math.sin(angle) ** 3) * 15
    y = (
        13 * math.cos(angle)
        - 5 * math.cos(2 * angle)
        - 2 * math.cos(3 * angle)
        - math.cos(4 * angle)
    ) * 15

    c = random.choice(colors)

    ax.plot([0, x], [40, y], color=c, linewidth=1)

    for _ in range(8):
        ax.plot(
            [x, x + 6],
            [y, y + 6],
            color=c,
            linewidth=1
        )

ax.axis("off")

st.pyplot(fig)
