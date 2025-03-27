# Documentation - statistical_toolkit
The Statistical Toolkit package provides functions, visualizations and automatic data cleaning pipelines which help simplify hypothesis testing by directly implementing statistical methods with good visualizations, making it accessible for anyone.

## ANOVA

### Overview
The ANOVA class provides an implementation of Analysis of Variance (ANOVA), a statistical test used to compare means among multiple groups. It calculates the F-statistic, p-value, and effect size (eta squared), and provides visualizations to interpret the results.

### Usage
```
from statistical_tests import ANOVA
```

### Parameters
|Parameters | Type | Description |
| :------: | :----: | :--------:|
|```groups```| list| A list of numeric arrays representing different groups.|
|```alpha```| float |Significance level (default is 5%).|

### Methods
```run_test()```
Computes the ANOVA test statistic and p-value. Returns a dictionary with:
*f_stat*: F-statistic
*p_value*: p-value for ANOVA test
*eta_squared*: Effect size measure
*alpha*: Significane level specified

```plot_test()```
Generates a visual representation of the standard normal distribution, the rejection region, and the Z-test statistic.

### Interpretation
If p_value < alpha, reject the null hypothesis (atleast one group mean is significantly different).

## Chi-Squared Test

### Overview
The Chi-Squared class provides an implementation of chi-square test, a statistical test used to compare means among multiple groups. It calculates the F-statistic, p-value, and effect size (eta squared), and provides visualizations to interpret the results.

### Usage
```
from statistical_tests import ChiSquareTest
```

### Interpretation
If p_value < alpha, reject the null hypothesis (atleast one group mean is significantly different).



## Z-Test

### Overview
The ZTest class provides functionality to perform one-sample and two-sample Z-tests, allowing statistical hypothesis testing for population means. It includes built-in visualization to display critical regions and test statistics on a standard normal distribution.

### Usage
```
from statistical_tests import ZTest
```

### Parameters
|Parameters | Type | Description |
| :------: | :----: | :--------:|
|```data1```| array-like| Sample data for the first group.|
|```data2```| array-like, optional (default: None) |Sample data for the second group (for a two-sample Z-test).|
|```population_mean```| float, optional (default: None)|Population mean for one-sample Z-test.|
|```sigma1```| float, optional (default: None)|Population standard deviation for data1
|```sigma2```| float, optional (default: None)| Population standard deviation for data2 (only for two-sample Z-test).|
|```tail```| str, optional (default: "two")|Specifies the type of test:<br>  "two": Two-tailed test <br> "left": Left-tailed test<br>"right": Right-tailed test|
|```alpha```| float, optional (default: 0.05)|Significance level (default is 5%).|

### Methods
```run_test()```
Computes the Z-test statistic and p-value. Returns a dictionary with:
*z_statistic*: Computed Z-score.
*p_value*: Probability of observing the test result under the null hypothesis.
*alpha*: Chosen significance level.

```plot_test()```
Generates a visual representation of the standard normal distribution, the rejection region, and the Z-test statistic.

### Interpretation
If p_value < alpha, reject the null hypothesis (significant difference exists).

If p_value >= alpha, fail to reject the null hypothesis (no significant difference).

