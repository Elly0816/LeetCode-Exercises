class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            triangle.append([])
        for i in range(len(triangle)):
             if i == 0:
                    triangle[i].append(1)
             else:
                for j in range(i+1):
                        if j-1 < 0 or j >= len(triangle[i-1]):
                            triangle[i].append(1)
                        else:
                            triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
        return triangle