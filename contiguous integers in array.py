#https://practice.geeksforgeeks.org/problems/check-if-array-contains-contiguous-integers-with-duplicates-allowed/0
# running time = 0.2

for _ in range(int(input())):
    l = int(input())
    lst = sorted(list(map(int, input().split())))
    lst = list(set(lst))
    c = 0
    for i in range(len(lst) - 1):
        if lst[i] + 1 != lst[i + 1]:
            c = 1
            break
    print("Yes") if c == 0 else print("No")


