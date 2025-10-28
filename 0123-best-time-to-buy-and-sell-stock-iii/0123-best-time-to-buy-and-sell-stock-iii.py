class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n = len(prices)
        # minn = float('inf')
        # maxx = 0
        # sell = []
        # i = 0
        # while i < n:
        #     if prices[i] < minn:
        #         minn = prices[i]
        #         maxx = 0

        #     maxx = prices[i] - minn
        #     sell.append(maxx)
        #     i+=1
        
        # buy = []
        # j = n - 1
        # maxx = prices[-1]
        # minn = 0
        # while j >= 0:
        #     if prices[j] > maxx:
        #         maxx = prices[j]
        #         minn = 0
        #     minn = maxx - prices[j]
        #     buy.append(minn)
        #     j-=1

        
        # buy.reverse()
        # max_idx = 0
        # for i in range(n):
        #     if buy[i] >= buy[max_idx]:
        #         max_idx = i
        # max_pro = 0
        # for i in range(max_idx+1):
        #     max_pro = max(max_pro, sell[i])
        

        # return max_pro + buy[max_idx]
        mini = prices[0]
        sell = []
        for i in range(len(prices)):
            if mini > prices[i]:
                mini = prices[i]
            sell.append(prices[i] - mini)
        # print(sell)

        buy = []
        maxi = prices[-1]

        for j in range(len(prices)-1,-1,-1):
            if prices[j]> maxi:
                maxi = prices[j]
            buy.append(maxi-prices[j])
        buy = buy[::-1]
        
        prefix_max =[]
        max_2 = 0
        for k in range(len(sell)):
            if max_2 < sell[k]:
                max_2 =sell[k]
            prefix_max.append(max_2)

        final_ans = 0
        for t in range(len(prefix_max)):
            if buy[t] + prefix_max[t] > final_ans:
                final_ans = buy[t] + prefix_max[t]


        return final_ans