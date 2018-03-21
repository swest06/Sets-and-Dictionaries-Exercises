line = input().split(" ")
d = dict()
list1 = []
for c in line:
    d[c] = d.get(c, 0) + 1
    list1.append(d[c] - 1) 
for i in list1:
    print(i, end= " ")
