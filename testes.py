import pandas as pd
import numpy as np
import statistics
from scipy import stats

data = pd.read_csv('Salary_Data.csv')

### coeficientes de correlação
print("Correlacao de Pearson =", statistics.correlation(data.Salary, data.YearsExperience))
print("Correlacao de Spearman =", stats.spearmanr(data.Salary, data.YearsExperience))
print("Correlacao de Kendall =", stats.kendalltau(data.Salary, data.YearsExperience))