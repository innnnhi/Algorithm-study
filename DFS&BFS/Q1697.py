# 숨바꼭질

# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
# 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

# sol
# n = 현재위치
# k = 동생위치 == 목표지점
from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001 # 전체 좌표 0으로 만들고 하나의 수평선이라 생각


def bfs():
    que = deque()
    que.append(n) # 탐색 시작점 입력

    while que: #que가 빌때까지 반복
        now = que.popleft() # 현재위치 설정
        if now == k: # 현재위치 == 목표위치 이면 탐색종료
            return visited[now]

        else:
            for next_location in (now - 1, now + 1, now * 2): # 다음 위치로 갈 탐색위치
                if 0 <= next_location < 100001 and not visited[next_location]: # 탐색범위 안에 있다면 즉 좌표안에 다음위치가 존재하면
                    visited[next_location] = visited[now] + 1 # 다음위치에 +1을 해줌으로서 다음위치까지 이동한 시간을 알수 있음
                    que.append(next_location) # 다음탐색위치 que에 추가


print(bfs())
