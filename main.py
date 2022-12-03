import time
import sys
from PathCreation import PathCreation
sys.setrecursionlimit(10000000)


def main():
    width = 6
    height = 6
    pc = PathCreation(width, height)
    pc.create_map_and_adjacency_list()

    sy, sx = 0, 0
    gy, gx = height-1, width-1
    pc.set_goal((sy, sx), (gy, gx))

    # for row in pc.G:
    #     print(row)
    pretime = time.time()
    dp1 = pc.create_dp()
    dp1 = pc.dp_forward(dp1)
    dp2 = pc.dp_backward(dp1)
    # print("done dp")
    # print("###################")
    # for row in dp1:
    #     print(row)
    # print("###################")
    # for row in dp2:
    #     print(row)

    route = pc.find_route(dp2)
    newtime = time.time()
    # print(route)
    print("実行時間:", newtime-pretime)

    result_route_map = pc.reformat_map(route)
    for row in result_route_map:
        print(row)

if __name__ == "__main__":
    main()

