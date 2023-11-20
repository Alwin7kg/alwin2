#RANGE
'''
#To print the range of elements in a list
print(range(10))
print(list(range(10)))
print(list(range(2,10)))
print(list(range(0,10,2)))

#program to iterate through a list using indexing
thing = ['rock','paper','scissor']
for i in range(len(thing)):
    print("I choose",thing[i])

for num in range(0,9,3):
    print('Number=',num)

for item in range(0,90,9):
    print('Multiples of 9=',item)
'''
y1=int(input('Enter the starting year: '))
y2=int(input('Enter the ending year: '))
if y1>y2:
    print('INVALID!!.. End year must be greater than or equal to the current year: ')
else:
    print(f"Leap year from {y1} to {y2}")
    for year in range(y1,y2+1):
        if(year%4==0 and year %100!=0) or (year%400==0):
            print(year)
