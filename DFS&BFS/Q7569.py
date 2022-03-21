# 3차원 토마토
# 2차원과 코드 자체는 동일하나 , 박스의 높이 즉 z축(입력은 k)을 고려해야함
from collections import deque
# 입력
m, n, k = map(int, input().split())
arr = []
for _ in range(k):
    arr.append([list(map(int, input().split())) for _ in range(n)])
# arr = [[[],[]] , [[],[]]] 이런 형태로 총 3중리스트 형태인데, 안에 담기는 x,y축으로 이루어진 2중리스트 포함

que = deque()
for u in range(k):
    for i in range(n):
        for j in range(m): #전체 좌표 돌때 주의점 : z축을 먼저 돌아야함 >> 리스트 모양을 보면 1층이 앞의 이중리스트 이기 때문
            if arr[u][i][j] == 1:
                que.append((u,i,j))

# 방향지시등 설정 : 6가지 경우의수가 있기 때문에 6가지 방향 설정
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs():
    t = 0
    while que:
        t += 1
        for i in range(len(que)):  # ***** 핵심 ****
            z, x, y = que.popleft()

            for i in range(6):
                nz = z + dz[i]
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and 0 <= nz < k: # 범위 설정 2차원이랑 동일하나 높이역시 같이 고려
                    if arr[nz][nx][ny] == 0:
                        arr[nz][nx][ny] = 1
                        que.append((nz, nx, ny))

    # 실행후 마찬가지로 박스 전체를 돌면서 익지 않은 토마토 있으면 -1 리턴
    for u in range(k):
        for i in range(n):
            for j in range(m):
                if arr[u][i][j] == 0:
                    return -1

    return t - 1


print(bfs())
