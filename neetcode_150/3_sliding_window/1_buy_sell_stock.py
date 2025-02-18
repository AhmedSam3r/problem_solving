
def maxProfit_brute_force(prices):
    '''
    Time Complexity: O(n²)
    Space Complexity: O(1)

    '''
    max_profit = 0
    print("prices ==>", prices)
    for i in range(len(prices)):
        buy = prices[i]
        profit = 0
        for j in range(i+1, len(prices)):
            sell = prices[j]
            print(f"buy={buy}, sell={sell}")
            profit = sell - buy
            if profit > max_profit:
                print("profit ==>", profit)
                max_profit = profit

    return max_profit


def max_profit_one_pass(prices) -> int:
    """
    the solution is more clearer when you draw it as a graph
    the two pointers move together into one direction
    """
    print("prices=>", prices)
    l, r = 0, 1
    max_profit = 0
    for _ in range(len(prices)):
        if prices[r] > prices[l]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        else:
            # if the next number is smaller than the current number
            # then we move both cursor,
            l += 1
        r += 1


def max_profit_sliding_pointers(prices) -> int:
    """
    time complexity: O(n)
    space complexity: O(1)
    buy low, sell hi
    the solution is more clearer when you draw it as a graph
    latest submission, code more simpler
    always draw or visualize your solution

    """
    left, right = 0, 1
    profit = 0
    print(prices)
    while left < right < (len(prices)):
        # print(f"prices[{left}]={prices[left]}, prices[{right}]={prices[right]} && {prices[left] >= prices[right]}")
        # base number is 0, so we're sure of min is 0
        profit = max(profit, prices[right]-prices[left])
        if prices[left] >= prices[right]:
            # print("INSIDE")
            left = right
        right += 1

    return profit
    # older working solution
    # print("prices=>", prices)
    # max_profit = 0
    # l, r = 0, 1
    # while r < len(prices):
    #     if prices[r] > prices[l]:
    #         profit = prices[r] - prices[l]
    #         max_profit = max(max_profit, profit)
    #     else:
    #         # if the next number is smaller than the current number
    #         # then we move both cursor,
    #         l = r
    #     r += 1
    # return max_profit

def maxProfit_sort(prices: list):
    """
    too complex and incomplete
    """
    new_prices = list(enumerate(prices))
    new_prices = sorted(new_prices, key=lambda x: x[1])
    left, right = 0, len(new_prices)
    max_profit = 0
    while left < right:
        buy = prices[left][1]
        sell = prices[right][1]
        profit = sell - buy
        right_ind = prices[right][0] 
        left_ind = prices[left][0]
        if right_ind > left_ind and profit > max_profit:
            max_profit = profit

        if right_ind < left_ind:
            left += 1
        else:
            right -= 1

    return profit



            


    






prices = [7,1,5,3,6,4]
r = max_profit_one_pass(prices)
print("r==>", r)


prices = [7,6,4,3,1]
r = max_profit_one_pass(prices)
print("r==>", r)


prices = [7,6,4,3,1, 4, 3, 6, 10]
r = max_profit_one_pass(prices)
print("r==>", r)
