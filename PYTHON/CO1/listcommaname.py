color=[ ]
n=int(input("Enter total number of colours: "))
print("Enter colours:")
for i in range(n):
    ch=input()
    color.append(ch)
print(f"First color is:{color[0]} \nLast color is: {color[-1]}")    
