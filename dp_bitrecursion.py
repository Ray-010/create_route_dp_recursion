from PathCreation import PathCreation


# def dfs(bit, x):


def main():
    width = 1
    height = 100
    start = [0, 0]
    goal = [height-1, width-1]

    pc = PathCreation(width, height, start, goal)
    pc.create_bfs_map()
    for row in pc.bfs_map:
        print(row)
    for row in pc.adjacency_list:
        print(row)
    # dp1 = pc.create_dp()
    # dp1 = pc.dp_forward(dp1)
    # dp2 = pc.dp_backward(dp1)

if __name__ == "__main__":
    main()
