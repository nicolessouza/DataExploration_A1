import statistics
from scipy import stats


listnumbers1 = [1, 2, 4, 2, 6, 7, 3]
listnumbers2 = [3, 1, 7, 3, 2, 8, 2]

print("Correlacao de Pearson =", statistics.correlation(listnumbers1, listnumbers2))
print("Correlacao de Spearman =", stats.spearmanr(listnumbers1, listnumbers2))
print("Correlacao de Kendall =", stats.kendalltau(listnumbers1, listnumbers2))