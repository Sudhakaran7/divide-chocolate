class Solution(object):
    def maximizeSweetness(self, sweetness, K):
        """
        :type sweetness: List[int]
        :type K: int
        :rtype: int
        """
        def check(sweetness, K, x):
            curr, cuts = 0, 0
            for s in sweetness:
                curr += s
                if curr >= x:
                    cuts += 1
                    curr = 0
            return cuts >= K+1

        left, right = min(sweetness), sum(sweetness)//(K+1)
        while left <= right:
            mid = left + (right-left)//2
            if not check(sweetness, K, mid):
                right = mid-1
            else:
                left = mid+1
        return right

val=Solution()
n,k=map(int,input().split())
rows=list(map(int,input().split()))
print(val.maximizeSweetness(rows,k))
