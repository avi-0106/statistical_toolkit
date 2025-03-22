from setuptools import setup, find_packages

setup(
    name="statistical_tests", 
    version="0.1.0", 
    author="ABHISHEK MISHRA",
    author_email="abhishekmishra0106@gmail.com",
    description="This Package is an implementation of multiple Statistical Tests e.g. Z-TEST, T-TEST, ANOVA, CHI SQUARE.",
    url="https://github.com/yourusername/my_project", 
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "scipy",
        "matplotlib",
        "seaborn",
        "statsmodels"
    ],
    license="MIT",
    platforms="OS Independent"
)