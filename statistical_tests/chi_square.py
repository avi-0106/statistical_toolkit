import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Union

class ChiSquareTest:
    '''Chi-square test of independence with comprehensive diagnostics.'''
    
    def __init__(self, observed: Union[np.ndarray, pd.DataFrame, list[list]], handle_missing: str = "remove"):   
        # Convert and validate input
        self.observed = self._process_input(observed, handle_missing)
        self._validate_table()
        
    def _process_input(self, observed, handle_missing) -> np.ndarray:
        # Convert and clean input contingency table.
        # Handle pandas DataFrame
        if isinstance(observed, pd.DataFrame):
            arr = observed.to_numpy()
        else:
            arr = np.array(observed, dtype=float)
            
        # Handle missing values
        if np.isnan(arr).any():
            if handle_missing == "remove":
                arr = arr[~np.isnan(arr).any(axis=1)]
            elif handle_missing == "add_category":
                arr = np.where(np.isnan(arr), -1, arr)  # Special value for missing
            elif handle_missing == "error":
                raise ValueError("Missing values detected in contingency table")
                
        return arr.astype(int)

    def _validate_table(self):
        #Validate contingency table requirements.
        if self.observed.size == 0:
            raise ValueError("Contingency table is empty after missing value handling")
        if np.any(self.observed < 0):
            raise ValueError("Contingency table contains negative values")
        if self.observed.ndim != 2:
            raise ValueError("Contingency table must be 2-dimensional")

    def run_test(self) -> dict:
        #Execute chi-square test with effect size measures.
        chi2, p, dof, expected = stats.chi2_contingency(self.observed)
        
        # Calculate effect sizes
        n = np.sum(self.observed)
        phi = np.sqrt(chi2/n)
        cramers_v = np.sqrt(chi2/(n * (min(self.observed.shape)-1)))
        
        # Check expected counts
        if np.any(expected < 5):
            print("Warning: >20% of expected counts <5. Results may be unreliable")
            
        return {
            'chi2': chi2,
            'p_value': p,
            'dof': dof,
            'expected': expected,
            'phi': phi,
            'cramers_v': cramers_v
        }

    def plot_test(self):
        #Visualize observed vs expected frequencies.
        results = self.run_test()
        
        fig, ax = plt.subplots(1, 2, figsize=(14, 6))
        
        # Observed frequencies
        sns.heatmap(self.observed, 
                    annot=True, fmt="d",
                    cmap="Blues", ax=ax[0])
        ax[0].set_title("Observed Frequencies")
        
        # Expected frequencies
        sns.heatmap(results['expected'], 
                    annot=True, fmt=".1f",
                    cmap="Oranges", ax=ax[1])
        ax[1].set_title("Expected Frequencies")
        
        plt.suptitle(f"Chi-square Test Results (φ={results['phi']:.2f}, V={results['cramers_v']:.2f})")
        plt.tight_layout()
        plt.show()
