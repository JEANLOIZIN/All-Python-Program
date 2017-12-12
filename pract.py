def uniqueWords(phrase):
     unique = []
     words = phrase.split()
     for word in words:
         if words.count(word) == 1:
             unique.append(word)
     return unique
popEye = "I am what I am"
print(uniqueWords(popEye))
