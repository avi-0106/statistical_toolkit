import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


class TTest:
    """T-Test with visualization"""

    def __init__(self, data1, data2, tail="two", alpha=0.05):
        self.data1 = data1
        self.data2 = data2
        self.tail = tail
        self.alpha = alpha  # Add alpha parameter
        self.t_stat = None
        self.p_value = None
        self.dof = None
        self._validate_table()

    def _validate_table(self):
        """Validate input data for the T-Test."""
        assert isinstance(
            self.data1, (list, np.ndarray)
        ), "data1 must be a list or NumPy array."
        assert isinstance(
            self.data2, (list, np.ndarray)
        ), "data2 must be a list or NumPy array."
        assert len(self.data1) > 1, "data1 must contain more than one data point."
        assert len(self.data2) > 1, "data2 must contain more than one data point."
        assert all(
            isinstance(x, (int, float, np.number)) for x in self.data1
        ), "data1 contains non-numeric values."
        assert all(
            isinstance(x, (int, float, np.number)) for x in self.data2
        ), "data2 contains non-numeric values."
        assert self.tail in [
            "two",
            "left",
            "right",
        ], "tail must be 'two', 'left', or 'right'."
        assert 0 < self.alpha < 1, "alpha must be a probability value between 0 and 1."

    def run_test(self):
        """Calculate Welch's t-test."""
        self.t_stat, self.p_value = stats.ttest_ind(
            self.data1, self.data2, equal_var=False
        )
        # Manually calculate degrees of freedom (Welch-Satterthwaite)
        var1 = np.var(self.data1, ddof=1)
        var2 = np.var(self.data2, ddof=1)
        n1, n2 = len(self.data1), len(self.data2)
        self.dof = (var1 / n1 + var2 / n2) ** 2 / (
            (var1**2) / (n1**2 * (n1 - 1)) + (var2**2) / (n2**2 * (n2 - 1))
        )

        return {
            "t_statistic": self.t_stat,
            "p_value": self.p_value,
            "dof": self.dof,
            "alpha": self.alpha,  # Include alpha in results
        }

    def plot_test(self):
        """Visualize t-distribution with critical regions."""
        plt.figure(figsize=(12, 6))
        x = np.linspace(-4, 4, 1000)
        y = stats.t.pdf(x, self.dof)

        # Plot t-distribution
        plt.plot(x, y, label=f"t-distribution (dof={self.dof:.1f})")
        plt.axvline(
            self.t_stat,
            color="r",
            linestyle="--",
            label=f"t-statistic ({self.t_stat:.2f})",
        )

        # Calculate critical values
        if self.tail == "two":
            critical = stats.t.ppf(1 - self.alpha / 2, self.dof)
            plt.fill_between(
                x[x <= -critical],
                y[x <= -critical],
                color="red",
                alpha=0.2,
                label=f"Rejection Region (α={self.alpha})",
            )
            plt.fill_between(x[x >= critical], y[x >= critical], color="red", alpha=0.2)
        elif self.tail == "left":
            critical = stats.t.ppf(self.alpha, self.dof)
            plt.fill_between(
                x[x <= critical],
                y[x <= critical],
                color="red",
                alpha=0.2,
                label=f"Rejection Region (α={self.alpha})",
            )
        else:
            critical = stats.t.ppf(1 - self.alpha, self.dof)
            plt.fill_between(
                x[x >= critical],
                y[x >= critical],
                color="red",
                alpha=0.2,
                label=f"Rejection Region (α={self.alpha})",
            )

        plt.title(f"T-Test ({self.tail}-tailed)\np-value: {self.p_value:.4f}")
        plt.legend()
        plt.show()
