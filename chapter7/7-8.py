n, m = list(map(int, input().split(' '))) # 떡의 개수, 떡의 길이
array = list(map(int, input().split())) # 떡의 높이

start = 0 # 시작점
end = max(array) # 끝점

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for i in array:
        if i > mid:
            total += i - mid
    # 떡의 양이 부족한 경우(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우(오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

# 정답 출력
print(result)