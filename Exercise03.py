a = set(input().split())
b = set(input().split())
a.intersection_update(b)
print(" ".join(sorted(a)))
