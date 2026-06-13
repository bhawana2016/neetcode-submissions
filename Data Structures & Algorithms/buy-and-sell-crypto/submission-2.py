class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        My Wrong approach:
        1. I was calculating profit when increasing sequence ended. In tthat case,
        profit was not being calculated at all for a sorted array. This is incorrect
         because the best selling day may not be followed by a drop.
        2. I moved profit calculation out of if condition prices[j] < prices[i] even then 
        it was wrong. I believe what i did wrong was I was increasing i to i+1. Instead, I
        should have set i -> j (correct min_so_far)
        The deeper thinking mistake

You were tracking local patterns:

Increasing sequence ended → calculate profit
Lower value found → move one step ahead

The correct algorithm tracks global state:

min_price_so_far
max_profit_so_far

At each step:

1. Update min_price_so_far
2. Calculate profit if sold today
3. Update max_profit
        '''
        length = len(prices)
        i = j = 0
        max_profit = 0
        while j < length:
            print(i, j, prices[i], prices[j], max_profit)
            if prices[j] < prices[i]:
                i = j
            max_profit = max(max_profit, prices[j] - prices[i])
            j += 1
        return max_profit