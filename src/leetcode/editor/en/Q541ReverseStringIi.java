//
//Given a string and an integer k, you need to reverse the first k characters
// for every 2k characters counting from the start of the string.
// If there are less than k characters left, reverse all of them.
// If there are less than 2k but greater than or equal to k characters,
// then reverse the first k characters and left the other as original.
// 
//
// Example: 
// 
//Input: s = "abcdefg", k = 2
//Output: "bacdfeg"
// 
// 
//
//Restrictions: 
// 
// The string consists of lower English letters only. 
// Length of the given string and k will in the range [1, 10000] 
// Related Topics String
package leetcode.editor.en;

public class Q541ReverseStringIi {

    public static void main(String[] args) {
        Solution solution = new Q541ReverseStringIi().new Solution();
        System.out.println(solution.reverseStr("abcdefg", 2));
    }


    //leetcode submit region begin(Prohibit modification and deletion)
    class Solution {
        private char[] reverseK(String s, int k) {
            char[] cs = s.toCharArray();
            int len = Math.min(s.length(), k);
            for (int i = 0; i < len / 2; i++) {
                char t = cs[i];
                cs[i] = cs[len - 1 - i];
                cs[len - 1 - i] = t;
            }
            return cs;
        }

        public String reverseStr(String s, int k) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < s.length(); i += 2 * k) {
                String sbs = s.substring(i, Math.min(s.length(), 2 * k + i));
                sb.append(reverseK(sbs, k));
            }
            return sb.toString();
        }
    }
//leetcode submit region end(Prohibit modification and deletion)

}