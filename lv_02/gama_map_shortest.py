#-*- coding:utf-8 -*-

from collections import deque



def bfs(map):
    
    M = len(map) - 1
    dx = [0, 1, 0, -1] # 4방향 북동남서 순서
    dy = [1, 0, -1, 0]

    q = deque()
    q.append([0,0])
    
    while q:
        a,b = q.popleft()
        
        if a == M and b == M:
            print(map[a][b])
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0 <= nx <= M and 0 <= ny <= M and map[nx][ny] == 1:
                q.append([nx,ny])
                map[nx][ny] = map[a][b] + 1
    
    if map[M][M] == 1:
        print(-1)
    

map = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	

bfs(map)


print(map)