import matplotlib.pyplot as plt
import numpy as np

#create an evenly spaced array
t = np.arange(0.0,5.0,0.2)

#add axes labels and a title
plt.xlabel('numbers')
plt.ylabel('more numbers')
plt.title('Look, a title!')

#plot red dashes, blue squares, and green triangles
plt.plot(t,t,'r--',t,t**2,'bs',t, t**3, 'g^')

#show your plot
plt.show()
