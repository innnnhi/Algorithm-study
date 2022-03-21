# Q7576 토마토(2차원)
# input
# 첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다.
# M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다.
# 단, 2 ≤ M,N ≤ 1,000 이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다.
# 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다.
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
# 토마토가 하나 이상 있는 경우만 입력으로 주어진다.

# output
# 여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다.
# 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

from collections import deque
# 문제 입력 받기
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]  # 토마토 밭 입력

que = deque() # 탐색시작점을 담을 que
for i in range(n): # 좌표돌면서
    for j in range(m):
        if arr[i][j] == 1: # 1이면 탐색시작지점으로 지정
            que.append((i, j))  # 1이 여러개 있으면 탐색시작점이 여러개 담김

# 좌표이동 x,y축
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#bfs 실행
def bfs():
    t = 0
    while que: #que가 빌때까지 실행 ==> 다비면 종료
        t += 1 # 한번실행될때마다 +1
        for i in range(len(que)):  # ***** 핵심 ****
            x, y = que.popleft() # que에 담긴 길이만큼 돌면서 여러개의 시작점이 한번에 각각 탐색하도록 설정

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if arr[nx][ny] == 0:
                        arr[nx][ny] = 1
                        que.append((nx, ny)) # 새로 시작할 탐색지역 que에 넣어줌

    for i in range(n):
        for j in range(m): # 한번 더 그래프를 돌면서
            if arr[i][j] == 0: # 익지 않은 토마토가 있다면 -1 리턴
                return -1

    return t - 1 # 첫 탐색지역에서 시작할때 +1 이 된 상태로 시작하기때문에 -1 해준 후 리턴


print(bfs())
