def max_profit(prices: list[int]) -> int:
    max_value = 0
    i = 0
    valley = prices[0]
    peak = prices[0]
    while i < len(prices) - 1:
      while i < len(prices) - 1 and prices[i] >= prices[i+1]:
        i += 1
      valley = prices[i]
      while i < len(prices) - 1 and prices[i] <= prices[i+1]:
        i += 1
      peak = prices[i]
      max_value += peak - valley
    return max_value

print(max_profit([7,1,5,3,6,4]))