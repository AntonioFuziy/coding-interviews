class Solution:
  def convert(self, s: str, numRows: int) -> str:
    if numRows == 1:
      return s
    rows = [''] * numRows
    row = 0
    goingDown = False
    for c in s:
      rows[row] += c
      if row == 0 or row == numRows - 1:
        goingDown = not goingDown
      if goingDown:
        row += 1
      else:
        row -= 1
    return ''.join(rows)