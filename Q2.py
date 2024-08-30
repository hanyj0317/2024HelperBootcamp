a = [1, 2, 2, 3, 4, 5, 5]
b = [3, 2, 6, 6, 8, 1, 9]

def deleteRepeat(a):
    a = set(a)
    return a
    
def union(a, b):
    answer = []
    a = deleteRepeat(a)
    for i in a:
        answer.append(i)
    b = deleteRepeat(b)
    for j in b:
        if j not in answer:
            answer.append(j)
    
    return answer

def intersection(a, b):
    a = deleteRepeat(a)
    b = deleteRepeat(b)
    
    answer = []
    
    for i in a:
        if i in b:
            answer.append(i)
    
    return answer

print(intersection(a, b))
