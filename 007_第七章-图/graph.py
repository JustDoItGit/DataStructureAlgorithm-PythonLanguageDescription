class GraphError(ValueError):
    pass


class Graph:  # 基本图类，采用邻接矩阵表示
    def __init__(self, mat, unconn=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:  # 检查是否为方阵
                raise ValueError('Argument for "Graph".')
        self._mat = [mat[i][:] for i in range(vnum)]
        self._unconn = unconn
        self._vnum = vnum

    def vertex_num(self):
        """ 获取这个图中定点的个数 """
        return self._vnum

    def _invalid(self, v):
        """ 检查顶点坐标是否有效 """
        return 0 > v or v >= self._vnum

    def add_vertex(self):
        raise GraphError('Adj-Matrix does not support "add_vertex".')

    def add_edge(self, vi, vj, val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + 'or' + str(vj) + ' is not a valid vertex.')
        self._mat[vi][vj] = val

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + 'or' + str(vj) + ' is not a valid vertex.')
        return self._mat[vi][vj]

    def out_edge(self, vi):
        if self._invalid(vi):
            raise GraphError(str(vi) + ' is not a valid vertex.')
        return self._out_edges(self._mat[vi], self._unconn)

    @staticmethod
    def _out_edges(row, unconn):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges

    def __str__(self):
        return '[\n' + ',\n'.join(map(str, self._mat)) + '\n]' + '\nUnconnected: ' + str(self._unconn)
