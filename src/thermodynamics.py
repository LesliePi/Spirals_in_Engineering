# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 13:15:43 2025

@author: Laszlo
"""


# 3. 🔥 thermodynamics.py – Hőtan modul

import numpy as np
import matplotlib.pyplot as plt

def run_thermodynamics():
    T0, beta = 100.0, 0.3
    r_vals = np.linspace(0.1, 5, 100)
    phi_vals = np.linspace(0, 4*np.pi, 100)
    R, PHI = np.meshgrid(r_vals, phi_vals)

    def spiral_temperature(r, phi):
        return T0 * np.exp(-beta * r) * np.cos(phi)

    T = spiral_temperature(R, PHI)
    X = R * np.cos(PHI)
    Y = R * np.sin(PHI)

    fig, axes = plt.subplots(2, 2, figsize=(15, 12))

    im1 = axes[0,0].contourf(X, Y, T, levels=50, cmap='hot')
    axes[0,0].set_title('Spirális hőmérséklet eloszlás')
    plt.colorbar(im1, ax=axes[0,0])

    axes[0,1].plot(r_vals, spiral_temperature(r_vals, 0), 'r-')
    axes[0,1].set_title('Hőmérséklet csökkenés spirális sugárban')

    ax3d = fig.add_subplot(2, 2, 3, projection='3d')
    ax3d.plot_surface(X, Y, T, cmap='hot', alpha=0.8)
    ax3d.set_title('3D Spirális hőáramlás')

    times = [0.5, 1.0, 2.0, 5.0]
    for t_val in times:
        T_time = spiral_temperature(r_vals, 0)
        axes[1,1].plot(r_vals, T_time, label=f't = {t_val}s')
    axes[1,1].set_title('Időbeli hőterjedés')
    axes[1,1].legend()

    plt.tight_layout()
    plt.show()

    return {
        "Max hőmérséklet": np.max(T),
        "Átlag hőmérséklet": np.mean(T),
        "Hőgradiens": np.max(T) - np.min(T)
    }