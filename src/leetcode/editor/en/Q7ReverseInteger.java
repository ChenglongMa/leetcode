//Given a 32-bit signed integer, reverse digits of an integer. 
//
// Example 1: 
//
// 
//Input: 123
//Output: 321
// 
//
// Example 2: 
//
// 
//Input: -123
//Output: -321
// 
//
// Example 3: 
//
// 
//Input: 120
//Output: 21
// 
//
// Note: 
//Assume we are dealing with an environment which could only store integers within
// the 32-bit signed integer range: [−2^31, 2^31 − 1].
// For the purpose of this problem, assume that your function returns 0
// when the reversed integer overflows.
// Related Topics Math
package leetcode.editor.en;

public class Q7ReverseInteger {

    public static void main(String[] args) {
        Solution solution = new Q7ReverseInteger().new Solution();
        //2147483647
        //System.out.println(solution.reverse(2147483647));
        System.out.println(solution.reverse(-5));
        System.out.println(solution.reverse(-2147483648));
    }


    //leetcode submit region begin(Prohibit modification and deletion)
    class Solution {
        public int reverse(int x) {

            boolean neg = x < 0;
            x = neg ? -x : x;
            int res = 0, prev;
            do {
                int rem = x % 10;
                prev = res;
                res = res * 10 + rem;
                if (prev != (res - rem) / 10) {
                    return 0;
                }
                x /= 10;
            } while (x != 0);
            return neg ? -res : res;
        }
    }
//leetcode submit region end(Prohibit modification and deletion)

}