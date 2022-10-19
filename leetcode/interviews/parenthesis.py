def place_parenthesis(n: int) -> list(str):

  def generateParenthesis(n, Open, close, s, ans):

    if Open == n and close == n:
      ans.append(s)
      return

    if Open < n:
      generateParenthesis(n, Open + 1, close, s + "(", ans)

    if close < Open:
      generateParenthesis(n, Open, close + 1, s + ")", ans)

  ans = []
  generateParenthesis(n, 0, 0, "", ans)
  return ans


n = 10
ans = []
place_parenthesis(n)
for s in ans:
    print(s)
