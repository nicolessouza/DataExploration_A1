import statistics
import numpy

listnumbers = [1, 2, 4, 2, 6, 7, 3]

#média aritmética
print("media aritmetica =",statistics.mean(listnumbers))
print("media aritmetica =",numpy.mean(listnumbers))

#média aritmética ponderada
notes = [10, 10, 5]
print("media aritmetica ponderada =",numpy.average(notes, weights=[0.3, 0.3, 0.4]))

#media geométrica
print ("media geomêtrica =",statistics.geometric_mean(listnumbers))

#media harmônica
print ("media harmonica =",statistics.harmonic_mean(listnumbers))
