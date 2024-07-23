def pairs_of_numbers(n):
    res = []
    result = []
    answer = ''
    for i in range(1, n):
        for j in range(i+1, n+1):
            if i != j:
                if n % (i + j) == 0:
                    res.append(i)
                    res.append(j)
                    result.append(res)
            res = []
    for h in result:
        for k in h:
            answer += str(k)
    return answer

answer = pairs_of_numbers(int(input('Введите число от 3 до 20: ')))

print(answer)
