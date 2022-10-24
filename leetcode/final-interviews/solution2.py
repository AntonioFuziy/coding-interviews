def max_profit(prices: list[int]) -> int:
    max_value = 0
    i = 1
    while i < len(prices):
      if prices[i] > prices[i-1]:
        max_value += prices[i] - prices[i-1]
      i += 1
    return max_value

print(max_profit([1, 7, 2, 3, 6, 7, 6, 7]))

import matplotlib.pyplot as plt

plt.plot([0,1,2,3,4,5,6,7,8],[1,7,2,3,6,7,6,7,8])
plt.show()