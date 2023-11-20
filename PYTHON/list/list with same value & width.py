list1 = [8, 6, 7, 4, 5]
list2 = [6,5,4,5,6]
#a.Check if the lists have the same length
if len(list1)==len(list2):
    print("a.The list have the same length.")
else:
    print("b.The list have different length.")
#b







    
print(f"b.sum of list1:{sum(list1)} & sum of list2:{sum(list2)}")
if sum(list1)==sum(list2):
    print("The lists sum to the same value.")
    print("The lists do not sum to the same value.")
if common_values:
    print(f"c.Common values in both lists: {common_values}")
else:
    print("c. There are no common values in both lists.")
