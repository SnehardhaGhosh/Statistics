import numpy as np
import statistics
import math

ages=[21,23,32,45,21,56,47,37,39,49,38,100]

print(np.var(ages)) #uses population variance formula
print(statistics.variance(ages)) #uses sample variance formula

def variance(data):
    n=len(ages)
   #mean
    mean=sum(ages)/n
    print(mean)
  #variance
    var1=[(x-mean) **2 for x in data]
    variance=sum(var1)/(n-1)
    return variance

standard_deviation=math.sqrt(statistics.variance(ages))


print(variance(ages))
print(standard_deviation)
