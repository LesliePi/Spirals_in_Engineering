# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 13:16:36 2025

@author: Laszlo
"""

# 4. 🌪️ fluid_dynamics.py – Áramlástan modul

import numpy as np
import matplotlib.pyplot as plt

def run_fluid_dynamics():
    Gamma, nu = 5.0, 1e-6
    def lamb_oseen_vortex(r, t):
        epsilon = 1e-12  # kis pozitív érték, hogy elkerüljük az osztást nullával
        t_safe = max(t, epsilon)
        r_safe = np.where(r == 0, epsilon, r)
        return (Gamma / (2 * np.pi * r_safe)) * (1 - np.exp(-r_safe**2 / (4 * nu * t_safe)))


    def spiral_vortex_field(x, y, t, a=1.0, b=0.2, c=2.0):
        r = np.sqrt(x**2 + y**2)
        phi = np.arctan2(y, x)
        spiral_mod = np.exp(-b * r) * np.sin(c * phi - t)
        v_r = -0.1 * r * spiral_mod
        v_theta = lamb_oseen_vortex(r, t) * (1 + 0.5 * spiral_mod)
        v_x = v_r * np.cos(phi) - v_theta * np.sin(phi)
        v_y = v_r * np.sin(phi) + v_theta * np.cos(phi)
        return v_x, v_y

    x = np.linspace(-3, 3, 50)
    y = np.linspace(-3, 3, 50)
    X, Y = np.meshgrid(x, y)
    VX, VY = spiral_vortex_field(X, Y, t=2.0)
    P = -0.5 * (VX**2 + VY**2)
    vorticity = np.gradient(VY, x, axis=1) - np.gradient(VX, y, axis=0)

    fig, axes = plt.subplots(2, 2, figsize=(15, 12))

    axes[0,0].streamplot(X, Y, VX, VY, density=2, color='blue')
    axes[0,0].set_title('Spirális örvény sebességmező')

    im2 = axes[0,1].contourf(X, Y, P, levels=50, cmap='viridis')
    axes[0,1].set_title('Nyomás eloszlás')
    plt.colorbar(im2, ax=axes[0,1])

    im3 = axes[1,0].contourf(X, Y, vorticity, levels=50, cmap='coolwarm')
    axes[1,0].set_title('Örvényesség')
    plt.colorbar(im3, ax=axes[1,0])

    r_profile = np.linspace(0.1, 3, 100)
    v_profile = lamb_oseen_vortex(r_profile, 2.0)
    axes[1,1].plot(r_profile, v_profile, 'r-')
    axes[1,1].set_title('Sebességprofil')

    plt.tight_layout()
    plt.show()

    return {
        "Max sebesség": np.max(np.sqrt(VX**2 + VY**2)),
        "Átlag nyomás": np.mean(P),
        "Örvényesség": np.max(vorticity)
    }

