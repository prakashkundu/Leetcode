class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a=abs(x)
        s=0
        while(a>0):
            d=a%10
            s=s*10+d
            a=a//10
        if(x<0):
            s=-s
        if(s>=-2**31 and s<=2**31-1):
            return s
        return 0