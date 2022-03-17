# Q 1012 유기농 배추

# input
# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
# 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의
# 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50),
# 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다.
# 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.

# output
# 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

from collections import deque
case = int(input())

def bfs(q, r):
    que = deque()
    graph[q][r] = 0
    que.append((q, r))

    while que:
        a, b = que.popleft()
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                que.append((nx, ny))
    return


cnt_list = []
for c in range(case):  # 2번 반복
    cnt = 0
    graph = []
    n, m, k = map(int, input().split())
    for _ in range(n):
        graph.append([0] * m)
    for bachu in range(k):  # 배추 좌표들 입력받고
        x, y = map(int, input().split())
        for i in range(n):
            for j in range(m):
                if i == x and j == y:
                    graph[i][j] = 1
                else:
                    continue

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for t in range(n):
        for u in range(m):
            if graph[t][u] == 1:
                bfs(t, u)
                cnt += 1
    cnt_list.append(cnt)

for answer in cnt_list:
    print(answer)