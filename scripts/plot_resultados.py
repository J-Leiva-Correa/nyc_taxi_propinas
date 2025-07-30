import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.visualization.plots import plot_f1_scores

# Resultados de ejemplo (puedes copiarlos de evaluate_months)
resultados = [
    {'mes': '2020-01', 'f1_score': 0.9593},
    {'mes': '2020-02', 'f1_score': 0.8238},
    {'mes': '2020-04', 'f1_score': 0.6606},
]

plot_f1_scores(resultados, save_path="f1_por_mes.png")
