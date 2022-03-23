# Q2206 벽부수고 이동하기
# N×M의 행렬로 표현되는 맵이 있다.
# 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
# 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다.
# 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
# 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
#
# 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)] # 좌표 입력
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
# 여기서 visited 3차원으로 만드는 이유는 x축 y축의 해당 인덱스에 위치한 원소의 [벽을 부수지않고 온 경우의 수 , 벽을 부수고 온 경우의수] 를 추가 해야함
# 최종형태가 [[[x][y][벽 부수지x 온 경우의 수 , 벽 부순o 경우의 수 ]]]
visited[0][0][0] = 1
#방향지시등
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
que = deque()
que.append((0, 0, 0))


def bfs(): ##
    while que:
        x, y, t = que.popleft() # 탐색시작지점 갱신
        if x == n-1 and y == m-1: # 우리가 원하는 끝지점 도달시 그 즉시 리턴
            return visited[x][y][1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # if 절이 2개인이유 = 벽을 부수고 이동했을때의 경우의수와, 이미벽을부쉈다면(기회사용완료) 벽을 피해서 이동해야하기 때문에 벽을 피해서
                # 이동하는 경우의수를 따로 체크해줘야하기 때문
                if arr[nx][ny] == 0 and visited[nx][ny][t] == 0: # 만난 곳이 벽이 없고 아직 방문도 안했으면 방문
                    visited[nx][ny][t] = visited[x][y][t] + 1
                    que.append((nx, ny, t))
                # 우리가 갈 곳이 벽이 있고 , 방문도 안했는데 , 벽부술기회(t) 조차 사용한적 없으면 한번 사용하고 방문
                if t == 0 and arr[nx][ny] == 1 and visited[nx][ny][t] == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    que.append((nx, ny, 1))
    return -1 # 다돌고 나서 위의 if - return문에서 리턴이 나오지 않았다면 제대로 가지 못한단 뜻이기 때문에 -1 리턴


print(bfs())


# target = max(visited[n-1][m-1])
# if target == 0 :
#     print(-1)
# else:
#     print(target)