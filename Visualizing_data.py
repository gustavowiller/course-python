# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt

years = range(1950,2011,10)
gdp = [300.2,543.3,1075.9,2862.5,5979.6,10289.7,14958.3]

print years
plt.plot(years,gdp,color='green',marker='o',linestyle='solid')

plt.title("Nominal GDP")
plt.ylabel("Billions of $")
plt.show()
