import pandas as pd
import numpy as np
import statistics
from scipy import stats

data = pd.read_csv('Salary_Data.csv')

#print(data.head())

### médias

print("média salarial: ")
print("media aritmetica salario =", statistics.mean(data.Salary))
print("media aritmetica em anos =", statistics.mean(data.YearsExperience))


print ("media geometrica salario =",statistics.geometric_mean(data.Salary))
print ("media geometrica em anos =",statistics.geometric_mean(data.YearsExperience))


print ("media harmonica salario =",statistics.harmonic_mean(data.Salary))
print ("media harmonica em anos =",statistics.harmonic_mean(data.YearsExperience))

#utilizando anos de empresa como o peso de cada salário:
print("media aritmetica ponderada =",np.average(data.Salary, weights=data.YearsExperience))

### desvios-padrão
print("desvio padrao populacional salario =", statistics.pstdev(data.Salary))
print("desvio padrao amostral salario =", statistics.stdev(data.Salary))

print("desvio padrao populacional em anos =", statistics.pstdev(data.YearsExperience))
print("desvio padrao amostral em anos =", statistics.stdev(data.YearsExperience))

### variâncias
print("variancia populacional salario =", statistics.pvariance(data.Salary))
print("variancia amostral salario =", statistics.variance(data.Salary))

print("variancia populacional em anos =", statistics.pvariance(data.YearsExperience))
print("variancia amostral em anos =", statistics.variance(data.YearsExperience))

### coeficientes de correlação
print("Correlacao de Pearson =", statistics.correlation(data.Salary, data.YearsExperience))
print("Correlacao de Spearman =", stats.spearmanr(data.Salary, data.YearsExperience))
print("Correlacao de Kendall =", stats.kendalltau(data.Salary, data.YearsExperience))