A = [12, 7, 4, -2, 10, 4, 9]
B = [16, 3, 2, 10, -2, 6, 4]
C = []

A.sort()
B.sort()

print(A, B)
print("Превращается в...")

for i in A:
    if i in C:
        continue
    for j in B:
        if i == j:
            C.append(i)
    print(C)
