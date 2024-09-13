#!/usr/bin/env python3
#
# file: drawdawn calculator.py
# project: drowdawn_calculator
# created: 2024. 09. 13.
# author: Pjotr 975
# pjotr957@gmail.com

# FONTOS!
# A bemeneti adatok OHLC adatok, vesszővel elválasztott csv formátumban!

import csv

# CSV fájl beolvasása a Python beépített eszközeivel
file_path = 'your_data.csv'  # Add meg a fájl elérési útját
close_prices = []

# Az árfolyamok beolvasása
with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        close_prices.append(float(row['Close']))  # Tegyük fel, hogy 'Close' az oszlop neve

# Maximum és Átlagos Drawdown egyetlen ciklusban
def calculate_drawdowns(prices):
    peak = prices[0]
    max_drawdown = 0
    drawdowns_sum = 0

    for price in prices:
        if price > peak:
            peak = price
        drawdown = (peak - price) / peak
        drawdowns_sum += drawdown

        if drawdown > max_drawdown:
            max_drawdown = drawdown

    average_drawdown = drawdowns_sum / len(prices)

    return max_drawdown * 100, average_drawdown * 100  # Százalékos értékek

# Számítások elvégzése
max_dd, avg_dd = calculate_drawdowns(close_prices)

print(f"Maximum Drawdown: {max_dd:.2f}%")
print(f"Átlagos Drawdown: {avg_dd:.2f}%")

