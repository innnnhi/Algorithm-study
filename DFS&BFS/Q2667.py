from collections import deque

# Q2667 단지번호 붙이기

# 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
# 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

# 해결방안 생각해보기
# bfs 사용 --> 1이 보이면 탐색 시작 > 새로운 1들을 찾아가면서 영역을 셈. > 하나의 1을 찾고 0으로 방문처리 >

# 문제 입력받기
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 상하좌우 탐색을 위한 dx dy 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs탐색 시작
def bfs(i, j):
    que = deque() # 큐로 받고
    graph[i][j] = 0 # 애초에 좌표가 1이면 탐색을 시작해야 하니 , 방문기록을 위해 0으로 재할당(0은 탐색을 안하기 위해)
    que.append((i, j))
    apartment = 1 # 아파트가 있는 위치에서 탐색 시작이니 , 1부터 아파트개수 세기시작

    while len(que) != 0:
        x, y = que.popleft()
        for w in range(4):
            nx = x + dx[w]
            ny = y + dy[w]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: #범위벗어나면 무시
                continue
            if graph[nx][ny] == 1: # 좌표가 1이면 0으로 재할당 => 재탐색을 하지않기 위해
                graph[nx][ny] = 0
                que.append((nx, ny))
                apartment += 1
    return apartment #아파트개수 리턴

# dangi = 아파트개수를 모아놓은 동네 ==> 길이가 총 아파트 단지 수
dangi = []
for i in range(n): # 좌표를 돌면서
    for j in range(n):
        if graph[i][j] == 1: # 그 좌표가 1이면 탐색 시작
            dangi.append(bfs(i, j))

print(len(dangi))
for k in sorted(dangi):
    print(k)
