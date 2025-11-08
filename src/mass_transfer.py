# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 13:17:07 2025

@author: Laszlo
"""

# 5. 🧪 mass_transfer.py – Anyagátadástan modul

import numpy as np
import matplotlib.pyplot as plt

def run_mass_transfer():
    D, c0 = 1e-9, 1.0
    def spiral_diffusion(x, y, t, D, a=1.0, b=0.3, c=2.0):
        r = np.sqrt(x**2 + y**2)
        phi = np.arctan2(y, x)
        spiral_pattern = np.exp(-b * r) * np.cos(c * phi)
        concentration = c0 * np.exp(-r**2 / (4 * D * t)) / (4 * np.pi * D * t)
        return concentration * (1 + 0.5 * spiral_pattern)

    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x, y)
    times = [0.1, 1.0, 5.0, 10.0]

    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    for i, t_val in enumerate(times):
        C = spiral_diffusion(X, Y, t_val, D)
        row, col = i // 2, i % 2
        im = axes[row, col].contourf(X, Y, C, levels=50, cmap='plasma')
        axes[row, col].set_title(f'Spirális diffúzió t = {t_val}s')
        plt.colorbar(im, ax=axes[row, col])

    fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    time_range = np.linspace(0.1, 20, 100)
    center_concentration = [spiral_diffusion(0, 0, t, D) for t in time_range]
    ax1.plot(time_range, center_concentration, 'b-')
    ax1.set_title('Koncentráció változás a középpontban')

    r_profile = np.linspace(0, 2, 100)
    concentration_profile = spiral_diffusion(r_profile, 0, 5.0, D)
    ax2.plot(r_profile, concentration_profile, 'r-')
    ax2.set_title('Koncentráció profil spirális sugárban')

    plt.tight_layout()
    plt.show()

    C_final = spiral_diffusion(X, Y, 10.0, D)
    return {
        "Kezdeti konc.": c0,
        "Végső konc.": spiral_diffusion(0, 0, 10.0, D),
        "Diffúziós egy.": D
    }

