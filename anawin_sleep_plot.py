"""anawin sleep plot"""
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import numpy as np

def main() -> None:
    """anawin sleep plot"""
    df = pd.read_csv("./data/anawin_sleep_data_ex.csv")
    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
    fig.tight_layout(pad=4.0)
    energy_ax: plt.Axes = ax[0, 0]
    energy_ax.set_title("Efficiency")
    energy_ax.set_xlabel("days")
    energy_ax.set_ylabel("percent")
    energy = df["energy"]
    x = np.arange(1, energy.size + 1)
    energy_y = [int(e.replace("%", "")) for e in energy]
    energy_ax.plot(x, energy_y, label="efficiency", marker="o", markersize=4)
    energy_ax.legend()
    energy_ax.set_yticks([40, 50, 60, 70, 80, 90, 100])
    energy_ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    energy_ax.set_xticks(x[x % 2 == 1])
    energy_ax.grid(True, linewidth=0.3, linestyle="--")
    
    owe: plt.Axes = ax[0, 1]
    owe.set_title("Deposit & Withdraw Sleep Time")
    owe.set_xlabel("days")
    owe.set_ylabel("deposit > withdraw")
    owe_y = df["owe"]
    owe.plot(x, owe_y, label="deposit-withdraw hour", marker="o", markersize=4, linewidth=1, color="mediumseagreen")
    owe.set_yticks(np.arange(-3, 11, 2))
    
    total = [owe_y[0]]
    for i in range(1, len(owe_y)):
        total.append(total[i - 1] + owe_y[i])
    owe.plot(x, total, label="total hours", linewidth=2)
    owe.plot(x, [0.17] * len(x), label="average=1.17", linestyle=":")
    owe.legend()
    owe.grid(True, linewidth=0.3, linestyle="--")
    owe.set_xticks(np.arange(1, len(x) + 1, 3))
    
    symtoms_jul: plt.Axes = ax[1, 0]
    symtoms_jul.set_title("Symptoms July")
    july_st = df[df["month"] == "July"]
    july_symtoms = july_st["symptom"].tolist()
    july_count = [july_symtoms.count("-"), july_symtoms.count("S"), 
                  july_symtoms.count("N"), july_symtoms.count("F"), 
                  july_symtoms.count("H"), july_symtoms.count("M")]
    symtoms_labels = ["Fine", "Sleepy", "Nap", "Brain Fog", "Headache", "Migraine"]
    symtoms_colors = ["lightgreen", "khaki", "sandybrown", "tomato", "darkslateblue", "brown"]
    symtoms_explodes = [0.05, 0.04, 0.02, 0, 0, 0]
    symtoms_jul.pie(july_count,
                    labels=symtoms_labels,
                    colors=symtoms_colors,
                    autopct=lambda p: '{:.1f}%'.format(p) if p > 0 else '',
                    explode=symtoms_explodes,
                    shadow=True)
    
    symtoms_aug: plt.Axes = ax[1, 1]
    symtoms_aug.set_title("Symptoms August")
    august_st = df[df["month"] == "August"]
    august_symtoms = august_st["symptom"].tolist()
    august_count = [august_symtoms.count("-"), august_symtoms.count("S"),
                    august_symtoms.count("N"), august_symtoms.count("F"),
                    august_symtoms.count("H"), august_symtoms.count("M")]
    symtoms_aug.pie(august_count,
                     labels=symtoms_labels,
                     colors=symtoms_colors,
                     autopct=lambda p: '{:.1f}%'.format(p) if p > 0 else '',
                     explode=symtoms_explodes,
                     shadow=True)
    
    plt.show()

main()
