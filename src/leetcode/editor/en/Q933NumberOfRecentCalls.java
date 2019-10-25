//Write a class RecentCounter to count recent requests. 
//
// It has only one method: ping(int t), where t represents some time in
// milliseconds.
//
// Return the number of pings that have been made from 3000 milliseconds ago
// until now.
//
// Any ping with time in [t - 3000, t] will count, including the current ping. 
//
// It is guaranteed that every call to ping uses a strictly larger value of t
// than before.
//
// 
//
// Example 1: 
//
// 
//Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
//Output: [null,1,2,3,3] 
//
// 
//
// Note: 
//
// 
// Each test case will have at most 10000 calls to ping. 
// Each test case will call ping with strictly increasing values of t. 
// Each call to ping will have 1 <= t <= 10^9. 
// 
//
// 
// 
// Related Topics Queue
package leetcode.editor.en;

/**
 * Note: There are some faster methods
 */
public class Q933NumberOfRecentCalls {

    public static void main(String[] args) {
        RecentCounter counter = new Q933NumberOfRecentCalls().new RecentCounter();
        System.out.println(counter.ping(1));
        System.out.println(counter.ping(100));
        System.out.println(counter.ping(3001));
        System.out.println(counter.ping(3002));
    }


    //leetcode submit region begin(Prohibit modification and deletion)
    class RecentCounter {

        private final int[] queue;
        int len;

        public RecentCounter() {
            queue = new int[10000];
            len = 0;
        }

        public int ping(int t) {
            queue[len++] = t;
            int left = 0;
            int right = len - 1;

            while (left <= right) {
                int i = (left + right) / 2;
                if (t - queue[i] <= 3000) {
                    right = i - 1;
                } else {
                    left = i + 1;
                }
            }
            return len - left;
        }
    }

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */
//leetcode submit region end(Prohibit modification and deletion)

}