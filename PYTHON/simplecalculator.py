n1=int(input('Enter first number: '))
n2=int(input('Enter second number: '))
print('1.ADD\n 2.SUB\n 3.MUL\n 4.DIV\n')
ch=input('Enter your choice: ')
if ch=='1':
    sum=n1+n2
    print('sum= ',sum)
elif ch=='2':
    diff=n1-n2
    print('diff= ',diff)
elif ch=='3':
    pro=n1*n2
    print('Product= ',pro)
elif ch=='4':
    quo=n1/n2
    print('Quotient= ',quo)
else:
    print('Enter correct choice: ')
    
