import time
import sys
import random
from PathCreation import PathCreation
sys.setrecursionlimit(10000000)

def main():
    # height = random.randint(2, 10)
    # width = random.randint(2, 10)
    map_size = [2, 3, 4, 5, 6]
    fill_ratios = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    map_size = [3]
    # fill_ratios = [0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09]
    fill_ratios = [0]
    times = 1

    for ratio in fill_ratios:
        print("####################", ratio)
        fill_ratio = ratio
        for size in map_size:
            height = width = size
            time_record = set()
            for i in range(times):
                sy, sx = 0, random.randint(0, width-1)
                while True:
                    gy, gx = random.randint(0, height-1), random.randint(0, width-1)
                    yx = random.choice([0,1])
                    if yx == 0: gy = random.choice([0, height-1])
                    else: gx = random.choice([0, width-1])
                    if not (gx == sx and gy == sy): break
                pc = PathCreation(width, height, (sy,sx), (gy,gx))
                
                pretime = time.time()
                dp1 = pc.create_dp()
                dp1 = pc.dp_forward(dp1)
                cnt = 0
                bit_cnt = 0
                while True:
                    dp2 = pc.dp_backward(dp1, fill_ratio+cnt)
                    # route = pc.find_route(dp2) # 再帰経路復元
                    # bit_new_cnt, route = pc.find_route_by_bitmemo_dfs(dp2) # メモ化再帰経路復元
                    # bit_new_cnt, route = pc.find_route_by_bitmemo_bfs_dfs(dp2) # bfsメモ化再帰経路復元
                    route = pc.find_route_by_bfs_dfs(dp2) # bfs再帰経路復元

                    # route = pc.find_route_ex_dp() # dp無しの純粋な経路探索
                    cnt += 0.1
                    if route: break
                    if cnt == 1: break
                result_route_map = pc.reformat_map(route)
                newtime = time.time()
                time_record.add(newtime-pretime)
                # bit_cnt = max(bit_new_cnt, bit_cnt)
                # print(f"done {i} time")
            for row in result_route_map:
                print(row)
            # for row in dp1:
            #     print(row)
            
            print("size:", size, "ratio:", fill_ratio)
            # print("bit cnt:", bit_cnt)
            print("実行平均時間:", sum(time_record)/len(time_record))
            print("最悪実行時間:", max(time_record))
            print("最小実行時間:", min(time_record))

if __name__ == "__main__":
    main()

