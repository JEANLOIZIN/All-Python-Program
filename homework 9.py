# Jean Loizin
# Practice exam two


#1)
Answer: D , ( 10 12 13 )

#2)
Answer: B, ( 3 )

#3)
Answer: D ( abraabracadabra )

#4)
Answer: B ( ['oo', 'ei', 'ea', 'io']

#5)
Answer: E ( none of the above, correct answer should be ( k ))

#6)
Answer: A ( D )

#7)
Answer: D ( ['zombie', 'pirate'] )

#8)
Answer: C ( ['that', 'ay'] )

#9)
Answer: C ( 9 )

#10)
Answer: C ( [0, 3] )

#11)
Answer: B ( Joe
            Mary )

#12)
Answer: C ( ['what']


#13)
Drawing droplets


def droplets(t,size,seperations):
            for space in seperations:
                t.down()
                t.circle(size)
                t.up()
                t.forward(space)



#14)

            
def words(word):
    return sum(letter in vowels for letter in word)

def mostlyVowels(lower):
    repeated=[]
    
    for word in lower.split():
        if words(word)>=3:
            repeated_vowels=word
            
    print(repeated_vowels)

mostlyVowels(lower
            

#15)
             
inF = 'bells.txt'
outF = 'bellsRepLines.txt'

def duplicateWordLines(inF,outF):
    infile=open(inF,'r')
    outfile= open(ouF,'w')
    count=0

    content=infile.read().split()
    infile.close()
    for word in inf:
        if word.count==2:
            word +=1
    outfile.write(word)

            
duplicateWordLines(inF,outF)


            

