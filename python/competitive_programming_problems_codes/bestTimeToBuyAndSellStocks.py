def maxProfit(prices: list[int]) -> int:
  profit = 0
  for i in range(0, len(prices)):
    b = prices[i]
    print("b=", b)
    for j in range(i + 1, len(prices)):
      if prices[j] > b:
        s = prices[j]
        print("s=", s)
        if profit < s - b:
          profit = s - b
          print("profit=", profit)
  return profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
