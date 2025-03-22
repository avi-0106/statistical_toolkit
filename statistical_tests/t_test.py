import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class TTest:
    # T-Test with visualization
    
    def __init__(self, data1, data2, population_mean=0, tail="two", alpha=0.05):
        self.data1 = data1
        self.data2 = data2
        self.population_mean = population_mean
        self.tail = tail
        self.alpha = alpha  
        self.p_value_two_tailed = None
        self.t_stat = None
        self.p_value = None
        self.dof = None

    def run_test(self):
        # Calculate t-test.
        if self.data2 is None:
            self._one_sample_ttest()
        else:
            self._two_sample_ttest()

        self.calculate_p_value()
        
        return {
            "t_statistic": self.t_stat,
            "p_value": self.p_value,
            "dof": self.dof,
            "alpha": self.alpha  
        }
    
    def one_sample_ttest(self):
        self.t_stat, p_value_two_tailed = stats.ttest_1samp(self.data1, popmean=self.population_mean)
        self.dof = len(self.data1) - 1
        self.p_value_two_tailed = p_value_two_tailed

    def two_sample_ttest(self):
        self.t_stat, p_value_two_tailed = stats.ttest_ind(self.data1, self.data2, equal_var=False)
        var1 = np.var(self.data1, ddof=1)
        var2 = np.var(self.data2, ddof=1)
        n1, n2 = len(self.data1), len(self.data2)

        numerator = (var1/n1 + var2/n2)**2
        denominator = ((var1**2)/(n1**2*(n1-1)) + (var2**2)/(n2**2*(n2-1)))
        self.dof = numerator / denominator
        self.p_value_two_tailed = p_value_two_tailed

    def calculate_p_value(self):
        if self.tail == "right":
            self.p_value = self.p_value_two_tailed / 2 if self.t_stat > 0 else 1 - (self.p_value_two_tailed / 2)
        elif self.tail == "left":
            self.p_value = self.p_value_two_tailed / 2 if self.t_stat < 0 else 1 - (self.p_value_two_tailed / 2)
        else:
            self.p_value = self.p_value_two_tailed

    def plot_test(self):
        #Visualize t-distribution with critical regions.
        plt.figure(figsize=(12, 6))
        x = np.linspace(-4, 4, 1000)
        y = stats.t.pdf(x, self.dof)
        
        # Plot t-distribution
        plt.plot(x, y, label=f"t-distribution (dof={self.dof:.1f})")
        plt.axvline(self.t_stat, color='r', linestyle='--', label=f"t-statistic ({self.t_stat:.2f})")
        
        # Calculate critical values
        if self.tail == "two":
            critical = stats.t.ppf(1 - self.alpha/2, self.dof)
            plt.fill_between(x[x <= -critical], y[x <= -critical], color='red', alpha=0.2, label=f'Rejection Region (α={self.alpha})')
            plt.fill_between(x[x >= critical], y[x >= critical], color='red', alpha=0.2)
        elif self.tail == "left":
            critical = stats.t.ppf(self.alpha, self.dof)
            plt.fill_between(x[x <= critical], y[x <= critical], color='red', alpha=0.2, label=f'Rejection Region (α={self.alpha})')
        else:
            critical = stats.t.ppf(1 - self.alpha, self.dof)
            plt.fill_between(x[x >= critical], y[x >= critical], color='red', alpha=0.2, label=f'Rejection Region (α={self.alpha})')
        
        plt.title(f"T-Test ({self.tail}-tailed)\np-value: {self.p_value:.4f}")
        plt.legend()
        plt.show()