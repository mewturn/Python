import tensorflow as tf
import matplotlib.pyplot as plt
from random import uniform
import numpy as np

## Placeholders for x and y variables
x = tf.placeholder("float", None)
y = tf.placeholder("float", None)

## Output = (x^3)*(y^2) - 7(x^2)*y + x - 12
output = (x ** 3) * (y ** 2) - 7 * (x **2) * y + x - 12

## Number of points to plot
n = 1000
  
## Generates the feed dictionary as input Tensors x, y with a specified distribution
def feedDictionary(x, y, distribution = "Random"):
    # Generate y value
    gen2 = 0.2
    
    # Generate x value based on the required distribution
    if distribution == "Gamma":
        gen1 = np.random.gamma(1)
        
    elif distribution == "Cauchy":
        gen1 = np.random.standard_cauchy()
    
    elif distribution == "Gaussian":
        u = 0
        s = 1
        gen1 = np.random.normal(u, s) 
        
    else:
        gen1 = uniform(-1, 1)
    
    fd = {x: gen1, y: gen2} 
    
    return fd
    
def run():
    with tf.Session() as session:
        for i in range(n):
            fd = feedDictionary(x, y, "Gaussian")
            result = session.run(output, feed_dict=fd)
            
            ## We only want to plot for -1 < x < 1
            if fd.get(x) > -1 and fd.get(x) < 1: 
                plt.plot(fd.get(x), result, "bo")
                
        plt.show()
        
if __name__ == "__main__":
    run()
