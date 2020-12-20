# Python code to check if k-th bit 
# of a given number is set or not 

def powerOfTwo(n):
    if (n and (not (n &(n-1)))):
        print("The number is a power of 2")
    else:
        print("The number is not a power of 2")
        
# Driver code
n = 32
powerOfTwo(n)
