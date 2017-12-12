s=['i would not like them here or there']
def vowelCount(s):
    vowels = 'aeiouAEIOU'
    d=[]
    for char in s:
        count = 0
        for char in s:
            if char in vowels:
                if char not in d:
                    d.append(char)
                
        return d


print(vowelCount(s))
