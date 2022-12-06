import time
import sys
from PathCreation import PathCreation
sys.setrecursionlimit(10000000)

def main():
    width = height = 20
    sy, sx = 0, 0
    gy, gx = height-1, width-1
    pc = PathCreation(width, height, (sy,sx), (gy,gx))

    pretime = time.time()

    dp1 = pc.create_dp()
    dp1 = pc.dp_forward(dp1)
    dp2 = pc.dp_backward(dp1)
    route = pc.find_route_by_bitdfs(dp2)
    newtime = time.time()

    result_route_map = pc.reformat_map(route)
    for row in result_route_map:
        print(row)
    print("実行時間:", newtime-pretime)

if __name__ == "__main__":
    main()

