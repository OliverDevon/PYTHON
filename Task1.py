name = str(input('type in a sentence: '))
lengthOfName = len(name)
WCount = 1
for i in name:
    if i == ' ':
        WCount+=1
print('There are:',lengthOfName, 'of letters in this sentence and there are', WCount, 'words in the sentence')

