import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []
for i in range(30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)


#For different plots
#plt.figure('lin')
#plt.clf()
#plt.xlabel('sample points')
#plt.ylabel('Linear function')
#plt.title('Linear')
#plt.ylim(0, 1000)
#plt.plot(mySamples, myLinear)
#plt.figure('quad')
#plt.clf()
#plt.xlabel('sample points')
#plt.ylabel('Quadratic function')
#plt.title('Quadratic')
#plt.ylim(0, 1000)
#plt.plot(mySamples, myQuadratic)
#plt.figure('cube')
#plt.clf()
#plt.xlabel('sample points')
#plt.ylabel('Cubic function')
#plt.title('Cubic')
#plt.ylim(0, 1000)
#plt.plot(mySamples, myCubic)
#plt.figure('exp')
#plt.clf()
#plt.xlabel('sample points')
#plt.ylabel('Exponential function')
#plt.title('Exponential')
#plt.ylim(0, 1000)
#plt.plot(mySamples, myExponential)


#For 2 in 1 plots
#plt.figure('lin quad')
#plt.clf()
#plt.subplot(211)
#plt.ylim(0, 900)
#plt.plot(mySamples, myLinear,'b', label = 'Linear', linewidth = '2.0')
#plt.subplot(212)
#plt.ylim(0, 900)
#plt.plot(mySamples, myQuadratic,'r', label = 'Quadratic', linewidth = '3.0')
#plt.legend(loc = 'upper left')
#plt.figure('cube exp')
#plt.clf()
#plt.subplot(121)
#plt.ylim(0, 140000)
#plt.plot(mySamples, myCubic,'g', label = 'Cubic', linewidth = '4.0')
#plt.subplot(122)
#plt.ylim(0, 140000)
#plt.plot(mySamples, myExponential,'r', label = 'Exponential', linewidth = '5.0')
#plt.legend()
#
#plt.figure('lin quad')
#plt.title('Linear vs Quadratic')
#plt.figure('cube exp')
#plt.title('Cubic vs Exponential')
