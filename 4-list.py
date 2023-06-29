# list1 = ["apple", "banana", "cherry"]
# for x in list1:
#     print(x)

# for i in range(len(list1)):
#     print(list1[i])

#creat new list from existing list
# newlist = []
# for x in list1:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)


# list2 = [1,3,6,5]
# list2.sort()
# print(list2)

# list1.append("mango")
# print(list1)

# del list1[3]

# list1[0]= ("mango")
# print(list1)

# conlist = list1 + list2
# print(conlist)

multidimention = [["apple", "banana", "cherry"],[1,3,6]]
newlist1 = []

for x in multidimention:
    newlist1.append(x[0:2])
print(newlist1)
# print(multidimention)

# print(multidimention[1][3])
