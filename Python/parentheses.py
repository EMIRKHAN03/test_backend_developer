from functools import lru_cache

def countWellFormedParenthesis(nCouples: int) -> int:
    @lru_cache(maxsize=None)
    def catalan(n):
        if n == 0:
            return 1
        res = 0
        for i in range(n):
            res += catalan(i) * catalan(n - i - 1)
        return res
    return catalan(nCouples)