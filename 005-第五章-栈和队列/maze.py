dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def mark(maze, pos):  # 给迷宫maze的位置pos标2表示"到过了"
    maze[pos[0]][pos[1]] = 2


def passable(maze, pos):  # 检查迷宫maze的位置pos是否可行
    return maze[pos[0]][pos[1]] == 0


# 递归实现
def find_path(maze, pos, end):
    mark(maze, pos)
    if pos == end:  # 已到达出口
        print(pos, end=" ")  # 输出这个位置
        return True  # 成功结束

    for i in range(4):  # 否则按四个方向顺序探查
        # 考虑下一个可能方向
        nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]  # 不可行的相邻位置不管
        if passable(maze, nextp):  # 从nextp可达出口
            if find_path(maze, nextp, end):  # 输出这个点
                print(pos, end=" ")  # 成功结束
                return True
    return False


if __name__ == '__main__':
    maze_test = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 1, 1],
        [1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 1, 0, 0, 0, 1, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    pos_test = (1, 1)
    end_test = (8, 8)
    find_path(maze_test, pos_test, end_test)
