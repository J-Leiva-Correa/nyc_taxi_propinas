import matplotlib.pyplot as plt
from src.visualization.plots import plot_f1_scores


def plot_f1_scores(resultados, save_path=None):
   
    meses = [r['mes'] for r in resultados]
    f1_scores = [r['f1_score'] for r in resultados]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(meses, f1_scores, color='skyblue')
    plt.title("F1-score por mes")
    plt.xlabel("Mes")
    plt.ylabel("F1-score")
    plt.ylim(0, 1.1)
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    # Mostrar los valores arriba de las barras
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.02, f"{yval:.2f}", ha='center')

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
        print(f"📸 Imagen guardada en: {save_path}")
    else:
        plt.show()
