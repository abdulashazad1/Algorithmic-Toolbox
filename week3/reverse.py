class Solution(object):
    def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        # max and min assertions
        MAX = 2**31 -1
        MIN = -2**31 + 1 
        #checking for isNegative
        if x >= 0:
            isNegative = 1
        elif x < 0:
            x = x*-1
            isNegative = -1
        # convert to a string
        input = str(x)
        newString = ""
        #index the string to reverse it
        for i in range(len(input)-1, -1, -1):
            newString += input[i]
        
        # checking for int overflow
        if int(newString)*isNegative > MAX or int(newString)*isNegative < MIN:
            return 0
        
        return int(newString)*isNegative  
    
    #testing
    
    print(reverse(-123))
