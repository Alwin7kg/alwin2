s=input('Enter a sentence')
print(s)
wordsList=s.split()
print(wordsList)
for i in wordsList:
    print(f'{i} occurs {wordsList.count(i)}times')
