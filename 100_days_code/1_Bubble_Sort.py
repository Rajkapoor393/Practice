# python program for implementation of bubble sort

def bubbleSort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        
        # last i elemests are already in place
        for j in range(0, n-i-1):
            
            # traverse the array from 0 to n-i-1
            # swap  if the next element found is greater
            # than the next element 
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
# driver code to test above

arr = [45,65,3,54,653,11,90]

bubbleSort(arr)

print("Sorted array is : ",arr)
# for i in range(len(arr)):
#     print("%d" %arr[i])