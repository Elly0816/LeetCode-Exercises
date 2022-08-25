class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        inner = []
        outer = []
        print(m*n)
        print(r*c)
        if (m*n) != (r*c):
            return mat
        else:
            for i in range(m):
                for j in range(n):
                    if len(inner) < c:
                        inner.append(mat[i][j])
                    else:
                        outer.append(inner)
                        inner = []
                        inner.append(mat[i][j])
            if len(outer) != r:
                outer.append(inner)
            return outer