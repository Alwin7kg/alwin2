file=open('file1.txt','w')
try:
    file.write('hello world')
finally:
    file.close()
        
