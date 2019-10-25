//Given an array of integers, return indices of the two numbers such that they add up to a specific target. 
//
// You may assume that each input would have exactly one solution, and you may not use the same element twice. 
//
// Example: 
//
// 
//Given nums = [2, 7, 11, 15], target = 9,
//
//Because nums[0] + nums[1] = 2 + 7 = 9,
//return [0, 1].
// Related Topics Array Hash Table
package leetcode.editor.en;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Q1TwoSum {

    public static void main(String[] args) {
        Solution solution = new Q1TwoSum().new Solution();
        System.out.println(Arrays.toString(solution.twoSum(new int[]{2, 7, 13}, 9)));
    }


    //leetcode submit region begin(Prohibit modification and deletion)
    class Solution {
        public int[] twoSum(int[] nums, int target) {
            Map<Integer, Integer> map = new HashMap<>();
            for (int i = 0; i < nums.length; i++) {
                int complement = target - nums[i];
                if (map.containsKey(complement)) {
                    return new int[]{map.get(complement), i};
                }
                map.put(nums[i], i);
            }
            throw new IllegalArgumentException("new result");
        }
    }
    //leetcode submit region end(Prohibit modification and deletion)

}