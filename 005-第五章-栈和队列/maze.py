from stack import SStack
import copy

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def mark(maze, pos):  # 给迷宫maze的位置pos标2表示'到过了'
    maze[pos[0]][pos[1]] = 2


def passable(maze, pos):  # 检查迷宫maze的位置pos是否可行
    return maze[pos[0]][pos[1]] == 0


# 递归实现
def find_path(maze, pos, end):
    mark(maze, pos)
    if pos == end:  # 已到达出口
        print(pos, end=' ')  # 输出这个位置
        return True  # 成功结束

    for i in range(4):  # 否则按四个方向顺序探查
        # 考虑下一个可能方向
        nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]  # 不可行的相邻位置不管
        if passable(maze, nextp):  # 从nextp可达出口
            if find_path(maze, nextp, end):  # 输出这个点
                print(pos, end=' ')  # 成功结束
                return True
    return False


# 回溯法求解
def maze_solver(maze, start, end):
    if start == end:
        print(start)
        return
    st = SStack()
    mark(maze, start)
    st.push((start, 0))  # 入口和方向0的序对入栈
    while not st.is_empty():  # 走不通时回退
        pos, nxt = st.pop()  # 取栈顶及其探查方向
        for i in range(nxt, 4):  # 依次检查未探查方向
            nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])  # 算出下一位置
            if nextp == end:  # 到达出口打印路径
                print(end, end=' ')
                print(pos, end=' ')
                while not st.is_empty():
                    print(st.pop()[0], end=' ')
                return
            if passable(maze, nextp):  # 遇到未探查的新位置
                st.push((pos, i + 1))  # 原位置和下一方向入栈
                mark(maze, nextp)
                st.push((nextp, 0))  # 新位置入栈
                break  # 退出内层循环，下次迭代将以新栈顶为当前位置继续
    print('No path found.')  # 找不到路径


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
    maze_for_solver = copy.deepcopy(maze_test)
    pos_test = (1, 1)
    end_test = (8, 8)
    find_path(maze_test, pos_test, end_test)
    print('')
    maze_solver(maze_for_solver, pos_test, end_test)
