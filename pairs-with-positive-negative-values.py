#https://practice.geeksforgeeks.org/problems/pairs-with-positive-negative-values/0
for _ in range(int(input())):
    length = int(input())
    arr = sorted(list(map(int, input().split())))
    pairs = []
    num = arr.pop()
    for a in arr:
        while num / a <= -1:
            if num / a == -1:
                pairs.append(a)
                break
            num = arr.pop()
    if pairs:
        for val in pairs[::-1]:
            print(val, -val, end=" ")
        print()
    else:
        print(0)
