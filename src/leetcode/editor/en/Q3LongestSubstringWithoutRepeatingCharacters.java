//Given a string, find the length of the longest substring without repeating characters. 
//
// 
// Example 1: 
//
// 
//Input: "abcabcbb"
//Output: 3 
//Explanation: The answer is "abc", with the length of 3. 
// 
//
// 
// Example 2: 
//
// 
//Input: "bbbbb"
//Output: 1
//Explanation: The answer is "b", with the length of 1.
// 
//
// 
// Example 3: 
//
// 
//Input: "pwwkew"
//Output: 3
//Explanation: The answer is "wke", with the length of 3. 
//             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
// 
// 
// 
// 
// Related Topics Hash Table Two Pointers String Sliding Window
package leetcode.editor.en;

public class Q3LongestSubstringWithoutRepeatingCharacters {

    public static void main(String[] args) {
        Solution solution = new Q3LongestSubstringWithoutRepeatingCharacters().new Solution();
//        System.out.println(solution.lengthOfLongestSubstring("?><?{}|[]123"));
        System.out.println(solution.lengthOfLongestSubstring("pwwkew"));
        System.out.println(solution.lengthOfLongestSubstring("dvavfe"));
    }

    // TODO: 25/10/19 025 to be continued
    //leetcode submit region begin(Prohibit modification and deletion)
    class Solution {
        public int lengthOfLongestSubstring(String s) {
            if (s == null) {
                return 0;
            }
            int[] counter = new int[128];
            int maxLen = 0;
            int from = 0;
            for (int i = 0; i < s.length(); i++) {
                char curr = s.charAt(i);
                int c = counter[curr];
                if (counter[curr] != 0) {
                    maxLen = i - from;
                    from = counter[curr];
                }
                counter[curr] = i + 1;
                maxLen++;
            }
            return maxLen;
        }
    }
//leetcode submit region end(Prohibit modification and deletion)

}