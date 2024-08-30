import random
print("숫자 야구 게임을 시작합니다. ")
cnt = 0
gameover = True
rg = [1, 2, 3, 4, 5, 6, 7, 8, 9]
strr = ""
a = random.sample(rg, 3)
for i in a:
    strr = strr + str(i)
while gameover:
    user = input()
    s, b = 0, 0
    if strr[0] in user:
        b += 1
    if strr[1] in user:
        b += 1
    if strr[2] in user:
        b += 1
    if strr[0] == user[0]:
        s += 1
        b -= 1
    if strr[1] == user[1]:
        s += 1
        b -= 1
    if strr[2] == user[2]:
        s += 1
        b -= 1
    if s == 0 and b == 0:
        print("OUT")
    elif s == 0 and b > 0:
        print(f"{b}B")
    elif s > 0 and b == 0:
        print(f"{s}S")
    else:
        print(f"{b}B {s}S")
    if s == 3:
        print("3개 다 맞춤")
        break
