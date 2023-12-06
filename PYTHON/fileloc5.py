f=open("test.txt","w")
seq=["first line\n","second line\n","third line\n","fourth line\n","fifth line\n"]
f.writelines(seq)
f.close()
f=open("test1.txt","r")
line=f.readlines()
print("line:",line)
f.close()
