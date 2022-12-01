import sys
import time
sys.setrecursionlimit(100000000)

# class PathCreation:
#     def __init__(self):
#         pass
    
#     def create_path():
#         pass

# def main():
#     pathcreation = PathCreation()
#     target_filling_rate = 1
#     route = pathcreation.create_path()



# if __name__ == "__main__":
#     main()


# width = 4
# height = 4
# G = [[] for _ in range(height)]
# idx = 0
# for i in range(height):
#     for _ in range(width):
#         G[i].append(idx)
#         idx += 1
# for row in G:
#     print(row)
# G = [
#     [0, 1, 2],
#     [3, 4, 5],
#     [6, 7, 8]
# ]
# def create_adjacency_list(width, height):
#     adjacency_list = [[] for _ in range(height*width)]
#     for i in range(height):
#         for j in range(width):
#             idx = G[i][j]
#             for i2, j2 in [[i+1, j],[i-1, j],[i, j+1],[i, j-1]]:
#                 if not(0<=i2<height and 0<=j2<width): continue
#                 adjacency_list[idx].append(G[i2][j2])
#     return adjacency_list

# sx, sy = 0, 0
# gx, gy = width-1, height-1
# target_filling_rate = 1
# grid_max = width*height
# adjacency_list = create_adjacency_list(width, height)
# print(adjacency_list)
# ans_rate = 0
# ans_route = []


# def dfs(route:list, now:int):
#     global G, gx, gy, grid_max, ans_rate, ans_route
#     # print(route)
#     if route[-1] == G[gy][gx]:
#         return route
    
#     for i in adjacency_list[now]:
#         if i not in set(route):
#             new_route = route + [i]
#             tmp = dfs(new_route, i)
#             rate = len(tmp)/grid_max
#             if ans_rate < rate:
#                 print(tmp)
#                 ans_route = tmp
#                 ans_rate = rate
    
#     return ans_route

# pretime = time.time()
# result_route = dfs([G[sy][sx]], G[sy][sx])
# print("実行時間：", time.time()-pretime)
# print(result_route)


# 動的計画法
width = 5
height = 5
G = [[] for _ in range(height)]
idx = 0
for i in range(height):
    for _ in range(width):
        G[i].append(idx)
        idx += 1
for row in G:
    print(row)
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


goal = width*height-1

dp = [[[] for _ in range(width*height)] for _ in range(height*width)]
# memo[i][j], 残りの実行回数iと残りの候補配列j
memo = [[] for _ in range(height*width)]

dp[0][0].append([0])

for i in range(height*width-1):
    for j in range(height*width):
        for k in dp[i][j]:
            if k[-1] == goal: continue
            for el in adjacency_list[k[-1]]:
                if el in set(k): continue
                # print(el)
                tmp = k + [el]
                dp[i+1][el].append(tmp)

for row in dp[-1][-1]:
    print(*row)

# print(ans)
# for row in dp[-1]:
#     print(row)

# for row in dp:
#     for el in row:
#         print(f"{el:6g}", end=" ")
#     print("", end="\n")


# sousa, now = 15, 15
# ans = [now]

# for i in range(sousa-1, -1, -1):
#     for j in range(width*height):
#         if not dp[i][j]: continue
#         if j in ans: continue
#         if j in adjacency_list[now]:
#             if j == 0: continue
#             ans.append(j)
#             now = j
#             break
# print(ans)
