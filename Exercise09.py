num = int(input())
d = dict()
while num > 0:
    num -= 1
    file = input().split()
    lst = file[1:]
    d[file[0]] = lst
    print(d)
