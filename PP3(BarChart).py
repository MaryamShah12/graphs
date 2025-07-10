import matplotlib.pyplot as plt
import numpy as np

company=['Google','Amazon','Microsoft','Facebook', 'OpenAI']
revenue=[90,136,89,27,50]

xpos=np.arange(len(company))
plt.title("US Tech Stocks")
plt.bar(xpos,revenue, label='Revenue')
plt.xticks(xpos, company)
plt.ylabel("$Bln")
plt.legend()
plt.show()
