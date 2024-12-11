class Solution:
    def mySqrt(self, x: int) -> int:
        res = str(x**(1/2))

        if "." in res:
            return int(res.split(".")[0])

        return int(res)