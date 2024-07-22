n = int(input())
result = []

for i in range(1, n//2+1):
    for j in range(1, n+1):
        if n % (i + j) == 0:
            if i != j:
                result += [i, j]
            
print(*result, sep = '')