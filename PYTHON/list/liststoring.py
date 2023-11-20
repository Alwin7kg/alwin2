'''
#Initialize an empty list to store positive numbers
list1=[2,4,-6,-8,7]
list2=[]
for i in list1:
    if i>0:
        list2.append(i)
        print(f'list={list2}')

#vowel
word=input('Enter a word:')
listVowel=[i for i in word if i in 'aeiouAEIOU']
print(f'vowels are {listVowel}')

w=input('Enter any character:')
listOrdinals=[ord(i) for i in w]
print(listOrdinals)

s=input('Enter a sentence')
print(s)
wordsList=s.split()
print(wordsList)
for i in wordsList:
    print(f'{i} occurs {wordsList.count(i)}times')
'''
