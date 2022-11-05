def is_sov(a):
    arr = []
    for i in range(1, a):
        if a % i == 0:
            arr.append(i)
    if sum(arr) == a:
        print(a, end=' ')

a = int(input())
for i in range(1, a):
    is_sov(i)