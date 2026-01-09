import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Paramètres principaux
# -----------------------------
# Taille de l'image
width, height = 2000, 2000

# Paramètres de la spirale logarithmique r = a * e^(b * theta)
a = 0.1
b = 0.15

# Nombre de points sur la spirale
n_points = 2500

# Nombre de petits "givrages" le long de la spirale
n_frost_branches = 800

# -----------------------------
# Calcul de la spirale
# -----------------------------
theta = np.linspace(0, 8 * np.pi, n_points)  # 4 tours environ
r = a * np.exp(b * theta)

# Coordonnées cartésiennes
x = r * np.cos(theta)
y = r * np.sin(theta)

# Normalisation pour la fenêtre de tracé
# On veut que la spirale tienne bien dans la figure
max_extent = np.max(np.abs(np.concatenate([x, y])))
margin = 0.2 * max_extent

# -----------------------------
# Création de la figure
# -----------------------------
fig, ax = plt.subplots(figsize=(8, 8), dpi=250)
fig.patch.set_facecolor(
    (0.10, 0.20, 0.35)
)  # Assurer que le fond de la figure est foncé

# Fond légèrement texturé : on utilise un "nuage" de points bleu clair
# pour faire une impression de neige / grain
bg_points = 40000
bg_x = np.random.uniform(-max_extent - margin, max_extent + margin, bg_points)
bg_y = np.random.uniform(-max_extent - margin, max_extent + margin, bg_points)
bg_alpha = np.random.uniform(0.02, 0.08, bg_points)

ax.scatter(
    bg_x,
    bg_y,
    s=1.5,
    c=[(0.75, 0.85, 1.0, a) for a in bg_alpha],
    marker="o",
    linewidths=0,
)

# Couleur de fond générale (bleu glacé)
ax.set_facecolor((0.10, 0.20, 0.35))

# -----------------------------
# Tracer la spirale principale
# -----------------------------
ax.plot(x, y, color="white", linewidth=10.0, solid_capstyle="round", alpha=0.95)

# -----------------------------
# Ajout de petits flocons radiaux sur la spirale
# -----------------------------
# On place des flocons à intervalles réguliers le long de la spirale
n_snowflakes = 150  # Nombre de flocons
snowflake_indices = np.linspace(100, n_points - 100, n_snowflakes, dtype=int)

for idx in snowflake_indices:
    x0, y0 = x[idx], y[idx]

    # Taille du flocon (proportionnelle au rayon)
    flake_size = 0.015 * max_extent * (r[idx] / (r.max() + 0.1))

    # Créer 6 branches radiales (symétrie hexagonale typique des flocons)
    for i in range(6):
        angle = np.deg2rad(60 * i + np.random.uniform(-5, 5))  # Petit bruit angulaire

        # Branche principale du flocon
        x_end = x0 + flake_size * np.cos(angle)
        y_end = y0 + flake_size * np.sin(angle)

        ax.plot(
            [x0, x_end],
            [y0, y_end],
            color=(1.0, 1.0, 1.0, 0.8),
            linewidth=0.8,
            solid_capstyle="round",
        )

        # Petites branches latérales (comme des cristaux)
        for side in [-1, 1]:
            side_angle = angle + np.deg2rad(30 * side)
            x_side = x0 + 0.6 * flake_size * np.cos(side_angle)
            y_side = y0 + 0.6 * flake_size * np.sin(side_angle)

            ax.plot(
                [x0, x_side],
                [y0, y_side],
                color=(1.0, 1.0, 1.0, 0.6),
                linewidth=0.5,
                solid_capstyle="round",
            )

# -----------------------------
# Ajout des branches de givre "fougères"
# -----------------------------
# On choisit aléatoirement des indices le long de la spirale
indices = np.random.choice(n_points, size=n_frost_branches, replace=False)

for idx in indices:
    x0, y0 = x[idx], y[idx]
    vx, vy = x0, y0
    norm = np.hypot(vx, vy)
    if norm == 0:
        continue
    vx /= norm
    vy /= norm

    # Longueur de base de la branche
    base_len = 0.04 * max_extent
    length = base_len * np.random.uniform(0.4, 1.1) * (r[idx] / (r.max() + 0.1))

    for sign in [-1, 1]:
        # Angle de la branche principale
        angle = np.deg2rad(np.random.uniform(35, 65)) * sign
        vx_b = vx * np.cos(angle) - vy * np.sin(angle)
        vy_b = vx * np.sin(angle) + vy * np.cos(angle)

        x1, y1 = x0 + vx_b * length, y0 + vy_b * length

        # Tracer la branche principale (plus fine que la spirale)
        ax.plot(
            [x0, x1],
            [y0, y1],
            color=(0.95, 0.98, 1.0, 0.9),
            linewidth=2.0,
            solid_capstyle="round",
        )

        # Ajouter des "plumes" (sous-branches) le long de cette branche
        n_feathers = 7
        for i in range(1, n_feathers + 1):
            f_pos = i / (n_feathers + 1)  # Position le long de la branche
            xf, yf = x0 + f_pos * vx_b * length, y0 + f_pos * vy_b * length

            # La "plume" repart avec un angle par rapport à la branche
            f_angle = np.deg2rad(np.random.uniform(25, 45)) * sign * -1
            vx_f = vx_b * np.cos(f_angle) - vy_b * np.sin(f_angle)
            vy_f = vx_b * np.sin(f_angle) + vy_b * np.cos(f_angle)

            f_len = length * 0.4 * (1 - f_pos * 0.6)
            ax.plot(
                [xf, xf + vx_f * f_len],
                [yf, yf + vy_f * f_len],
                color=(0.9, 0.95, 1.0, 0.7),
                linewidth=1.2,
                solid_capstyle="round",
            )


# -----------------------------
# Finitions de la figure
# -----------------------------
ax.set_aspect("equal", "box")
ax.set_xlim(-max_extent - margin, max_extent + margin)
ax.set_ylim(-max_extent - margin, max_extent + margin)
ax.axis("off")

plt.tight_layout()
output_file = "spirale_glacee.png"
plt.savefig(output_file, dpi=300, bbox_inches="tight", pad_inches=0)
print(f"Image enregistrée : {output_file}")
