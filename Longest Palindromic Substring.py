'''
5. Longest Palindromic Substring
Medium

Given a string s, return the longest 
palindromic
 
substring
 in s.

'''





#_________________________________


'''


time limit exceeded

        def compare(aWord):
            return aWord == aWord[::-1]
        temp = ""
        d = dict()
        #wordList = list(s)
        wordList2 = list(s)
        idx = 0
        for lett in range(len(s)):
            while idx < len(wordList2):
                temp += wordList2[idx]
                if temp == temp[::-1]:
                    #if temp not in d:
                    d[len(temp)] = temp
                idx +=1
            wordList2.remove(s[lett])
            temp = ""
            idx = 0
        
        return d[max(d.keys())]
                    


   


class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resultLength = 0
        #d = dict()
        for i in range(len(s)):
            leftPointer, rightPointer = i, i
            while rightPointer< len(s) and leftPointer >=0 and s[leftPointer] == s[rightPointer]:

                if (rightPointer - leftPointer+1) > resultLength:
                    result = s[leftPointer: rightPointer+1] 
                    resultLength = rightPointer - leftPointer+1
                #d[len(result)] = result
                leftPointer -=1 
                rightPointer += 1
        
            leftPointer = i
            rightPointer = i+1
            
            while rightPointer< len(s) and leftPointer >=0 and s[leftPointer] == s[rightPointer]:

                if (rightPointer - leftPointer+1) > resultLength:
                    result = s[leftPointer: rightPointer+1] 
                    resultLength = rightPointer - leftPointer+1
                #d[len(result)] = result
                leftPointer -=1 
                rightPointer += 1
    
        # maximum = max(d.keys())
        # return d[maximum]
        return result


                 

            

'''


# without using dictionary

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resultLength = 0

        
        def perform(leftPointer, rightPointer, resultLength, result):
        
            while leftPointer >=0 and rightPointer < len(s) and s[leftPointer] == s[rightPointer]:
                if (rightPointer - leftPointer+1) > resultLength:
                    result = s[leftPointer:rightPointer+1]
                    resultLength  = rightPointer - leftPointer+1
                leftPointer -=1
                rightPointer +=1
            return [resultLength, result]


        for i in range(len(s)):
            leftPointer, rightPointer = i,i
            [resultLength, result] = perform(leftPointer, rightPointer, resultLength, result)
            leftPointer, rightPointer = i, i+1
            [resultLength, result] = perform(leftPointer, rightPointer, resultLength, result)

            
        return result




            
        

            
            


