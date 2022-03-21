# Q2178 : 미로 탐색 (미로 = N * M)
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때,
# (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
from collections import deque
n, m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)] # 그래프 입력
dx = [-1,1,0,0] # 방향지시 --> 좌 우 상 하
dy = [0,0,-1,1] # 좌 우 상 하


def bfs_sol(x,y):
    que = deque()
    que.append((x,y))

    while que : # que가 빌때까지
        x,y = que.popleft() # 탐색시작점
        for i in range(4): # 방향 선택
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m: # 그래프 범위 벗어나면 무시
                continue
            if graph[nx][ny] == 0: # 탐색지역이 0이면(막혀있으면) 무시
                continue
            if graph[nx][ny] == 1: # 탐색해야할 곳이라면
                graph[nx][ny] = graph[x][y] + 1 # 이전 시작지점에 + 1 을 해줌으로써 첫 출발점과의 거리 표시
                que.append((nx,ny)) # 새로운 시작점 지시

    return graph[n-1][m-1] # 그래프의 마지막 원소(N*M)의 값 리턴 --> 첫 시작점으로부터 의 길이


print(bfs_sol(0,0)) # 시작점 좌표 입력