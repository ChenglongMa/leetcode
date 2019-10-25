//Given an array of integers A sorted in non-decreasing order,
// return an array of the squares of each number,
// also in sorted non-decreasing order.
// 
// Example 1:
//Input: [-4,-1,0,3,10]
//Output: [0,1,9,16,100]
//
// 
// Example 2:
//Input: [-7,-3,2,3,11]
//Output: [4,9,9,49,121]
//
// Note:
// 1 <= A.length <= 10000 
// -10000 <= A[i] <= 10000 
// A is sorted in non-decreasing order.
// 
// Related Topics Array Two Pointers
package leetcode.editor.en;

import java.util.Arrays;

public class Q977SquaresOfASortedArray {

    public static void main(String[] args) {
        Solution solution = new Q977SquaresOfASortedArray().new Solution();
        System.out.println(Arrays.toString(solution.sortedSquares(new int[]{
                -7, -3, 2, 3, 11
        })));
    }


    //leetcode submit region begin(Prohibit modification and deletion)
    class Solution {
        public int[] sortedSquares(int[] A) {
            if (A == null || A.length == 0) {
                return null;
            }
            int len = A.length;
            int[] res = new int[len];
            int i = 0, j = 0, k = 0;
            while (j < len && A[j] < 0) {
                j++;
            }
            i = j - 1;
            while (i >= 0 && j < len) {
                int vi = A[i] * A[i];
                int vj = A[j] * A[j];
                if (vi < vj) {
                    res[k++] = vi;
                    i--;
                } else {
                    res[k++] = vj;
                    j++;
                }
            }
            while (i >= 0) {
                res[k++] = A[i] * A[i];
                i--;
            }
            while (j < len) {
                res[k++] = A[j] * A[j];
                j++;
            }
            return res;
        }
    }
    //leetcode submit region end(Prohibit modification and deletion)

}