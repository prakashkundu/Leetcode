class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        odd=[]
        for x in nums1:
            if(x%2==1):
                odd.append(x)
        if(len(odd)==0):
            return True
        smallest_odd=min(odd)
        for x in nums1:
            if (x%2==0 and x<smallest_odd):
                return False
        return True

        