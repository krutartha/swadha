import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import to_rgb

# Define the color palettes
palettes = {
    "Elemental Harmony": {
        "Sacred Fire": "#FF6B35",
        "Pure Water": "#4ECDC4", 
        "Solar Energy": "#FF8C42",
        "Spirit Air": "#8B4513",
        "Vital Earth": "#4CAF50",
        "Sacred Ground": "#5D4037",
    },
    "Earthy Elegance": {
        "Terracotta": "#C95F47",
        "Sandalwood Beige": "#E5D3B3",
        "Forest Green": "#3A5A40",
        "Gold": "#BFA66B",
        "Ivory": "#F8F4EC",
    },
    "Himalayan Serenity": {
        "Himalayan Blue": "#8FB5B2",
        "Ash Grey": "#A8A29E",
        "Marigold Yellow": "#FFD56B",
        "Charcoal Black": "#2E2E2E",
        "Stone White": "#F3F2ED",
    },
    "Deep Roots": {
        "Indigo": "#2C2D5B",
        "Saffron Orange": "#ED9B40",
        "Lotus Pink": "#D36C6C",
        "Olive Green": "#7A8450",
        "Natural Linen": "#E9E4D4",
    },
}

# Plot the color palettes
fig, axs = plt.subplots(len(palettes), 1, figsize=(12, 8), constrained_layout=True)

for i, (palette_name, colors) in enumerate(palettes.items()):
    hex_colors = list(colors.values())
    rgb_row = np.array([to_rgb(c) for c in hex_colors])[np.newaxis, :, :]

    axs[i].imshow(rgb_row, aspect="auto")
    n = len(hex_colors)
    axs[i].set_xticks(range(n))
    axs[i].set_xticklabels(list(colors.keys()), rotation=45, ha="right")
    axs[i].set_yticks([])
    axs[i].set_title(palette_name, fontsize=14, fontweight="bold")
    for spine in axs[i].spines.values():
        spine.set_visible(False)

plt.show()


