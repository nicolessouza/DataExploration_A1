import statistics

listnumbers = [1, 2, 4, 2, 6, 7, 3]

print("variancia populacional =", statistics.pvariance(listnumbers))
print("variancia amostral =", statistics.variance(listnumbers))