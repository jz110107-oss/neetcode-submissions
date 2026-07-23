class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            arrayA = nums1
            arrayB = nums2
        else:
            arrayB = nums1
            arrayA = nums2
        
        half = (len(arrayA) + len(arrayB))//2
        l, r = 0, len(arrayA) - 1

        while True:
            middle = (l + r)//2
            remaining = half - middle - 2

            Aleft = arrayA[middle] if middle >= 0 else float("-infinity")
            Aright = arrayA[middle + 1] if middle + 1 < len(arrayA) else float("infinity")
            Bleft = arrayB[remaining] if remaining >= 0 else float("-infinity")
            Bright = arrayB[remaining + 1] if remaining + 1 < len(arrayB) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if (len(arrayA) + len(arrayB)) % 2 == 0:
                    return (max(Aleft,Bleft) + min(Aright,Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                r = middle - 1
            else:
                l = middle + 1




