# # 胡睿诚	174ms
#
# import heapq
# m, n, p = map(int, input().split())
# info = []
# for _ in range(m):
#     info.append(list(input().split()))
# directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
#
#
# def dijkstra(start_r, start_c, end_r, end_c):
#     pos = []
#     dist = [[float('inf')] * n for _ in range(m)]
#     if info[start_r][start_c] == '#':
#         return 'NO'
#     dist[start_r][start_c] = 0
#     heapq.heappush(pos, (0, start_r, start_c))
#     while pos:
#         d, r, c = heapq.heappop(pos)
#         if r == end_r and c == end_c:
#             return d
#         h = int(info[r][c])
#         for dr, dc in directions:
#             nr = r + dr
#             nc = c + dc
#             if 0 <= nr < m and 0 <= nc < n and info[nr][nc] != '#':
#                 if dist[nr][nc] > d + abs(int(info[nr][nc]) - h):
#                     dist[nr][nc] = d + abs(int(info[nr][nc]) - h)
#                     heapq.heappush(pos, (dist[nr][nc], nr, nc))
#     return 'NO'
#
#
# for _ in range(p):
#     x, y, z, w = map(int, input().split())
#     print(dijkstra(x, y,z,w))

#jrx's daima
import heapq
fangxiang={(0,1),(0,-1),(1,0),(-1,0)}
def dijiesitela(x1,y1,x2,y2):
    if ditu[x1][y1]=='#' or ditu[x2][y2]=='#':
        return "NO"
    shuchu=[[float('inf')]*n for _ in range(m)]
    shuchu[x1][y1]=0
    senn = [[0] * n for _ in range(m)]
    xianyoushuju=[(0,x1,y1)]
    while xianyoushuju:
        (juli_min,xx,yy)=heapq.heappop(xianyoushuju)
        if (xx,yy) == (x2,y2):
            return juli_min

        gaodu=int(ditu[xx][yy])

        for dx,dy in fangxiang:
            if 0<=xx+dx<m and 0<=yy+dy<n and ditu[xx+dx][yy+dy]!='#':
                gaoducha=abs(gaodu-int(ditu[xx+dx][yy+dy]))
                if gaoducha+juli_min<shuchu[xx+dx][yy+dy]:
                    heapq.heappush(xianyoushuju,(gaoducha+juli_min,xx+dx,yy+dy))
                    shuchu[xx+dx][yy+dy]=gaoducha+juli_min

    return "NO"






m,n,p=map(int,input().split())
ditu=[list(input().split()) for i in range(0,m)]
for _ in range(p):
    x1,y1,x2,y2=map(int,input().split())
    print(dijiesitela(x1,y1,x2,y2))
