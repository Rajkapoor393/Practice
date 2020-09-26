# Python program to find equilibrium index of an bytearray

# Function to find the equilibrium index
def equilibrium(arr):
    
    # finding the sum of whole array 
    total_sum = sum(arr)
    leftsum = 0
    
    for i, num in enumerate(arr):
        
        # total_sum is now right sum 
        # for index i 
        total_sum -= num 
        
        if leftsum== total_sum:
            return i 
        leftsum += num 
        
        # If no equilibrium index found, 
        # then return -1
        
    return -1
    
# driver code 
arr = [-7, 1,5,2,-4,3,0]
print(equilibrium(arr))