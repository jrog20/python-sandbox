# 121. Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a 
# different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, 
# return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

################################################################################################
# Brute force solution:

# We need to find the maximum different (max profit) between two numbers in the array.
# The second number (selling price) must be larger than the first number (buying price).
# We can do a double for loop to compare each starting number (buying price) with each
# next number in the array (possible selling prices)

# We need to find the max(prices[j] - prices[i]) for every i and j where j > i

# Time complexity: O(n^2)
# Space complexity: O(1)

# def max_profit(prices):
#     max_profit = 0
#     for i in range(len(prices) - 1):
#         for j in range(i + 1, len(prices)):
#             if prices[i] < prices[j]:
#                 profit = prices[j] - prices[i]
#                 max_profit = max(max_profit, profit)
#     return max_profit

################################################################################################
# One pass solution:

# We can iterate over the given array once, keeping track of the largest number following the
# smallest number. 

# We can initiate two variables, min_price and max_profit, to keep track of the lowest buy price
# and the maximum profit seen so far.

# Time complexity: O(n)
# Space complexity: O(1)

def max_profit(prices):
    min_price = prices[0]
    max_profit = 0
    for i in range(len(prices)):
        # if current element is less than min_price, make min_price equal to the current element
        if prices[i] < min_price:
            min_price = prices[i]
        # if current element - min_price is greater than max_profit, make max_profit equal to the
        # current best profit found
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    return max_profit

################################################################################################
prices = [7,1,5,3,6,4]
print('Expecting 5')
print(max_profit(prices))

prices = [7,6,4,3,1]
print('Expecting 0')
print(max_profit(prices))
