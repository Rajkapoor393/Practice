def count(s,c):
    
    # initialise a count variable
    res = 0
    for i in range(len(s)):
        
        if (s[i]== c):
            res +=1
    return res
# driver code
str = input("Enter the string you want ")
c = input("Enter the character for search ")
print(count(str,c))
