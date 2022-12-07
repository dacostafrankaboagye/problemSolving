'''


An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false


#________________________________________________________________

def is_isogram(string):
    #your code here
    #change all to similar case
    #if the word has a number ==  false
    # have a hashset of the various numbers and compare to the orignal word
    #if same = true
    #else = false
    
    
    
    mySet = set()
    
    newWord = string.lower()
    for letter in newWord:
        if not letter.isalpha():
            return False
        mySet.add(letter)
        
    return len(mySet) == len(newWord)
    
        
            
  


'''
