def fibonacci(n, list):
    prev = 0
    curr = 1
    list.append(prev)
    list.append(curr)
    
    if n == 0:
        return []
    elif n == 1:
        return [0]
    
    for i in range(n-2):
        next = prev + curr
        list.append(next)
        prev, curr = curr, next
        
    return list
    
if __name__ == "__main__":
    while True:
        try:
            n = input("Please enter the number of integers you want to see in the Fibonacci sequence: ")
            print(fibonacci(int(n), []))
        except Exception as e:
            print(e)
    