# Python code to check if k-th bit 
# of a given number is set or not 

def isKthBitSet(n,k):
    if(n &(1 << (k-1)))!=0:
        print("SET")
    else:
        print("NOT SET")
        
# Driver code
n = 5
k = 1 
isKthBitSet(n,k)
