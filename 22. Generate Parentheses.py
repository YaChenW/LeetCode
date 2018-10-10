class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = self.getSolList(n)
        return list(self.getSolList(n)) if ret != None else None

    def getSolList(self, n, left=0, right=0, sol=""):
        if n < 1: return None
        if right > left: return None
        if left > n: return None
        ret = set()
        if left == n and right == n:
            ret.add(sol)
            return ret
        ret1 = self.getSolList(n, left + 1, right, sol + "(")
        ret2 = self.getSolList(n, left, right + 1, sol + ")")
        if ret1 != None: ret = ret | ret1
        if ret2 != None: ret = ret | ret2
        return ret