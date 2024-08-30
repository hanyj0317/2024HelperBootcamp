n = input()
lst = []
for i in n:
    lst.append(i)
lst.reverse()
cnt = 0
for j in range(3, len(lst), 4):
    lst.insert(j, ",")

lst.reverse()
print(''.join(lst))
