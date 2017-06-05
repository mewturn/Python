### Original Questions: http://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
from copy import deepcopy

## Problem 1
## Write three functions that compute the sum of the numbers in a given list using a for-loop, a while-loop, and recursion.

## For Loop
def sum_for(list):
    output = 0
    for number in list:
        output += number
        
    return output

## While Loop
def sum_while(list):
    output = 0
    thisList = deepcopy(list)
    while len(thisList) != 0:
        output += thisList[0]
        thisList.remove(thisList[0])
        
    return output

## Recursion         
def sum_recur(input, list):
    if len(list) == 0:
        return input
    else:
        return sum_recur(input + list[0], list[1:])
        
        
## Problem 2
## Write a function that combines two lists by alternatingly taking elements. For example: given the two lists [a, b, c] and [1, 2, 3], the function should return [a, 1, b, 2, c, 3].
def combine(list1, list2):
    output = []
    ## Check which list is longer
    if len(list1) > len(list2):
        length = len(list1)
    else:
        length = len(list2)
        
    for i in range(length):
        ## If any of the indices are out of range, we add a "Null" to the output list
        if i > len(list1) - 1:
            output.append("Null")
            output.append(list2[i])
        elif i > len(list2) - 1:
            output.append(list1[i])
            output.append("Null")
        else:
            output.append(list1[i])
            output.append(list2[i])
    return output
    
## Problem 3
## Write a function that computes the list of the first n Fibonacci numbers. By definition, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two. 
## As an example, here are the first 10 Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.
def fibonacci(n):
    ## Initialise first number: 0 and second number: 1
    prev = 0
    current = 1
    
    ## Output list
    output = [0, 1]
    
    ## Since we already have two numbers at the start, we only need n-2 more
    for i in range(n-2):
        next = prev + current
        output.append(next)
        prev = current
        current = next
        
    return output
    
## Problem 4
## Write a function that given a list of non negative integers, arranges them such that they form the largest possible number. 
## For example, given [50, 2, 1, 9], the largest formed number is 95021.
def largestnumber(list):
    string = ""
    for i in list:
        string += str(i)
    ascending = "".join(sorted(string))
    
    return int(ascending[::-1])


        
    