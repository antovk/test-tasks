# First Missing Positive (leetcode hard)

## Task

<pre>
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1

Constraints:

1 <= nums.length <= 5 * 10^5
-2^31 <= nums[i] <= 2^31 - 1
</pre>

## Solution

```java
class Solution {

    public int firstMissingPositive(int[] nums) {
        int totalPosCnt = 0;
        int[] allPositives = new int[nums.length + 1];

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0 && nums[i] < allPositives.length) {
                allPositives[nums[i]] = 1;
                totalPosCnt += 1;
            }
        }

        for (int i = 1; i <= totalPosCnt; i++) {
            if (allPositives[i] == 0) {
                return i;
            }
        }

        return totalPosCnt + 1;
    }
}
```
