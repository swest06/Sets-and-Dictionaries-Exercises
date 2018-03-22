num = int(input())
d = dict()
while num > 0:
    num -= 1
    file = input().split()
    lst = file[1:]
    for i, e in enumerate(lst):
        if e == "R":
            lst[i] = "read"
        elif e == "W":
            lst[i] = "write"
        else:
            lst[i] = "execute"      
    d[file[0]] = lst

num2 = int(input())
while num2 > 0:
    num2 -= 1
    file2 = input().split()
    if file2[0] in d[file2[1]]:
        print("OK")
    else:
        print("Access denied")
