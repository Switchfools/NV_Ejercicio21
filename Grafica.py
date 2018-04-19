import numpy as np
import matplotlib.pylab as plt
Sol=np.genfromtxt('step.txt')
Sol2=np.genfromtxt('gauss.txt')
index=Sol[:,0]==0.49
index2=Sol2[:,0]==0.49
plt.plot(Sol[index,1],Sol[index,2])
plt.savefig('escalon.png')
plt.figure()
plt.plot(Sol2[index2,1],Sol2[index2,2])
plt.savefig('gaussiana no lineal.png')
