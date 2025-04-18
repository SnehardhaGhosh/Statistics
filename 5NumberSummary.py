import numpy as np
import seaborn as sea
import matplotlib.pyplot as plt

ages=[21,23,32,45,21,56,47,37,39,49,38,100]

# minimum of dataset
# quartile 25%
# median
# quartile 75%
# maximum of dataset

q1,q3=np.percentile(ages,[25,75])
print(q1,q3)

Iqr=q3-q1
print(Iqr)

lower=q1-(1.5*Iqr)
higher=q3+(1.5*Iqr)
print(lower, higher)

sea.boxplot(ages)
plt.show()
