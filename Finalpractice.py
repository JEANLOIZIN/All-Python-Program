inF = 'word.txt'
outF = 'repeatwords.txt'


def repeatWords(inF,outF):
    infile = open(inputF, 'r')
    outfile = open(outputF, 'w')
    content = infile.read().lower().split('\n')
    for words in content:
        if infile.count(word)>1 and word not in outfile:
                    outfile.write(word + '\n')

    inF.close()
    outF.close()

