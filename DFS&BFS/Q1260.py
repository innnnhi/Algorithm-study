# Q 1260 : 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
# 조건 :
# n = 정점(node)개수 , m = 간선(양방향)의 개수 , v = 탐색을 시작할 정점의 번호

# sol
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [0] * (n + 1)
visited2 = [0] * (n + 1)


def dfs(num):
    visited[num] = 1
    print(num, end=" ")
    for j in graph[num]:
        if not visited[j]:
            dfs(j)
    return ""


def bfs(num):
    que = deque([num])
    visited2[num] = 1
    while que:
        t = que.popleft()
        print(t, end=" ")
        for l in graph[t]:
            if not visited2[l]:
                que.append(l)
                visited2[l] = 1
    return ""


print(dfs(v))
print(bfs(v))