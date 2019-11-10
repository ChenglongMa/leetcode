/*
 * @lc app=leetcode id=58 lang=csharp
 *
 * [58] Length of Last Word
 *
 * https://leetcode.com/problems/length-of-last-word/description/
 *
 * algorithms
 * Easy (32.33%)
 * Likes:    467
 * Dislikes: 1916
 * Total Accepted:    310K
 * Total Submissions: 958.6K
 * Testcase Example:  '"Hello World"'
 *
 * Given a string s consists of upper/lower-case alphabets and empty space
 * characters ' ', return the length of last word in the string.
 * 
 * If the last word does not exist, return 0.
 * 
 * Note: A word is defined as a character sequence consists of non-space
 * characters only.
 * 
 * Example:
 * 
 * 
 * Input: "Hello World"
 * Output: 5
 * 
 * 
 * 
 * 
 */

// @lc code=start
public class Solution
{
    public int LengthOfLastWord(string s)
    {
        if (s == null)
        {
            return 0;
        }
        var arr = s.TrimEnd().Split(' ');
        return arr[arr.Length - 1].Length;
    }
}
// @lc code=end

