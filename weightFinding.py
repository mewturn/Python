## Milton Li, 2017
## 50.021 Artificial Intelligence

import numpy as np
import time
## Weights
w = np.zeros(3)

## List of arrays
x_list = []

## Lists of x1 and x2 and their expected value
x1_list = [0, 0, 1, 1]
x2_list = [0, 1, 0, 1]
y_list = [1, 1, -1, -1]

## Learning Rate
lr = 0.05

## Iteration count
iteration = 0

#################################### METHODS ###############################

## Adding an array to the list of arrays
def addArray(list, x1, x2, x0=-1):
    x = np.array([x0,x1,x2])
    list.append(x)
    
    return list
    
## The activation function g(z) given in the homework question
## g(z) <- z, if |z| < 1
## g(z) <- sign(z), otherwise

def activation(w, x):
    output = 0
    
    ## Element-wise product of w and x
    output = np.dot(w,x)
    
    # Check if the modulus of g(z) is between -1 and 1
    if output < 1 and output > -1:
        return output
   
    else:
        # Returns the sign of g(z) otherwise
        return np.sign(output)
        
#################################### METHODS ###############################


for i in range(len(x1_list)):
    x_list = addArray(x_list, x1_list[i], x2_list[i])

while True:
    ## Errors found in the Perceptron algorithm
    errors = 0
    
    for i in range(len(x1_list)):
        ## Calculate the predicted value 
        predict = activation(w, x_list[i])
        
        ## Check if predictions are correct, otherwise we change w accordingly:
        ## For positive ground truth, we want more positive weights: 
        ## w[t+1] = w[t] + lr * x  
        if y_list[i] == 1:
            if predict < 1:
                errors += 1      
                w += lr * x_list[i]
                iteration += 1
                break
                
        ## For negative ground truth: we want more negative weights:
        ## w[t+1] = w[t] - lr * x
        else:
            if predict > -1:
                errors += 1
                w -= lr * x_list[i]
                iteration += 1
                break

    ## When there are no more errors, we can output the solution and break loop
    if errors == 0:
        print("Possible weight classifier vector: ", w, "in", iteration, "changes.")
        break
