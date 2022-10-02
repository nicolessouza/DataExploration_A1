import statistics

listnumbers = [1, 2, 4, 2, 6, 7, 3]

print("desvio padrao populacional =", statistics.pstdev(listnumbers))
print("desvio padrao amostral =", statistics.stdev(listnumbers))