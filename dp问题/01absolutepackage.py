import sys
import math
def cal_values(N, M, values, weights):
    """
    :param N: 总共多少件物品
    :param M: 背包容量
    :param values: 每件物品的价值
    :param weights: 每件物品的重量
    :return:
    """
    dp = [[-math.inf for i in range(M + 1)] for j in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = 0

    values.insert(0, 0)
    weights.insert(0, 0)
    for i in range(1, N + 1):      # 放入前i个物品
        for j in range(0, M + 1):  # 背包容量
            k = 0                  # 第i个物体放入k个
            while k * weights[i] <= j:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - k * weights[i]] + k * values[i])
                k += 1
    return dp[-1][-1]

if __name__ == '__main__':
    N = 5
    M = 10

    values = [5, 4, 3, 2, 1]
    weights = [3, 3, 3, 3, 3]
    print(cal_values(N, M, values, weights))