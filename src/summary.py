# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 13:17:50 2025

@author: Laszlo
"""

# 7. 📊 summary.py – Összegző táblázat modul

def summarize_results(results):
    print("\n" + "="*60)
    print("SPIRÁLIS MÉRNÖKI ALAP – NUMERIKUS EREDMÉNYEK ÖSSZEFOGLALÓ")
    print("="*60)

    for discipline, data in results.items():
        print(f"\n{discipline}:")
        for key, value in data.items():
            if isinstance(value, float):
                formatted = f"{value:.3f}" if abs(value) < 1e3 else f"{value:.2e}"
            else:
                formatted = str(value)
            print(f"  {key}: {formatted}")

    print("\n" + "="*60)
    print("KÖVETKEZTETÉS: A spirális koordinátarendszer egyesíti a mérnöki területeket")
    print("és lehetővé teszi az egységes matematikai leírást.")
    print("="*60)