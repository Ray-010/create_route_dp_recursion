import time
import sys
sys.setrecursionlimit(1000000000)

width = 51
height = 51
G = [[] for _ in range(height)]
idx = 0
for i in range(height):
    for _ in range(width):
        G[i].append(idx)
        idx += 1

# for row in G:
#     print(*row)

def create_adjacency_list(width, height):
    adjacency_list = [[] for _ in range(height*width)]
    for i in range(height):
        for j in range(width):
            idx = G[i][j]
            for i2, j2 in [[i+1, j],[i-1, j],[i, j+1],[i, j-1]]:
                if not(0<=i2<height and 0<=j2<width): continue
                adjacency_list[idx].append(G[i2][j2])
    return adjacency_list

sx, sy = 0, 0
gx, gy = width-1, height-1
target_filling_rate = 1
grid_max = width*height
adjacency_list = create_adjacency_list(width, height)
ans_rate = 0
ans_route = []


pre_time = time.time()

dp = [[[] for _ in range(width*height)] for _ in range(height*width-1)]

for i in adjacency_list[0]:
    dp[0][i].append(0)

for i in range(height*width-1):
    for j in range(height*width):
        if j == 0: continue
        if not dp[i-1][j]: continue # 空
        for el in adjacency_list[j]:
            if j in dp[i][el]: continue
            dp[i][el].append(j)

print("done dp list")
# for row in dp:
#     print(*row)


ans = []
memo = [set() for _ in range(width*height)]
def dfs(route:list, y, x):
    global ans
    if route[-1] == 0: return route
    # if route[-1] in memo[(len(route)-1)]: return route[:-1]
    # if x in memo[y]: return route[:-1]

    for i in dp[y][x]:
        if i in set(route): continue
        if i not in adjacency_list[x]: continue

        new_line = route + [i]
        route = dfs(new_line, y-1, i)

    if len(ans) < len(route):
        if route[-1] == 0: ans = route
        else: 
            # memo[y].add(x)
            return route[:-1]
    # if route[-1] == 0: return route

    return route

# y 試行回数, now
goal = width*height-1
""" dfs 引数
# rotue
# start y, 0<=y<=width*height-2
# start x, 0<=x<=width*height-1
"""
y = width*height-2
x = width*height-1

# ans = dfs([width*height-1], y, x)

# for row in dp:
#     print(row)

# for row in memo:
#     print(row)

# print(ans)
# print(time.time()-pre_time)


print("#####################################")
# 2重dp ----------------------------------------------------------------
dp2 = [[[] for _ in range(width*height)] for _ in range(height*width-1)]
for i in adjacency_list[width*height-1]:
    dp2[0][i].append(width*height-1)


for i in range(height*width-2):
    for j in range(height*width):
        if not dp2[i][j]: continue # 空
        if j == (width*height-1): continue

        for el in adjacency_list[j]:
            if j in dp2[i][el]: continue
            dp2[i+1][el].append(j)

dp2.reverse()
# for row in dp2:
#     print(row)

ans = []
def dfs(route, y, x):
    if route[-1] == width*height-1: return route
    for i in dp2[y][x]:
        if i in route: continue
        new_line = route + [i]
        route = dfs(new_line, y+1, i)
    return route
# for row in dp:
#     print(row)
# print("######")
# for row in dp2:
#     print(row)

ans = dfs([0], 0, 0)
print(time.time()-pre_time)
print(ans)

