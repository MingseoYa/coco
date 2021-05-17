# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) //2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

n = int(input()) # 전자 매장 부품
array = list(map(int, input().split())) # 부품 고유 번호
m = int(input()) # 찾을 부품 종류
array2 = list(map(int, input().split())) # 찾을 부품 고유 번호

for i in array2:
    if binary_search(array, i, 0, n - 1) == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')