# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 12:45:22 2025

@author: Laszlo
"""

# 1. 🧭 main.py – Fő vezérlőprogram

from mechanics import run_mechanics
from thermodynamics import run_thermodynamics
from fluid_dynamics import run_fluid_dynamics
from mass_transfer import run_mass_transfer
from electromagnetics import run_electromagnetics
from summary import summarize_results

def main():
    print("="*60)
    print("SPIRÁLIS MÉRNÖKI SZIMULÁCIÓK – EGYSÉGES FUTTATÁS")
    print("="*60)

    results = {}

    results["Szilárdságtan"] = run_mechanics()
    results["Hőtan"] = run_thermodynamics()
    results["Áramlástan"] = run_fluid_dynamics()
    results["Anyagátadástan"] = run_mass_transfer()
    results["Villamoságtan"] = run_electromagnetics()

    summarize_results(results)

if __name__ == "__main__":
    main()
