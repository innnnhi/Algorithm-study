import sys

n , m = map(int, sys.stdin.readline().split())
chess = []
for i in range(n):
    chess.append(sys.stdin.readline().strip())
cnt = []
# print(chess)
for i in range(n-7):
    for j in range(m-7):
        first_Black = 0
        first_White = 0
        for u in range(i,i+8):
            for k in range(j,j+8):
                if (u+k) % 2 == 0 :
                    if chess[u][k] != 'B':
                        first_Black += 1
                    if chess[u][k] != 'W':
                        first_White += 1
                else:
                    if chess[u][k] != 'B':
                        first_White += 1
                    if chess[u][k] != 'W':
                        first_Black += 1
        cnt.append(first_Black)
        cnt.append(first_White)
print(min(cnt))

