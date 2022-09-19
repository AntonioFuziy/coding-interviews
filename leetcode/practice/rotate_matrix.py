class Solution:
  def rotate(self, matrix: list[list[int]]) -> None:
    for i in range(len(matrix)):
      for j in range(i, len(matrix[0])):
        switch1 = matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = switch1
    for i in range(len(matrix)):
      matrix[i].reverse()