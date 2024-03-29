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

import java.util.HashMap;
import java.util.Map;

public class Q3LongestSubstringWithoutRepeatingCharacters {

    public static void main(String[] args) {
        Solution solution = new Q3LongestSubstringWithoutRepeatingCharacters().new Solution();
//        System.out.println(solution.lengthOfLongestSubstring("?><?{}|[]123"));
        System.out.println(solution.lengthOfLongestSubstring("pwwkew"));
        System.out.println(solution.lengthOfLongestSubstring("dvavfe"));
    }

    //         TODO: 25/10/19 025 to be continued
    //leetcode submit region begin(Prohibit modification and deletion)
    public class Solution {
        public int lengthOfLongestSubstring(String s) {
            int n = s.length(), ans = 0;
            Map<Character, Integer> map = new HashMap<>(); // current index of character
            // try to extend the range [i, j]
            for (int j = 0, i = 0; j < n; j++) {
                if (map.containsKey(s.charAt(j))) {
                    i = Math.max(map.get(s.charAt(j)), i);
                }
                ans = Math.max(ans, j - i + 1);
                map.put(s.charAt(j), j + 1);
            }
            return ans;
        }
    }
//leetcode submit region end(Prohibit modification and deletion)

}