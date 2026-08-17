# Question: Best Time to Buy and Sell Stock
# Find the maximum profit you can achieve by buying on one day and selling in the future.

# Way 1: One-Pass with Explicit If Statements (Time: O(N), Space: O(1))
class Solution1:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit

sol1 = Solution1()
print(sol1.maxProfit([7, 1, 5, 3, 6, 4]))

# Way 2: One-Pass using min() and max() (Time: O(N), Space: O(1))
class Solution2:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

sol2 = Solution2()
print(sol2.maxProfit([7, 1, 5, 3, 6, 4]))




# Way 3: Direct iteration without classes or functions
prices = [7, 1, 5, 3, 6, 4]
min_price = prices[0]  # Initialize with the first price
max_profit = 0

for price in prices:
    if price < min_price:
        min_price = price
    profit = price - min_price
    if profit > max_profit:
        max_profit = profit

print(max_profit)