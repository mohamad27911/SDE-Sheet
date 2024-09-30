class Solution(object):
    def setZeroes(self, matrix):
        s = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    s.add((i, j))
        for (i, j) in s:
            for col in range(len(matrix[0])):
                matrix[i][col] = 0
            for row in range(len(matrix)):
                matrix[row][j] = 0
        print(matrix)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
sol = Solution()
sol.setZeroes(matrix)
