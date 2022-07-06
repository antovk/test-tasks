from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_len = len(nums1)
        nums2_len = len(nums2)

        median_index_1 = -1
        median_index_2 = -1

        nums_united = []

        if (nums1_len + nums2_len) % 2 != 0:
            # odd
            median_index_1 = int((nums1_len + nums2_len) / 2 - 0.5)
        else:
            # even
            median_index_1 = int((nums1_len + nums2_len) / 2 - 1)
            median_index_2 = int((nums1_len + nums2_len) / 2)

        cursor_pos_01 = 0
        cursor_pos_02 = 0

        while(cursor_pos_01 + cursor_pos_02 < median_index_1 + 2):
            n1 = 1_000_001
            n2 = 1_000_001

            if cursor_pos_01 < nums1_len:
                n1 = nums1[cursor_pos_01]

            if cursor_pos_02 < nums2_len:
                n2 = nums2[cursor_pos_02]

            if n1 < n2:
                nums_united.append(n1)
                cursor_pos_01 += 1

            if n1 > n2:
                nums_united.append(n2)
                cursor_pos_02 += 1

            if n1 == n2:
                nums_united.append(n1)
                nums_united.append(n2)
                cursor_pos_01 += 1
                cursor_pos_02 += 1

        if median_index_2 == -1:
            # odd
            return float(nums_united[median_index_1])
        else:
            # even
            return (nums_united[median_index_1] + nums_united[median_index_2]) / 2
