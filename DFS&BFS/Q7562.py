# Q7562 나이트의 이동
from collections import deque

# import sys

k = int(input())  # 케이스 개수
move = [(-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, 2), (2, 1), (1, -2), (2, -1)] # 방향 지시등
answer = []
for _ in range(k):
    t = int(input())  # 변의 길이
    chess = [[0]*t for _ in range(t)] # chess판에서 움직인 횟수 == visited역할
    a, b = map(int, input().split())  # start 시작점 받기
    c, d = map(int, input().split())  # end 도착점 받기
    que = deque()
    que.append((a, b)) # 시작점 입력받고

    while que:
        x, y = que.popleft() # 탐색시작점 설정
        if x == c and y == d: # 탐색시작할려고 봤는데 도착점이랑 같다면
            answer.append(chess[c][d]) # answer에 넣고 while문 탈출
            break

        for i in range(8):
            nx = x + move[i][0] # 이동 후 좌표 설정
            ny = y + move[i][1]

            if 0 <= nx < t and 0 <= ny < t: # 체스판 안이라면
                if chess[nx][ny] == 0: # 아직 방문 안했으면
                    chess[nx][ny] = chess[x][y] + 1 # 이전 탐색에 +1 을 해서 다음 좌표로 넘어가
                    que.append((nx, ny))

for j in answer:
    print(j)

