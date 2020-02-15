# Program to count the occurance of given character in a given string

def count(s,c):
    
    # initialise a count variable
    res = 0
    
    for i in range(len(s)):
       # s = s.lower()           # Convert all the character to lowercse
        if s[i]==c:
            res +=1
    return res

# driver code
    
# str = input("Enter the String ")      # Asking from user to give string
# c = input("Enter the character for search ")      
str = "yesturday was valleNtines day and i am single so it was Normal Day for me"
c = "n"

print(count(str,c))
