import matplotlib.pyplot as plt
import numpy as np

def y(x):
  return (-0.1 + 0.3*x - 0.7*x*x + 0.1*x*x*x)

#params[0]=alpha, params[1]=beta, params[2]=gamma, params[3]=delta
def y_hat(params, x):
  return (params[0] + params[1]*x + params[2]*x*x + params[3]*x*x*x)

def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

#plot ground truth
t1 = np.arange(-1.0, 1.0, 0.1)
plt.figure()
plt.title("Ground truth")
plt.plot(t1, y(t1))

#plot function
t1 = np.arange(-5.0, 5.0, 0.1)
plt.figure()
plt.title("Function")
plt.plot(t1, y_hat([1,1,1,1],t1))


Gene = np.array([0,1,0,0])

Alpha_values = np.array([Gene[0]])
Beta_values = np.array([Gene[0]])
for i in range(100):
    Alpha_values = np.append(Alpha_values,[Alpha_values[i]+np.random.normal(0, 0.1)])
    Beta_values = np.append(Beta_values,[Alpha_values[i]+np.random.normal(0, 0.1)])

plt.figure()
plt.subplot(211)
plt.hist(Alpha_values)
plt.title("Alpha")
plt.subplot(212)
plt.title("Beta")
plt.hist(Beta_values)

Population = np.random.normal(0, 1, (100,4))
plt.figure()
plt.subplot(211)
plt.hist(Population[:,1])
plt.title("Beta")
plt.subplot(212)
plt.title("Gamma")
plt.hist(Population[:,2])

avg_loss = np.array([])
for gen in range(100):
    test_values = np.random.uniform(-1.0,1.0,10)
    loss = np.array([])
    for i in range(100):
        err = rmse(y(test_values),y_hat(Population[i],test_values))
        loss = np.append(loss,[err])

    #append loss to population
    Population = np.column_stack((Population,loss))
    #sort based on loss using lambda func
    Population = np.array(sorted(Population, key=lambda x: x[4]))
    #store the average loss of best 10
    avg_loss = np.append(avg_loss,np.mean(Population[:10,4]))
    #only keep best 10
    Population = Population[:10,:4]

    for i in range(9):
        for _ in range(10):
            #slow mutation over time for better convergene
            mutation_rate = 1/(gen+1)
            Population = np.append(Population,Population[i]+np.random.normal(0, mutation_rate, (1,4)), axis=0)

#plot the loss over generations
plt.figure()
plt.plot(avg_loss)
plt.title('bestfit = {}'.format(Population[0]))
plt.xlabel('generations')
plt.ylabel('loss')

#print best fit
print(Population[0])

plt.show()
