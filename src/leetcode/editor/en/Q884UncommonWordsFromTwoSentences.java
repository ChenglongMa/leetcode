//We are given two sentences A and B.
// (A sentence is a string of **space** separated words.
// Each word consists only of *lowercase* letters.)
//
// A word is uncommon if it appears exactly *once* in one of the sentences,
// and does not appear in the other sentence.
//
// Return a list of all uncommon words. 
//
// You may return the list in any order. 
//
// 
// Example 1: 
//
// 
//Input: A = "this apple is sweet", B = "this apple is sour"
//Output: ["sweet","sour"]
// 
//
// 
// Example 2: 
//
// 
//Input: A = "apple apple", B = "banana"
//Output: ["banana"]
// 
//
// 
//
// Note: 
//
// 
// 0 <= A.length <= 200 
// 0 <= B.length <= 200 
// A and B both contain only spaces and lowercase letters. 
// 
// 
// 
// Related Topics Hash Table
package leetcode.editor.en;

import java.util.HashSet;
import java.util.Set;

public class Q884UncommonWordsFromTwoSentences {

    public static void main(String[] args) {
        Solution solution = new Q884UncommonWordsFromTwoSentences().new Solution();
    }


    //leetcode submit region begin(Prohibit modification and deletion)
    class Solution {
        public String[] uncommonFromSentences(String A, String B) {
            String[] words = (A + " " + B).split(" ");
            Set<String> allDistWords = new HashSet<>();
            Set<String> commons = new HashSet<>();
            for (String s : words) {
                if (!allDistWords.add(s)) {
                    commons.add(s);
                }
            }
            String[] uncommons = new String[allDistWords.size() - commons.size()];
            int i = 0;
            for (String word : words) {
                if (commons.add(word)) {
                    uncommons[i++] = word;
                }
            }

            return uncommons;
        }
    }
//leetcode submit region end(Prohibit modification and deletion)

}