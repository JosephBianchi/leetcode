class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # length = len(nums1) + len(nums2)
        # if length % 2 == 0:
        #     return (nums1[-1] + nums2[1]) / 2
        # else:
        # >>>>>>>>>>>>>
        mergedlist = nums1 + nums2
        mergedlist.sort()
        print(mergedlist)
        length = len(mergedlist)
        if length % 2 != 0:
            median = int(length / 2)
            return mergedlist[median]
        else:
            endmedian = length / 2
            startmedian = length / 2 - 1
            median = (mergedlist[int(startmedian)] + mergedlist[int(endmedian)]) / 2
            return median

a = [1,3]
b = [2]
print(Solution().findMedianSortedArrays(a,b))
