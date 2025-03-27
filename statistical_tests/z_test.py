import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


class ZTest:
    """Z-Test with visualization"""

    def __init__(
        self,
        data1,
        data2=None,
        population_mean=None,
        sigma1=None,
        sigma2=None,
        tail="two",
        alpha=0.05,
    ):
        self.data1 = data1
        self.data2 = data2
        self.population_mean = population_mean
        self.sigma1 = sigma1
        self.sigma2 = sigma2
        self.tail = tail
        self.alpha = alpha
        self.z_stat = None
        self.p_value = None
        self._validate_table()

    def _validate_table(self):
        """Validate input data for the Z-Test."""
        assert isinstance(
            self.data1, (list, np.ndarray)
        ), "data1 must be a list or NumPy array."
        assert len(self.data1) > 1, "data1 must contain more than one data point."
        assert all(
            isinstance(x, (int, float, np.number)) for x in self.data1
        ), "data1 contains non-numeric values."

        if self.data2 is not None:
            assert isinstance(
                self.data2, (list, np.ndarray)
            ), "data2 must be a list or NumPy array."
            assert len(self.data2) > 1, "data2 must contain more than one data point."
            assert all(
                isinstance(x, (int, float, np.number)) for x in self.data2
            ), "data2 contains non-numeric values."

        if self.population_mean is not None:
            assert isinstance(
                self.population_mean, (int, float, np.number)
            ), "population_mean must be a numeric value."

        if self.sigma1 is not None:
            assert (
                isinstance(self.sigma1, (int, float, np.number)) and self.sigma1 > 0
            ), "sigma1 must be a positive number."

        if self.sigma2 is not None:
            assert (
                isinstance(self.sigma2, (int, float, np.number)) and self.sigma2 > 0
            ), "sigma2 must be a positive number."

        assert self.tail in [
            "two",
            "left",
            "right",
        ], "tail must be 'two', 'left', or 'right'."
        assert 0 < self.alpha < 1, "alpha must be a probability value between 0 and 1."

    def run_test(self):
        # Perform Z-Test calculations

        if self.data2 is not None:
            self.two_sample_ztest()  # Two-sample Z-test
        else:
            self.one_sample_ztest()  # One-sample Z-test

        # Calculate p-value
        self.calculate_p_value()

        return {
            "z_statistic": self.z_stat,
            "p_value": self.p_value,
            "alpha": self.alpha,
        }

    def one_sample_ztest(self):
        mean1 = np.mean(self.data1)
        n1 = len(self.data1)
        if self.sigma1 is None:
            self.sigma1 = np.std(self.data1, ddof=1)
        standard_error = self.sigma1 / np.sqrt(n1)
        self.z_stat = (mean1 - self.population_mean) / standard_error

    def two_sample_ztest(self):
        mean1 = np.mean(self.data1)
        mean2 = np.mean(self.data2)
        n1 = len(self.data1)
        n2 = len(self.data2)
        if self.sigma1 is None:
            self.sigma1 = np.std(self.data1, ddof=1)
        if self.sigma2 is None:
            self.sigma2 = np.std(self.data2, ddof=1)
        standard_error = np.sqrt((self.sigma1**2 / n1) + (self.sigma2**2 / n2))
        self.z_stat = (mean1 - mean2) / standard_error

    def calculate_p_value(self):
        if self.tail == "right":
            self.p_value = 1 - stats.norm.cdf(self.z_stat)  # right
        elif self.tail == "left":
            self.p_value = stats.norm.cdf(self.z_stat)  # left
        else:
            self.p_value = 2 * (1 - stats.norm.cdf(abs(self.z_stat)))  # two

    def plot_test(self):
        # Visualize Z-test with critical regions and test statistic.

        plt.figure(figsize=(12, 6))
        x = np.linspace(-4, 4, 1000)
        y = stats.norm.pdf(x)

        # Plot standard normal distribution
        plt.plot(x, y, label="Standard Normal Distribution")

        # Shade critical regions
        if self.tail == "two":
            critical_value = stats.norm.ppf(1 - self.alpha / 2)
            plt.fill_between(
                x,
                y,
                where=(x <= -critical_value) | (x >= critical_value),
                color="red",
                alpha=0.2,
                label=f"Rejection Region (α={self.alpha})",
            )
        elif self.tail == "left":
            critical_value = stats.norm.ppf(self.alpha)
            plt.fill_between(
                x,
                y,
                where=(x <= critical_value),
                color="red",
                alpha=0.2,
                label=f"Rejection Region (α={self.alpha})",
            )
        else:
            critical_value = stats.norm.ppf(1 - self.alpha)
            plt.fill_between(
                x,
                y,
                where=(x >= critical_value),
                color="red",
                alpha=0.2,
                label=f"Rejection Region (α={self.alpha})",
            )

        # Plot test statistic
        plt.axvline(
            self.z_stat,
            color="blue",
            linestyle="--",
            label=f"Z-statistic ({self.z_stat:.2f})",
        )

        plt.title(
            f"Z-Test ({self.tail}-tailed)\nZ-statistic: {self.z_stat:.2f}, p-value: {self.p_value:.4f}"
        )
        plt.xlabel("Z-value")
        plt.ylabel("Probability Density")
        plt.legend()
        plt.grid(True)
        plt.show()
