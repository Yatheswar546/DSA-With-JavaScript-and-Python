def validAnagram(s, t):

    if(len(s) != len(t)):
        return "false"

    else:
        str1 = {}

        for i in s:
            if i in str1:
                str1[i] +=1
            else:
                str1[i] = 1
    
        str2 = {}

        for i in t:
            if i in str2:
                str2[i] +=1
            else:
                str2[i] = 1

        for i in str1:

            if(i not in str2):
                return "false"
            else:
                if(str1[i] != str2[i]):
                    return "false"
        
        return "true"
            
print(validAnagram("python","nothypp"))


# Time Complexity  : O(s)
# Space Complexity : O(s)