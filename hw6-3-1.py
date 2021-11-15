# author: LM (AMDG) 11/15/21
word1 = input("Enter a word: ")
word2 = input("Enter another word: ")
newlist = list([word1, word2])
print(newlist)
if word1 == word2: 
    print("They are the same word.")
elif sorted(word1) == sorted(word2):
    print(word1 + " and " + word2 + " are anagrams.")
else:
    print(word1 + " and " + word2 + " are not anagrams.")
