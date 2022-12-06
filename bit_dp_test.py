import sys
sys.setrecursionlimit(10000000)


def create_adjacency_list(width, height):
    adjacency_list = [[] for _ in range(height*width)]
    for i in range(height):
        for j in range(width):
            idx = G[i][j]
            for i2, j2 in [[i+1, j],[i-1, j],[i, j+1],[i, j-1]]:
                if not(0<=i2<height and 0<=j2<width): continue
                adjacency_list[idx].append(G[i2][j2])
    return adjacency_list
width = 3
height = 3
G = [[i for i in range(j*width, width+j*width)] for j in range(height)]
adjancecy_list = create_adjacency_list(width, height)
operation = width*height
element_num = width*height
ans = [0]
memo = [set() for _ in range(width*height)]
# def dfs(bit, x):
#     if bit == 0b11111111: return bit
#     if bit in memo[x]: 
#         ans.pop()
#         return bit & ~(1<<x)
#     for i in adjancecy_list[x]:
#         if i in ans: continue
#         next = bit | 1<< i
#         ans.append(i)
#         bit = dfs(next, i)
    
#     if bit == 0b11111111:
#         return bit
#     else: 
#         memo[x].add(bit)
#         return bit & ~(1<<x)

# bit = dfs(1, 0)
# print(ans)


dp = [[set() for _ in range(element_num)] for _ in range(operation)]
dp[0][0].add(1)
for i in range(operation-1):
    for j in range(element_num):
        if not dp[i][j]: continue

        for bit in list(dp[i][j]):
            for el in adjancecy_list[j]:
                if bit & 1<<el: continue # 値が含まれていれば
                dp[i+1][el].add(bit|1<<el)
# for row in G:
#     print(row)
for row in dp:
    print(*row)

# print(f"{255:09b}")
# print(f"{447:09b}")
# print(f"{507:09b}")
# print(f"{511:09b}")

# now = width*height-1
# ans = [width*height-1]

# def now_bit(route):
#     bit = 0
#     for i in route:
#         bit = bit | 1<<i
#     return bit

# for i in range(operation-2, -1, -1):
#     for j in adjancecy_list[now]:
#         if not dp[i][j]: continue
#         if j in set(ans): continue
#         for bit in list(dp[i][j]):
#             nowbit = now_bit(ans)
#             if bit & nowbit: continue # 含まれていたら
#             ans.append(j)
#             now = j
#             break
# print(ans)

