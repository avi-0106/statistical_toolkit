# Documentation
The Statistical Toolkit package provides functions that simplify hypothesis testing and helps in interpretation by giving out-of-the-box solutions for creating great visualizations.

# Installation

#### 1. Clone or Fork the repository

```git clone https://github.com/avi-0106/statistical_toolkit.git```

#### 2. Install the Package in editable mode

```python -m pip install -e .```

#### 3. Verify installation

```python -c "import statistical_tests"```

If this runs without errors, then the package has been installed successfully.

# Usage

## ANOVA

#### Overview
The ANOVA class provides an implementation of Analysis of Variance (ANOVA), a statistical test used to compare means among multiple groups. It calculates the F-statistic, p-value, and effect size (eta squared), and provides visualizations to interpret the results.

#### Example
```
from statistical_tests import ANOVA

anova_test = ANOVA(group1, group2, group3, alpha=0.05)
```

#### Parameters
|Parameters | Type | Description |
| :------: | :----: | :--------:|
|```groups```| list| A list of numeric arrays representing different groups.|
|```alpha```| float |Significance level (default is 5%).|

#### Methods
```run_test()```
Computes the ANOVA test statistic and p-value. Returns a dictionary with:
*f_stat*: F-statistic
*p_value*: p-value for ANOVA test
*eta_squared*: Effect size measure
*alpha*: Significane level specified

```plot_test()```
Generates a visual representation of the standard normal distribution, the rejection region, and the Z-test statistic.

#### Interpretation
If p_value < alpha, reject the null hypothesis (atleast one group mean is significantly different).

## Chi-Squared Test

#### Overview
The Chi-Squared class provides takes a [contingency table](https://www.graphpad.com/guides/prism/latest/user-guide/contingency_table.htm) as an input and performs the chi-square test on the data provided.

#### Example
```
from statistical_tests import ChiSquareTest

chi_test = ChiSquareTest(contingency_table)
```

#### Parameters
|Parameters | Type | Description |
| :------: | :----: | :--------:|
|```handle_missing```| str, optional| "remove" (default): Remove rows with missing values.<br>"add_category": Treat missing values as a separate category.<br>"error": Raise an error if missing values are detected.|

#### Methods

```run_test()```
Returns a dictionary:
*chi2 (float)*: The computed chi-square statistic.
*p_value (float)*: The p-value of the test.
*dof (int)*: Degrees of freedom.
*expected (np.ndarray)*: Expected frequencies.
*phi (float)*: Phi coefficient.
*cramers_v (float)*: Cramér's V statistic.

```plot_test()```
Plots a heatmap that shows the observed and expected frequencies.


## Z-Test

#### Overview
The ZTest class provides functionality to perform one-sample and two-sample Z-tests, allowing statistical hypothesis testing for population means. It includes built-in visualization to display critical regions and test statistics on a standard normal distribution.

#### Example
```
from statistical_tests import ZTest

z_one_sample = ZTest(
    data1=setosa_sepal,
    population_mean=5.0,  # Hypothetical population mean
    sigma1=0.5,           # Known population std
    tail="two",
    alpha=0.05
)
```

#### Parameters
|Parameters | Type | Description |
| :------: | :----: | :--------:|
|```data1```| array-like| Sample data for the first group.|
|```data2```| array-like, optional (default: None) |Sample data for the second group (for a two-sample Z-test).|
|```population_mean```| float, optional (default: None)|Population mean for one-sample Z-test.|
|```sigma1```| float, optional (default: None)|Population standard deviation for data1
|```sigma2```| float, optional (default: None)| Population standard deviation for data2 (only for two-sample Z-test).|
|```tail```| str, optional (default: "two")|Specifies the type of test:<br>  "two": Two-tailed test <br> "left": Left-tailed test<br>"right": Right-tailed test|
|```alpha```| float, optional (default: 0.05)|Significance level (default is 5%).|

#### Methods
```run_test()```
Computes the Z-test statistic and p-value. Returns a dictionary with:
*z_statistic*: Computed Z-score.
*p_value*: Probability of observing the test result under the null hypothesis.
*alpha*: Chosen significance level.

```plot_test()```
Generates a visual representation of the standard normal distribution, the rejection region, and the Z-test statistic.

#### Interpretation
If p_value < alpha, reject the null hypothesis (significant difference exists).

If p_value >= alpha, fail to reject the null hypothesis (no significant difference).

## T-Test

#### Overview
The TTest class provides functionality to perform two-sample T-tests, allowing statistical hypothesis testing for population means when population variances are unknown. It includes built-in visualization to display critical regions and test statistics on a t-distribution.

#### Example
```
from statistical_tests import TTest

two_sample_ttest = TTest(
    data1=male_ages,
    data2=female_ages,
    tail="two",
    alpha=0.05
)
```

#### Parameters
|Parameters | Type | Description |
| :------: | :----: | :--------:|
|```data1```| array-like| Sample data for the first group.|
|```data2```| array-like, optional (default: None) |Sample data for the second group (for a two-sample Z-test).|
|```tail```| str, optional (default: "two")|Specifies the type of test:<br>  "two": Two-tailed test<br>  "left": Left-tailed test<br> "right": Right-tailed test|
|```alpha```| float, optional (default: 0.05)|Significance level (default is 5%).|

#### Methods
```run_test()```
Computes the Z-test statistic and p-value. Returns a dictionary with:
*t_statistic*: Computed T-score.
*p_value*: Probability of observing the test result under the null hypothesis.
*dof*: Degrees of freedom of the test.
*alpha*: Chosen significance level.

```plot_test()```
Generates a visual representation of the standard normal distribution, the rejection region, and the T-test statistic.

#### Interpretation
If p_value < alpha, reject the null hypothesis (significant difference exists).

If p_value >= alpha, fail to reject the null hypothesis (no significant difference).

# License

MIT License

Copyright (c) 2025 Abhishek Mishra, Siddhant Mihsra, Anirudh Parameswaran

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.