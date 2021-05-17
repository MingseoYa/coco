n, k = map(int, input().split())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

list_a.sort() #오름차순
list_b.sort(reverse=True) #내림차순

for i in range(k):
    if list_a[i] < list_b[i]:
        list_a[i], list_b[i] = list_b[i], list_a[i]
    else:
        break

print(sum(list_a))


