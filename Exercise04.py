nums = input().split()
al = int(nums[0])
bob = int(nums[1])
a = set()
b = set()

while al > 0:
    al -= 1
    a.add(int(input()))

while bob > 0:
    bob -= 1
    b.add(int(input()))

inter = (a.intersection(b))

print(len(inter))
sorted(inter)
for i in inter: print(i)

a = sorted(a.difference(b))
b = sorted(b.difference(inter))

print(len(a))
for i in a: print(i)

print(len(b))
for i in b: print(i)
