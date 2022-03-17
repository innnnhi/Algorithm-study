# Q2606 바이러스

# 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다.
# 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
# 예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자.
# 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어
# 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다.
# 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

# input
# 첫째 줄에는 컴퓨터의 수가 주어진다.
# 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다.
# 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

from collections import deque
node = int(input())
trunk = int(input())
graph = [[] for _ in range(node+1)]

for _ in range(trunk):
    a , b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (node+1)

def bfs(n, visited):
    que = deque()
    que.append(n)
    visited[n] = 1
    cnt = 0
    while que :
        v = que.popleft()
        cnt += 1
        for i in graph[v]:
            if visited[i] == 0:
                que.append(i)
                visited[i] = 1
    return cnt-1

print(bfs(1,visited))


