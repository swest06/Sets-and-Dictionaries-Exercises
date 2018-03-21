n = int(input())
d = dict()

for i in range(n):
    pair = input().split()
    d[pair[0]] = pair[1]
    d[pair[1]] = pair[0]

last = input()
print(d[last])
