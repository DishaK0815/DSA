from typing import List
class Solution:
    def countPaths(self, i, j, n, m, dp):
        if i == (n - 1) and j == (m - 1):
            return 1
        if i >= n or j >= m:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        else:
            dp[i][j] = self.countPaths(
                i + 1, j, n, m, dp) + self.countPaths(i, j + 1, n, m, dp)
            return dp[i][j]


    def uniquePaths(self, m, n) :
        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]


        # dp[1][1]=1;
        num = self.countPaths(0, 0, m, n, dp)
        if m == 1 and n == 1:
            return num
        return dp[0][0]


if __name__ == "__main__":
    obj = Solution()
    totalCount = obj.uniquePaths(3, 7)
    print("The total number of Unique Paths are", totalCount)



class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N = n + m - 2
        r = m - 1
        res = 1
        for i in range(1, r + 1):
            res = res * (N - r + i) / i
        return int(res)




if __name__ == "__main__":
    obj = Solution()
    totalCount = obj.uniquePaths(2, 3)
    print("The total number of Unique Paths are", totalCount)