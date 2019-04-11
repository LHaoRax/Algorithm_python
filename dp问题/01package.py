import sys
# 01背包问题
"""
有 n 个重量个价值分别为 w_i, v_i 的物品。
从这些物品中选出总重量不超过 W 的物品，使其总价值最大。

示例
1                // 用例数
5 10             // 物品数 背包容量 N <= 1000 , V <= 1000
1 2 3 4 5
5 4 3 2 1

14
"""
# 需要注意的点就是python中二维数组的初始化问题，很容易初始化为浅赋值，需要使用列表生成式初始化
def max_values(N, V, values, weights):
    dp = [[0 for i in range(V + 1)] for i in range(N + 1)]  # 用列表生成式来写二维数组的初始化
    for i in range(1, N + 1):
        for j in range(0, V + 1):
            if weights[i] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                max_number = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + values[i])
                dp[i][j] = max_number

    return dp[-1][-1]

if __name__ == '__main__':
    line = sys.stdin.readline().strip().split()
    line_num = list(map(int, line))
    N, V = line_num[0], line_num[1]

    values_line = sys.stdin.readline().strip().split()
    values = list(map(int, values_line))
    values.insert(0, 0)

    weights_line = sys.stdin.readline().strip().split()
    weights = list(map(int, weights_line))
    weights.insert(0, 0)

    print(max_values(N, V, values, weights))


