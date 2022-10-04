N = 6
A = [1, -45, 3, 2, 100, -45]
for i in range(N-1):
    for j in range(N-2, i-1, -1):
        if A[j] < A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
for n in range(N):
    print(A[n])
