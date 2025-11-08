# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 13:17:28 2025

@author: Laszlo
"""

# 6. ⚡ electromagnetics.py – Villamoságtan modul

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def run_electromagnetics():
    mu0 = 4e-7 * np.pi
    N, I, f = 100, 1.0, 50e6
    omega = 2 * np.pi * f

    def spiral_coil(t, a=0.1, b=0.05, c=10.0, d=0.01):
        r = a * np.exp(b * t)
        phi = c * t
        z = d * t
        x = r * np.cos(phi)
        y = r * np.sin(phi)
        return x, y, z, r

    def em_wave_spiral(t, E0=1.0, k=1.0):
        Ex = E0 * np.cos(omega * t - k)
        Ey = E0 * np.sin(omega * t - k)
        Ez = 0.1 * E0 * np.sin(2 * omega * t - k)
        return Ex, Ey, Ez

    t_coil = np.linspace(0, 4*np.pi, 1000)
    t_wave = np.linspace(0, 2e-8, 1000)
    x_coil, y_coil, z_coil, r_coil = spiral_coil(t_coil)
    B_theta = (mu0 * N * I) / (2 * np.pi * r_coil)
    Ex, Ey, Ez = em_wave_spiral(t_wave)

    fig = plt.figure(figsize=(16, 12))
    ax1 = fig.add_subplot(231, projection='3d')
    ax1.plot(x_coil, y_coil, z_coil, 'r-', linewidth=2)
    ax1.set_title('Spirális tekercs geometria')

    ax2 = fig.add_subplot(232)
    ax2.plot(t_coil, B_theta * 1e6, 'b-')
    ax2.set_title('Mágneses tér spirális tekercsben')

    ax3 = fig.add_subplot(233, projection='3d')
    ax3.plot(Ex, Ey, np.zeros_like(Ex), 'g-', alpha=0.7)
    ax3.set_title('EM hullám spirális polarizáció')

    ax4 = fig.add_subplot(234)
    ax4.plot(t_wave * 1e9, Ex, 'r-', label='Ex')
    ax4.plot(t_wave * 1e9, Ey, 'b-', label='Ey')
    ax4.set_title('EM hullám komponensek')
    ax4.legend()

    r_avg = np.mean(r_coil)
    length_coil = np.trapz(np.sqrt(np.gradient(x_coil)**2 +
                                   np.gradient(y_coil)**2 +
                                   np.gradient(z_coil)**2))
    A_coil = np.pi * r_avg**2
    L_spiral = mu0 * N**2 * A_coil / length_coil

    ax5 = fig.add_subplot(235)
    components = ['Hagyományos', 'Spirális']
    inductance_values = [mu0 * N**2 * A_coil / 0.1, L_spiral]
    bars = ax5.bar(components, inductance_values, color=['blue', 'red'])
    ax5.set_title('Induktivitás összehasonlítás')
    for bar, value in zip(bars, inductance_values):
        ax5.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
                 f'{value:.2e} H', ha='center', va='bottom')

    energy_density = 0.5 * mu0 * (B_theta**2) / mu0
    ax6 = fig.add_subplot(236)
    ax6.plot(t_coil, energy_density, 'purple')
    ax6.set_title('Mágneses energiasűrűség')

    plt.tight_layout()
    plt.show()

    return {
        "Induktivitás": L_spiral,
        "Mágneses tér": np.mean(B_theta)*1e6,
        "Frekvencia": f/1e6,
        "Hullámimpedancia": np.sqrt(mu0 / (8.854e-12))
    }

