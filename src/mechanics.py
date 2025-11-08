# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 13:15:19 2025

@author: Laszlo
"""

# 2. 🧱 mechanics.py – Szilárdságtani modul

import numpy as np
import matplotlib.pyplot as plt

def run_mechanics():
    # Paraméterek
    a, b, c, d = 1.0, 0.1, 2.0, 0.05
    E, epsilon_0, alpha = 210000, 0.001, 0.02
    t = np.linspace(0, 10, 1000)

    # Spirális koordináták
    r = a * np.exp(b * t)
    phi = c * t
    z = d * t
    x = r * np.cos(phi)
    y = r * np.sin(phi)

    # Hooke-törvény
    epsilon = epsilon_0 * np.exp(-alpha * t) * np.cos(c * t)
    sigma = E * epsilon
    sigma_spiral = E * epsilon_0 * np.exp(-alpha * t) / np.sqrt(2 * np.pi * r)

    # Vizualizáció
    fig = plt.figure(figsize=(15, 10))

    ax1 = fig.add_subplot(231, projection='3d')
    ax1.plot(x, y, z, 'r-', linewidth=2)
    ax1.set_title('Spirális repedésterjedés')

    ax2 = fig.add_subplot(232)
    ax2.plot(t, sigma, 'b-')
    ax2.set_title('Hooke-törvény: σ = E·ε')

    ax3 = fig.add_subplot(233)
    ax3.plot(epsilon, sigma, 'g-')
    ax3.set_title('Fázistér - Spirális pálya')

    ax4 = fig.add_subplot(234)
    scatter = ax4.scatter(x, y, c=sigma_spiral, cmap='hot', s=10)
    ax4.set_title('Feszültség spirális térben')
    plt.colorbar(scatter, ax=ax4)

    plt.tight_layout()
    plt.show()

    # Numerikus eredmények
    return {
        "Max feszültség": np.max(sigma),
        "Repedéshossz": np.sqrt(x[-1]**2 + y[-1]**2),
        "Alakváltozás": np.max(epsilon)
    }