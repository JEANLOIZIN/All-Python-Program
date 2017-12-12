#JEAN LOIZIN
#CS 100
#SPRING BREAK HOMEWORK



#4.27

def fcopy(firstfile, secondfile):
    infile=open(firstfile,'r')
    outfile=open(secondfile,'w')
    lineList=infile.readlines()
    for lines in lineList:
        outfile.write(lines)

    infile.close()
    outfile.close()

#4.29
    
def stats('text.txt'):
    myfile=open('text.text','r')
    file=infile.read()
    myfile.close()
    lines=len(file.split("\n"))
    words=len(file.split())
    characters=len(file.replace('\n', '').replace(' ', ''))
    print(lines':', words':', characters':')



    
inF = 'hatCat.txt'
outF = 'hatCatrepeatWords.txt'

def repeatWords(inF,outF):
    infile=open(inF,'r')
    outfile= open(ouF,'w')
    count=0

    content=infile.read().split()
    infile.close()
    for word in inf:
        if word.count==2:
            word +=1
    outfile.write(word)

            
repeatWords(inF,outF)

