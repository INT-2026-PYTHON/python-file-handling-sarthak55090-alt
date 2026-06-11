"""
## 5. Longest Palindrome in the File  *(Hard)*

=================================================
LONGEST PALINDROME
=================================================

Problem Statement:
Read the text file `sowpods.txt` and find the
LONGEST PALINDROME word in the file.

If multiple palindromes share the maximum
length, print ALL of them.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
noon
civic
deified
racecar
rotator
malayalam

Output Example:
Longest palindrome length: 9
malayalam

-------------------------------------------------
Explanation:
Lengths of the palindromes in the sample:
   level    -> 5
   radar    -> 5
   noon     -> 4
   civic    -> 5
   deified  -> 7
   racecar  -> 7
   rotator  -> 7
   malayalam -> 9
The longest is "malayalam" with 9 characters.
=================================================

"""
def longest_palindrome(path):
    with open(path,"r") as files:
     max = 0
     max_word = ""
    
     for word in files:
            
            word = word.strip()
            letters = list(word)
            rev = ""
            
            while letters:
              rev += letters.pop()
            
            if word == rev:
               length = len(word)
               if length > max:
                   max = length
                   max_word = word
            else:
                continue
    return (max,max_word)
print(f'Longest Plaindrome length:  {longest_palindrome("file_reading_practice/sowpods.txt")}')
  

          
                
