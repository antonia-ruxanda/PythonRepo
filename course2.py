myList = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
ascList, descList = list(myList), list(myList)
multiplyList = []

ascList.sort()
descList.sort(reverse=True)
evenList = ascList[1::2]
oddList = ascList[::2]

for i in myList:
    if i % 3 == 0:
        multiplyList.append(i)

print('Ascending list:', ascList)
print('Descending list', descList)
print('Even list', evenList)
print('Odd list', oddList)
print('Multiplies of 3 list', multiplyList)

