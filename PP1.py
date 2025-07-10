import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7]
y=[50,51,52,48,47,49,46]

plt.xlabel("Day")
plt.ylabel("Temperature")
#plt.plot(y, "r+") # ditto, but with red plusses.

# alpha is used for transparency of the line.

#plt.plot(x,y, color='green', linewidth=5,alpha=0.4)
#different formats of styling the graph dotted line in --
#plt.plot(x,y, "d--")

plt.plot(x,y, )
plt.show()