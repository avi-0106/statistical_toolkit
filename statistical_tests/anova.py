import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class ANOVA:
    """ANOVA implementation with boxplots, violin + swarmplot overlay, and bar chart visualization."""

    def __init__(self, *groups, alpha=0.05):
        self.groups = groups
        self.alpha = alpha
        self.f_stat = None
        self.p_value = None
        self.eta_sq = None

    def run_test(self):
        self.anova()                                         #Calculate ANOVA statistics and effect size.

        return {
            "f_stat": self.f_stat,
            "p_value": self.p_value,
            "eta_squared": self.eta_sq,
            "alpha": self.alpha
        }
    
    def anova(self):
        self.f_stat, self.p_value = stats.f_oneway(*self.groups)        #Calculate ANOVA statistics

        # Calculate eta squared (effect size)
        grand_mean = np.mean(np.concatenate(self.groups))
        ss_between = sum([len(g) * (np.mean(g) - grand_mean) ** 2 for g in self.groups])
        ss_total = sum([np.sum((g - grand_mean) ** 2) for g in self.groups])
        self.eta_sq = ss_between / ss_total

    def plot_test(self):
        
        plt.figure(figsize=(18, 6))

        # ===========================
        # Subplot 1: Boxplot
        # ===========================
        ax1 = plt.subplot(1, 3, 1)
        sns.boxplot(data=self.groups, palette="Pastel1", width=0.4, ax=ax1)
        ax1.set_title("Boxplot")
        ax1.set_xticks(range(len(self.groups)))
        ax1.set_xticklabels([f"Group {i+1}" for i in range(len(self.groups))])
        ax1.grid(axis='y', linestyle='--', alpha=0.7)

        # ===========================
        # Subplot 2: Violin + Swarmplot (Overlayed)
        # ===========================
        ax2 = plt.subplot(1, 3, 2)
        sns.violinplot(
            data=self.groups,
            palette="muted",
            inner=None,  
            ax=ax2,
            alpha=0.7   
        )
        sns.swarmplot(
            data=self.groups,
            palette="dark",
            edgecolor="black",
            size=5,
            alpha=0.9,
            ax=ax2
        )
        ax2.set_title("Violin + Swarmplot")
        ax2.set_xticks(range(len(self.groups)))
        ax2.set_xticklabels([f"Group {i+1}" for i in range(len(self.groups))])
        ax2.grid(axis='y', linestyle='--', alpha=0.7)

        # ===========================
        # Subplot 3: Bar Chart (Mean ± SEM)
        # ===========================
        ax3 = plt.subplot(1, 3, 3)
        means = [np.mean(g) for g in self.groups]
        sems = [stats.sem(g) for g in self.groups]
        ax3.bar(range(len(self.groups)), means, yerr=sems, capsize=5,
                color=sns.color_palette("Pastel1", len(self.groups)))
        ax3.set_title("Bar Chart (Mean ± SEM)")
        ax3.set_xticks(range(len(self.groups)))
        ax3.set_xticklabels([f"Group {i+1}" for i in range(len(self.groups))])
        ax3.grid(axis='y', linestyle='--', alpha=0.7)

        # Effect size & stats annotation
        plt.figtext(
            0.90, 0.92,
            f"η² = {self.eta_sq:.2f}\nF = {self.f_stat:.2f}\np = {self.p_value:.4f}",
            bbox=dict(facecolor='white', alpha=0.9),
            fontsize=12
        )

        plt.suptitle(f"ANOVA Results (α = {self.alpha})", fontsize=16, y=0.98)
        plt.tight_layout()
        plt.show()
